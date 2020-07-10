exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_total_replace = exam_hour * 60 + exam_minutes
arrival_total_replace = arrival_hour * 60 + arrival_minutes

if exam_total_replace >= arrival_total_replace:
    check = exam_total_replace - arrival_total_replace
    if check > 30:
        h = check // 60
        m = check % 60
        if h >= 1:
            print('Early')
            print(f'{h}:{str(m).zfill(2)} hours before the start')
        else:
            print('Early')
            print(f'{str(m)} minutes before the start')
    elif 0 < check <= 30:
        print('On time')
        print(f'{check} minutes before the start')
    elif check == 0:
        print('On time')


elif exam_total_replace < arrival_total_replace:
    check = arrival_total_replace - exam_total_replace
    h = check // 60
    m = check % 60
    if h >= 1:
        print('Late')
        print(f'{h}:{str(m).zfill(2)} hours after the start')
    else:
        print('Late')
        print(f'{str(m)} minutes after the start')

