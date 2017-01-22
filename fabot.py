'''
IT IS JUST FOR EDUCATIONAL PURPOSE PROJECT

Fabot - "Facebook experience redefined"

To-do:
1. Messages
2. Notifications
3. Home page

'''
import Cookie
import cookielib
import mechanize
from getpass import getpass
from bs4 import BeautifulSoup
cookiejar =cookielib.LWPCookieJar()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print bcolors.OKBLUE+bcolors.BOLD+'\n\n\n\t\tFabot'+bcolors.ENDC
print bcolors.WARNING+'Press Enter to continue ...'+bcolors.ENDC,
check = raw_input()
br = mechanize.Browser()
br.set_cookiejar(cookiejar)

# Robots is false
br.set_handle_robots(False)

br.open('https://m.facebook.com/')
br._factory.is_html = True
br.select_form(nr = 0)
print bcolors.BOLD + "Email:" + bcolors.ENDC,
email = raw_input()
br['email'] = email
passw = getpass()
br['pass'] = passw
print bcolors.OKBLUE+'\nSubmitting login credentials'+ bcolors.ENDC
br.submit()
soup = BeautifulSoup(br.response().read())

if 'login_try_number=' in str(soup):
    print bcolors.FAIL+'Failed'+bcolors.ENDC
else:
    print bcolors.OKGREEN+'Successfully Logged in'+bcolors.ENDC
'''
l = soup.find_all("h3",{"class": "_52je _52jg _5tg_"})
for i in l:
    if 'user' in i.find_all('a')[0].text:
        print i.find_all('a')[0]['href']
        ur = str(i.find_all('a')[0]['href'])

print 'Going there --->'
br.open('https://m.facebook.com'+ur)
br._factory.is_html = True
#soup = BeautifulSoup(br.response().read())
br.select_form(nr = 1)
br['body'] = 'Sended through mechanize bot'
br.submit()

'''