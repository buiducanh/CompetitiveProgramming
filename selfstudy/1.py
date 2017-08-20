format = int(raw_input().strip())
time = raw_input()

hours, minutes = time.strip().split(':')

# transform hours
if format == 12:
    if hours[1] == '0':
        if hours[0] != '1':
            hours = '1' + hours[1:]
    else:
        if int(hours) > 12:
            hours = '0' + hours[1:]
elif format == 24:
    if int(hours) > 23:
        hours = '1' + hours[1:]

# transform minutes
if int(minutes) > 59:
    minutes = '5' + minutes[1:]

print('{}:{}'.format(hours, minutes))

