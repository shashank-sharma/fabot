'''
IT IS JUST FOR EDUCATIONAL PURPOSE PROJECT

Fabot - "Facebook experience redefined"

#Wish list
1. One session and more than 1 login - Status: Not possible

To-do:
1. Messages
2. Notifications
3. Home page

'''
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    import Cookie
    import cookielib
    import mechanize
    import time
    import os
    from getpass import getpass
    from bs4 import BeautifulSoup
    print bcolors.OKGREEN+'Import: OK'+bcolors.ENDC
except:
    print bcolors.FAIL+'Import: FAILED'+bcolors.ENDC
time.sleep(1)

def fetchdata(data,soup):
    name = soup.find_all('div',{'title': data})
    if name == []:
        print bcolors.FAIL+data.upper()+': NOT FOUND'+bcolors.ENDC
    else:
        print bcolors.OKGREEN+data+': '+str(name[0].text[len(data):])+bcolors.ENDC
def searchUser():
    print bcolors.WARNING+'Enter USER id: '+bcolors.ENDC
    print bcolors.WARNING+'https://m.facebook.com/(this is user id)'+bcolors.ENDC
    url = raw_input()
    url = 'https://m.facebook.com/'+url+'/about'
    print bcolors.OKGREEN+'URL: '+url+bcolors.ENDC
    try:
        br.open(url)
        br._factory.is_html = True
        print bcolors.OKGREEN+'Opening user profile: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Opening user profile: FAILED'+bcolors.ENDC
    try:
        soup = BeautifulSoup(br.response().read())
        print bcolors.OKGREEN+'Getting data: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Getting data: FAILED'+bcolors.ENDC
    name = soup.find_all('title')
    print bcolors.OKGREEN+'\n\nNAME: '+str(name[0].text)+bcolors.ENDC
    fetchdata('Gender',soup)
    fetchdata('Languages',soup)
    fetchdata('Mobile',soup)
    fetchdata('Facebook',soup)
    fetchdata('Websites',soup)
    fetchdata('Email',soup)
    fetchdata('Current City',soup)
    fetchdata('Home Town',soup)
    fetchdata('Interested in',soup)
    fetchdata('Religious views',soup)
    fetchdata('Political Views',soup)
    fetchdata('Social links',soup)

    relationship = soup.find_all('div',{'id': 'relationship'})
    if relationship == []:
        print bcolors.FAIL+'Relationship: NOT FOUND'+bcolors.ENDC
    else:
        print bcolors.OKGREEN+'Relationship: '+str(relationship[0].text[len(relationship):])+bcolors.ENDC
    family = soup.find_all('div',{'id': 'family'})
    if family == []:
        print bcolors.FAIL+relationship+'Family: NOT FOUND'+bcolors.ENDC
    else:
        print bcolors.OKGREEN+'Family: '+str(family[0].text[len(data):])+bcolors.ENDC
    

def notifications():
    print bcolors.WARNING+'Getting notifications'+bcolors.ENDC
    url = 'https://m.facebook.com/notifications'
    print bcolors.OKGREEN+'URL: '+url+bcolors.ENDC
    try:
        br.open(url)
        br._factory.is_html = True
        print bcolors.OKGREEN+'Opening notification: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Opening notification: FAILED'+bcolors.ENDC
    try:
        soup = BeautifulSoup(br.response().read())
        print bcolors.OKGREEN+'Getting data: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Getting data: FAILED'+bcolors.ENDC
    a = soup.find_all('div',{'id': 'notifications_list'})
    b = a[0].find_all('div')
    #sno = 1
    for i in b:
        #if (sno%5)==0:
        #print bcolors.WARNING+'Press Enter to continue'+bcolors.ENDC
        print i.text
        #print str(sno)+' '+i.text
        #sno +=1

