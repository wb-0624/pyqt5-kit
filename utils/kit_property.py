from PyQt5.QtCore import *


class KitNotifyProperty(pyqtProperty):
    class PropertyObject(QObject):
        changed = pyqtSignal(QVariant)

        def __call__(self, *args, **kwargs):
            return self._value

        def __init__(self, PropertyType):
            super(KitNotifyProperty.PropertyObject, self).__init__()
            self._value = None

        def set(self, value):
            if value == self._value:
                return
            self._value = value
            self.changed.emit(self._value)

        def bind(self, obj: QObject, propertyName: str, onChange: 'def (src: srcType)->destType' = None):
            if onChange is None:
                self.changed.connect(lambda value: obj.setProperty(propertyName, value))
            else:
                self.changed.connect(lambda value: obj.setProperty(propertyName, onChange(value)))

        def get(self):
            return self._value

    def __set__(self, instance, value):
        self.setPropertyValue(instance, value)

    def __get__(self, instance, owner) -> PropertyObject:
        return self.getPropertyObj(instance)

    def __init__(self, propertyType):
        self._properties: dict[QObject, KitNotifyProperty.PropertyObject] = {}

        def _getPropertyObj(owner: QObject) -> KitNotifyProperty.PropertyObject:
            try:
                return self._properties[owner]
            except KeyError:
                self._properties[owner] = \
                    self.PropertyObject(propertyType)

                def removeProperty():
                    del self._properties[owner]

                owner.destroyed.connect(removeProperty)
                return self._properties[owner]

        def _getPropertyValue(owner: QObject):
            return _getPropertyObj(owner)()

        def _setPropertyValue(owner: QObject, value) -> None:
            _getPropertyObj(owner).set(value)

        self.getPropertyObj = _getPropertyObj
        self.setPropertyValue = _setPropertyValue
        super(KitNotifyProperty, self).__init__(type=propertyType, fget=_getPropertyValue,
                                                fset=_setPropertyValue)


class Meal(QObject):

    def __int__(self):
        super(Meal, self).__int__()

    temperature = KitNotifyProperty(int)
    calorie = KitNotifyProperty(int)


def main():
    a = QCoreApplication([])
    meal = Meal()
    meal2 = Meal()
    # 直接 属性.信号名 的方式获取信号
    meal.temperature.changed.connect(lambda value: print("meal on temperature changed:", value))
    meal.calorie.changed.connect(lambda value: print("meal on calorie changed:", value))
    meal2.temperature.changed.connect(lambda value: print("meal2 on temperature changed:", value))
    meal2.calorie.changed.connect(lambda value: print("meal2 on calorie changed:", value))
    # 属性绑定，将meal2和meal对象进行默认的属性绑定
    meal.temperature.bind(meal2, "temperature")
    meal.calorie.bind(meal2, "calorie")
    # setProperty的方式触发值改变信号
    meal.setProperty("temperature", 50)
    meal.setProperty("calorie", 1000)
    # property的方式访问属性值
    print("temperature: ", meal.property("temperature"))
    print("calorie: ", meal.property("calorie"))
    # 赋值的方式触发值改变信号
    meal.temperature = 60
    meal.calorie = 2000
    # 获取属性值的另外两种方式 .get() 和 ()
    print("temperature", meal.temperature())
    print("calorie", meal.calorie.get())


if __name__ == '__main__':
    main()

