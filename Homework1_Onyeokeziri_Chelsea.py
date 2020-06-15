#Chelsea Onyeokeziri 1570698

print('Birthday Calculator')
print ('Current day')


current_month=int(input('Month:'))
current_day =int(input('Day:'))
current_year =int(input('Year:'))

cday= current_month+current_day

print('Birthday')

birth_month=int(input('Month:'))
birth_day=int(input('Day:'))
birth_year=int(input('Year:'))

bday= birth_month+birth_day

print('You are',(current_year-birth_year),'years old.')

if cday==bday:
    print('Happy Birthday!')


