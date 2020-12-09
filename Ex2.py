import sys
import datetime,time
print(sys.version,'\n',sys.version_info)
print(datetime.datetime(2020,5,13),datetime.datetime.today())
#print(datetime.datetime.today())
#print(datetime.date.today())
#print()
print(time.localtime(time.time()))
#print(type(time.localtime(time.time())))
print(time.time())
print(time.asctime(time.localtime(time.time())))

for i in range(0,5):
    if i<4:
        print(i,end=',')
    else:
        print(i)
    time.sleep(1)