def loadMessenger(fid):
    url = 'https://m.facebook.com'+str(fid)
    print bcolors.OKGREEN+'URL: '+url+bcolors.ENDC
    try:
        br.open(url)
        br._factory.is_html = True
        print bcolors.OKGREEN+'Loading messages: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Loading messages: FAILED'+bcolors.ENDC
    soup = BeautifulSoup(br.response().read())
    a = soup.find_all('div',{'class': 'msg'})
    try:                                            # Test to fix bug #1
        b = a[0].find_all('span')
    except:
        a = soup.find_all('div',{'id': 'messageGroup'})
        b = a[0].find_all('span')
    print bcolors.WARNING+bcolors.BOLD+'Showing messages'+bcolors.ENDC
    print '\n\n'
    for i in b:
        print i.text
    print '\nEnter your text to send message'
    br.select_form(nr = 1)
    messageBody = raw_input('>>>')
    br['body'] = messageBody
    try:
        br.submit()
        print bcolors.OKGREEN+'Sending status: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Sending status: FAILED'+bcolors.ENDC

def messages():
    print bcolors.OKBLUE+'GETTING MESSAGES'+bcolors.ENDC
    url = 'https://m.facebook.com/messages'
    print bcolors.OKGREEN+'URL: '+url+bcolors.ENDC

    try:
        br.open(url)
        print bcolors.OKGREEN+'Opening messages: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Opening messages: FAILED'+bcolors.ENDC
    
    surl = []
    sname = []

    soup = BeautifulSoup(br.response().read())
    l = soup.find_all('a')
    for i in l:
        if '/messages/read/' in str(i['href']):
            print i.text
            surl.append(str(i['href']))
            sname.append(i.text)

    print 'To whom you want to send message: '
    search_name = raw_input('Name: ')
    flag = 0
    for i in xrange(len(surl)):
        if search_name in sname[i]:
            loadMessenger(surl[i])
            flag = 1
            break
    if flag == 0:
        print bcolors.FAIL+'You enterd wrong name'+bcolors.ENDC

def delete():
    print bcolors.FAIL+'Cookies: DELETED'+bcolors.ENDC
    os.remove('.cookies.txt')

'''

Main function starts here #------------------------------------------------------------------------->

'''
print bcolors.OKBLUE+bcolors.BOLD+'###################         ##################'+bcolors.ENDC
print bcolors.OKBLUE+bcolors.BOLD+'###################         ######           ####'+bcolors.ENDC
print bcolors.OKBLUE+bcolors.BOLD+'###################         ######             ###'+bcolors.ENDC
print bcolors.OKBLUE+bcolors.BOLD+'#######                     ######            ###'+bcolors.ENDC
print bcolors.OKBLUE+bcolors.BOLD+'#######                     ######           ###'+bcolors.ENDC
print bcolors.OKBLUE+bcolors.BOLD+'#############               ###################'+bcolors.ENDC
print bcolors.OKBLUE+bcolors.BOLD+'#############               ######            ####'+bcolors.ENDC
print bcolors.OKBLUE+bcolors.BOLD+'#######                     ######             ####'+bcolors.ENDC
print bcolors.OKBLUE+bcolors.BOLD+'#######                     ######            ##'+bcolors.ENDC
print bcolors.OKBLUE+bcolors.BOLD+'#######                     ##################'+bcolors.ENDC
print bcolors.OKBLUE+bcolors.BOLD+'\n\n\tFabot'+bcolors.ENDC

if os.path.isfile('./.cookies.txt'):
    print bcolors.OKGREEN+'Compiled: Successfully'+bcolors.ENDC
    time.sleep(1)
    print bcolors.OKGREEN+'Cookies: FOUND'+bcolors.ENDC
    time.sleep(1)
    try:
        br = mechanize.Browser()
        print bcolors.OKGREEN+'Mechanize Browser: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Browser Setting: FAILED'+bcolors.ENDC
    time.sleep(1)
    cookiejar =cookielib.LWPCookieJar()
    br.set_cookiejar(cookiejar)
    cookiejar.load('.cookies.txt', ignore_discard=True, ignore_expires=True)
    br.set_handle_robots(False)
    print bcolors.OKGREEN+'Robots settings: OK'+bcolors.ENDC
    print bcolors.OKGREEN+'\nStatus: ACCESS GRANTED'+bcolors.ENDC
    try:
        br.open('https://m.facebook.com/')
        print bcolors.OKGREEN+'Connection: OK'+bcolors.ENDC
    except:
        cou = 0
        print bcolors.FAIL+'Connection: Not Connected'+bcolors.ENDC
        while True:
            print bcolors.WARNING+'Trying again: '+str(cou+1)+'/3'+bcolors.ENDC
            try:
                br.open('https://m.facebook.com/')
                print bcolors.OKGREEN+'Connection: OK'+bcolors.ENDC
                break
            except:
                cou+=1
            if cou >= 3:
                print bcolors.FAIL+'Failed Quitting'+bcolors.ENDC
                failno = 1
                break
    soup = BeautifulSoup(br.response().read())
    coname = soup.find_all('a',{'class': '_5jlw _3t21'})
    for i in coname:
        print bcolors.OKGREEN+'User: '+str(i.text)+bcolors.ENDC
        break


