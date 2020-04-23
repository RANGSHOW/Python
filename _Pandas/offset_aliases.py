import pandas as pd
offset_aliases = \
'''Date Offset

Frequency String

Description

DateOffset

None

Generic offset class, defaults to 1 calendar day

BDay or BusinessDay

'B'

business day (weekday)

CDay or CustomBusinessDay

'C'

custom business day

Week

'W'

one week, optionally anchored on a day of the week

WeekOfMonth

'WOM'

the x-th day of the y-th week of each month

LastWeekOfMonth

'LWOM'

the x-th day of the last week of each month

MonthEnd

'M'

calendar month end

MonthBegin

'MS'

calendar month begin

BMonthEnd or BusinessMonthEnd

'BM'

business month end

BMonthBegin or BusinessMonthBegin

'BMS'

business month begin

CBMonthEnd or CustomBusinessMonthEnd

'CBM'

custom business month end

CBMonthBegin or CustomBusinessMonthBegin

'CBMS'

custom business month begin

SemiMonthEnd

'SM'

15th (or other day_of_month) and calendar month end

SemiMonthBegin

'SMS'

15th (or other day_of_month) and calendar month begin

QuarterEnd

'Q'

calendar quarter end

QuarterBegin

'QS'

calendar quarter begin

BQuarterEnd

'BQ

business quarter end

BQuarterBegin

'BQS'

business quarter begin

FY5253Quarter

'REQ'

retail (aka 52-53 week) quarter

YearEnd

'A'

calendar year end

YearBegin

'AS' or 'BYS'

calendar year begin

BYearEnd

'BA'

business year end

BYearBegin

'BAS'

business year begin

FY5253

'RE'

retail (aka 52-53 week) year

Easter

None

Easter holiday

BusinessHour

'BH'

business hour

CustomBusinessHour

'CBH'

custom business hour

Day

'D'

one absolute day

Hour

'H'

one hour

Minute

'T' or 'min'

one minute

Second

'S'

one second

Milli

'L' or 'ms'

one millisecond

Micro

'U' or 'us'

one microsecond

Nano

'N'

one nanosecond'''

off = offset_aliases.split('\n')
new_off = []
for i in off:
    if i is not '':
        new_off.append(i)
new_off
new_off_col = new_off[0:3]
data_offset_list = []
frequency_list = []
desc_list = []
for i in range(len(new_off)):
    if i % 3 == 0:
        data_offset_list.append(new_off[i])
    elif i % 3 == 1:
        frequency_list.append(new_off[i])
    else:
        desc_list.append(new_off[i])
data_offset_list = data_offset_list[1:]
frequency_list = frequency_list[1:]
desc_list = desc_list[1:]
offset_alias = pd.DataFrame({new_off_col[0]: data_offset_list, new_off_col[1]: frequency_list, new_off_col[2]: desc_list})


