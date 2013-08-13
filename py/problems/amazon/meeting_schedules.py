from datetime import datetime,time,timedelta,date
todate=date.today()
today=datetime.combine(todate,time(0,0))
eod=datetime.combine(todate,time(0,0)) +timedelta(days=1)

def make_time_range(str_):
    sh,sm,eh,em = map(int,str_.split(' '))
    return datetime.combine(todate,time(sh,sm)),datetime.combine(todate,time(eh,em))

n,mins=map(int,raw_input().split(' '))
times = sorted([make_time_range(raw_input()) for i in range(n)]) 
free_times=[]

if today<times[0][0]:
    free_times.append((today,times[0][0]))
max_=times[0][1]   
for i in range(1,len(times)):
    if times[i][0]>max_:
        free_times.append((max_,times[i][0]))
    if times[i][1]>max_:
        max_=times[i][1]
      
if max_<eod:
   free_times.append((max_,eod))
#print free_times
for start,end in free_times:
    if (end-start).total_seconds()//60>=mins:
        #print start,end
        print (str(start.hour).zfill(2) + ' ' + str(start.minute).zfill(2) + ' ' 
                + str(end.hour).zfill(2) + ' '+ str(end.minute).zfill(2))