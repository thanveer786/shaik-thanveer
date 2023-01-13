month=input("input the month(e.g january,february,etc.):")
day=int(input("input the day:"))
if month in ('january','february','march'):
    season='winter'
elif month in ('aoril','may','june'):
    season='summer'
elif month in ('july','august','september'):
    season='spring"
else:
    season='autum'

if(month=='june')and (day>20):
    season='spring'
elif(month=='march')and (day>19):
    season='summer'
elif(month=='september')and(day>21):
    season='autum'
elif(month=='december')and(day>20):
    season='winter'
print("season is",season)
