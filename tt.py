from splinter import Browser
from selenium import webdriver
from datetime import datetime, timedelta
import time
import argparse





b=Browser('firefox')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simulate to login Jing Dong, and buy sepecified good')
    parser.add_argument('-d', '--bday', 
                        help='buy day', default='')
    parser.add_argument('-t', '--btime', 
                        help='buy time', default='0')

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
 
    #b.visit('https://passport.jd.com/new/login.aspx?ReturnUrl=https://item.jd.com/3857525.html')
    b.visit('https://passport.jd.com/new/login.aspx?ReturnUrl=https://item.jd.com/4390094.html')
    uu=b.find_link_by_text('账户登录')
    uu.click()
    b.fill('loginname', '18371542519')
#    b.fill('loginname','18371542519')
    b.fill('nloginpwd', 'Super123!')
    b.find_by_id('loginsubmit').click()
    # b.visit('https://item.jd.com/3763103.html')

     # qg =b.find_by_id('choose-btn-ko')
    tryb = b.find_by_id('tryBtn')
    lentry = tryb.__len__()
    if lentry != 1:
        print('reload')
        b.reload()

    if lentry == 1:
        print('try buy ')
        tryb.click()
        
        b.find_by_id('saveConsigneeTitleDiv').click()
        b.find_by_id('order-submit').click()
#    qg = b.find_by_id('choose-btn-ko')
    qg = b.find_by_id('choose-btn-qiang')
    ttttt = qg.__len__()
    print('ttttt %d' % ttttt)
    if ttttt == 1:
        qbhtml = qg.first.outer_html
        enable = qbhtml.find('btn-disable')
        print('enable %d     %s' % (enable, qbhtml))
        if enable == -1:
            print('buy')
            qg.click()
            b.find_by_id('saveConsigneeTitleDiv').click()
            b.find_by_id('order-submit').click()

                        
                


    