else:
    cookiejar =cookielib.LWPCookieJar('.cookies.txt')
    print bcolors.OKGREEN+'Compiled: Successfully'+bcolors.ENDC
    print bcolors.OKGREEN+'Cookies.txt: NOT FOUND'+bcolors.ENDC
    time.sleep(1)
    try:
        br = mechanize.Browser()
        print bcolors.OKGREEN+'Mechanize Browser: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Browser Setting: FAILED'+bcolors.ENDC
        failno = 1
    time.sleep(1)
    try:
        br.set_cookiejar(cookiejar)
        print bcolors.OKGREEN+'Browser cookies: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Browser cookies: FAILED'+bcolors.ENDC
        failno = 1
    time.sleep(1)
    # Robots is false
    br.set_handle_robots(False)
    print bcolors.OKGREEN+'Robots settings: OK'+bcolors.ENDC
    failno = 0
    try:
        br.open('https://m.facebook.com/')
        print bcolors.OKGREEN+'Connection: OK'+bcolors.ENDC
    except:
        cou = 0
        print bcolors.FAIL+'Connection: Not Connected'+bcolors.ENDC
        while True:
            print bcolors.WARNING+'Trying again: '+str(cou+1)+'/3'+bcolors.ENDC
            try:
                br.open('https://m.facebook.com/')
                print bcolors.OKGREEN+'Connection: OK'+bcolors.ENDC
                break
            except:
                cou+=1
            if cou >= 3:
                print bcolors.FAIL+'Failed Quitting'+bcolors.ENDC
                failno = 1
                break
    if failno == 0:
        br._factory.is_html = True
        try:
            br.select_form(nr = 0)
            print bcolors.OKGREEN+'Form selected: OK'+bcolors.ENDC
        except:
            print bcolors.FAIL+'Form selected: FAILED'+bcolors.ENDC
        print bcolors.BOLD + "Email:" + bcolors.ENDC,
        email = raw_input()
        br['email'] = email
        passw = getpass()
        print bcolors.OKBLUE+'\nSubmitting:'+ bcolors.ENDC,
        br['pass'] = passw
        try:
            br.submit()
            print bcolors.OKGREEN+'OK'+bcolors.ENDC
        except:
            cou = 0
            print bcolors.FAIL+'FAILED'+bcolors.ENDC
            while True:
                print bcolors.WARNING+'Trying again: '+str(cou+1)+'/3'+bcolors.ENDC
                try:
                    br.submit()
                    print bcolors.OKGREEN+'OK'+bcolors.ENDC
                except:
                    cou += 1
                if cou>= 3:
                    print bcolors.FAIL+'Failed Quitting'+bcolors.ENDC
                    failno = 1
                    break

        cookiejar.save()
        soup = BeautifulSoup(br.response().read())

if 'login_try_number=' in str(soup):
    print bcolors.FAIL+'Log in: Failed'+bcolors.ENDC
else:
    print bcolors.OKGREEN+bcolors.BOLD+'Log in: Accepted'+bcolors.ENDC
    check = raw_input('Press Enter to continue')
    while True:
        print 'Features allowed: \n1. Messages\n2.Notifications\n\nEnter your choice',
        ge = raw_input()
        if ge == '1':
            messages()
        elif ge == '2':
            notifications()
        elif ge == 'quit':
            print 'Thanks for using'
            break
        elif ge == 'delete':
            delete()
        elif ge == '3':
            searchUser() 

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