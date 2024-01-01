#Project Details

#1. get the HN website front page (request package)
#2.Scrape required Content (title/link)
#3.Build Email Body/Content
#4.Email  Authenticaltion
#5.Email Sent 

# bs4 package used for webscrapping
# smtplib used for email authentication
# email.mime creating email body
# datatime used to manupulate date and time


import requests#helps to do API calls

from bs4 import BeautifulSoup#used for scrapping

import smtplib#Email server import

#Imports to help build our email
from email.mime.multipart import MIMEMultipart
from email.mime.text    import MIMEText

#Sys date and time
import datetime

now = datetime.datetime.now()

content = "" #This variable contains the content of our Email

def extract_new(url):
    print("Extracting the Hacker News Stories....\n")
    
    line_break= '<br>'
    cont=""
    cont +=('<b>HN Top Stories:<b>\n'+'<br>'+'-'*50+'<br>'+'\n')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    print (soup)
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        my_link =tag.find('a')
        link=""
        if my_link:
            link = my_link['href']
            cont += f"{i + 1} :: {tag.text} (Link: {link}){line_break}" if tag.text != 'More' else ''
        else:
            cont += f"{i + 1} :: {tag.text}{line_break}" if tag.text != 'More' else ''

    print(cont)
    return cont
cnt = extract_new('https://news.ycombinator.com/')
content += cnt
content += ('<br>-------<br>')
content += ('<br><br>End of Message')

#lets send the Email
print('Composing Email....')

#update your details
SERVER = 'smtp.gmail.com' #SMPT SERVER for GMAIL
PORT = 587
FROM = ''
TO = ''
PASS=''

#Message body
msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Automated Email]'+" "+str(now.day) + '-'+str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content,'html'))

print('Initializing the Server....')

server = smtplib.SMTP(SERVER,PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM,TO,msg.as_string())

print('Email Sent....')
