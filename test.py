import time
from datetime import datetime
if __name__ == '__main__':
    i=0
    for j in range(0,25):
        print('********%d'%(j%24))
    t1=datetime.now()
    time.sleep(1)
    t2=datetime.now()
    tt= t2-t1
#    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'sleep 1')
    t3=datetime.strptime('2017-03-01 00:00:00','%Y-%m-%d %H:%M:%S')
    ttt= t3-t2
    print('span %d'% ttt.seconds)
#     while(i<65535*65536):
#         time.sleep(1)
#         print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'sleep 1')
#         i=i+1