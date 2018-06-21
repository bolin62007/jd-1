from splinter import Browser
from selenium import webdriver
from datetime import datetime, timedelta
import time
import argparse
from click.decorators import password_option
from pip._vendor.requests.packages.urllib3.util import url




PRICE = ""
b=Browser('firefox')

#b=webdriver.Chrome()    
def endStep():
    nprice = PRICE
    while nprice == PRICE:
        b.reload()
        nprice = b.find_by_id('needPayPrice').value
        print ("%s-->current price:%s" % (datetime.datetime.now().strftime("%H:%M:%S.%f"), nprice))
    print ("submit order.....")
    b.find_by_id('submit').click()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simulate to login Jing Dong, and buy sepecified good')
    parser.add_argument('-u', '--username', 
                        help='Jing Dong login user name', default='')
    parser.add_argument('-p', '--password', 
                        help='Jing Dong login user password', default='')
    parser.add_argument('-g', '--good', 
                        help='Jing Dong good ID', default='')
    parser.add_argument('-d', '--bday', 
                        help='buy day', default='')
    parser.add_argument('-t', '--btime', 
                        help='buy time', default='0')
#     
#     
    options = parser.parse_args()
    print( options)
    buyd=options.bday
    buyt=options.btime
    user=options.username
    ppp= options.password
    item=options.good
#     buyh=int(options.bhour)
#     buym=int(options.bminute)
#     buyh=24
#     buym=15
#     if buym==0:
#         bbm=59
#         bbh=buyh-1
#     else:
#         bbm=buym-1
#         bbh=buyh
#         
    # for test
    print ("start.....")
#    
    t3=datetime.strptime(buyd+' '+buyt,'%Y-%m-%d %H:%M:%S')
    #t3=datetime.strptime('2017-03-02 00:00:00','%Y-%m-%d %H:%M:%S')
    #b.visit('https://passport.jd.com/new/login.aspx?ReturnUrl=https://cart.jd.com/order/orderInfoMain.html')
    #b.visit('https://passport.jd.com/new/login.aspx?ReturnUrl=https://item.jd.com/4325034.html')
    url='https://passport.jd.com/new/login.aspx?ReturnUrl=https://item.jd.com/'+item+'.html'
#    b.visit('https://passport.jd.com/new/login.aspx?ReturnUrl=https://item.jd.com/4390094.html')
    b.visit(url)
    uu=b.find_link_by_text('账户登录')
    uu.click()
    b.fill('loginname',user)
#    b.fill('loginname','18371542519')
    b.fill('nloginpwd',ppp)
    b.find_by_id('loginsubmit').click()
    #b.visit('https://item.jd.com/3763103.html')
    tt=datetime.now()
    tttt= t3-tt
    ttt= tttt.days*24*60*60+tttt.seconds
    while (ttt>-60*15):

        tt=datetime.now()
        tttt=t3-tt
        
        ttt= tttt.days*24*60*60+tttt.seconds
        print ('timespan:%d'%ttt) 
        if(ttt>60*20 ):
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'sleep 15')
            time.sleep(60*15)
            b.reload
            #print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'sleep 15')
            continue
        else:
            if (ttt>=60*2):
                print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'sleep 1')
                time.sleep(60)
                
                continue
            else: 
                if(ttt<60*2 and ttt>=7):
                    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'sleep 1 second')
                    time.sleep(1)
                    
                    continue
                else: 
                    if(ttt<7 and ttt >-60*15):
                        #qg =b.find_by_id('choose-btn-ko')
                        tryb = b.find_by_id('tryBtn')
                        lentry=tryb.__len__()
                        if lentry != 1:
                            print('reload')
                            b.reload()
            
                        if lentry ==1:
                            print('try buy ')
                            tryb.click()
                            
                            b.find_by_id('saveConsigneeTitleDiv').click()
                            b.find_by_id('order-submit').click()
                            continue
                        qg =b.find_by_id('choose-btn-ko')
                        ttttt= qg.__len__()
                        print('ttttt %d'%ttttt)
                        if ttttt==1:
                            qbhtml=qg.first.outer_html
                            enable=qbhtml.find('btn-disable')
                            print('enable %d     %s'%(enable, qbhtml))
                            if enable ==-1:
                                print('buy')
                                qg.click()
                                b.find_by_id('saveConsigneeTitleDiv').click()
                                b.find_by_id('order-submit').click()
        
                        
                


    