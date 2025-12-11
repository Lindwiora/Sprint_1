time = '1h 45m,360s,25m,30m 120s,2h 60s'

amount_minutes = 0

total_time = time.replace(',', ' ').split(' ')

for time in total_time:
    if 's' in time:
        seconds = int(time.replace('s', ''))
        amount_minutes += int(seconds // 60)

    if 'm' in time:
        minutes = int(time.replace('m', ''))
        amount_minutes += int(minutes)

    if 'h' in time:
        hours = int(time.replace('h', ''))
        amount_minutes += int(hours * 60)


print('Общее количество минут: ', amount_minutes)