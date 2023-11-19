import enum
from datetime import datetime, timedelta, tzinfo, timezone

import pytz
import tzlocal


# %Y：四位数的年份表示（例如：2023）
# %m：两位数的月份表示（01到12）
# %d：两位数的日期表示（01到31）
# %H：24小时制的小时表示（00到23）
# %M：分钟表示（00到59）
# %S：秒表示（00到59）
# %f：微秒表示（000000到999999）
# %a：星期几的简写（例如：Mon）
# %A：星期几的全称（例如：Monday）
# %b：月份的简写（例如：Jan）
# %B：月份的全称（例如：January）
# %c：完整的日期和时间表示（例如：Tue Jan 23 14:23:01 2023）
# %p：上午或下午表示（AM或PM）
# %I：12小时制的小时表示（01到12）
# %j：一年中的第几天（001到366）
# %U：一年中的第几周（以周日为一周的开始，00到53）
# %W：一年中的第几周（以周一为一周的开始，00到53）
# %x：适用于当前区域设置的日期表示（例如：01/23/23）
# %X：适用于当前区域设置的时间表示（例如：14:23:01）
# %Z：时区名称（例如：EST）

class TimeLayout(enum.Enum):
    """
    枚举时间格式，其他格式根据上述格式自行设计,使用时注意 .value
    """
    RFC3339 = '%Y-%m-%dT%H:%M:%SZ'
    RFC3339Nano = '%Y-%m-%dT%H:%M:%S.%fZ'
    time_z = '%Y-%m-%d %H:%M:%S%z'
    YMDhms = '%Y-%m-%d %H:%M:%S'
    YMDhms2 = '%Y/%m/%d %H:%M:%S'
    YMD = '%Y-%m-%d'
    YMD2 = '%Y/%m/%d'
    hms = '%H:%M:%S'
    number_time = '%Y%m%d%H%M%S'


class UTC(tzinfo):
    """
    A UTC class timezone
    offset: UTC offset in hours (e.g. +1, -2, 0)
    """

    def __init__(self, offset=0):
        self._offset = offset

    def utcoffset(self, dt):
        return timedelta(hours=self._offset)

    def tzname(self, dt):
        return "UTC +%s" % self._offset

    def dst(self, dt):
        return timedelta(hours=self._offset)


def is_validator_time(time_str: str):
    """
    判断时间字符串是否符合TimeLayout里定义的时间格式,符合的话返回datetime对象
    :param time_str:
    :return:
    """
    for layout in TimeLayout:
        try:
            time = datetime.strptime(time_str, layout.value)
            return time
        except ValueError:
            continue
    raise ValueError("There is no matching time format in TimeLayout")


def convert_time_tz(time_str: str, time_zone=None, target_zone=None):
    """
    :param time_str:时间字符串
    :param time_zone:时间字符串所在时区。
        这个值的优先级最高。会覆盖字符串自带的时区信息。
        如果为None，则默认为字符串自带的时区，如果字符串没有时区，则默认为中时区。
    :param target_zone:目标时区，默认为本地时区
    :return:
    """
    origin_time = is_validator_time(time_str)
    origin_tz_time = origin_time

    if time_zone is not None:
        origin_tz_time = origin_time.replace(tzinfo=UTC(time_zone))
    elif origin_time.tzinfo is None:
        origin_tz_time = origin_time.replace(tzinfo=UTC(0))

    if target_zone is None:
        local_zone = pytz.timezone(tzlocal.get_localzone_name())
        target_time = origin_tz_time.astimezone(local_zone)
    else:
        target_time = origin_tz_time.astimezone(UTC(target_zone))
    return target_time


def datetime_convert_timezone(time: datetime, target_zone: int) -> datetime:
    """
    用于将datetime对象转为指定时区的datetime对象
    :param target_zone:
    :param time:datetime对象
    """
    return time.astimezone(UTC(target_zone))


if __name__ == "__main__":
    time1 = "2021/01/01 00:00:00"
    date_time_1 = convert_time_tz(time1).strftime("%Y%m%d%H%M%S")
    print(date_time_1)
