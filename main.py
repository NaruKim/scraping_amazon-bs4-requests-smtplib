#Thanks_to_Ajinkya Sonawane = https://medium.com/analytics-vidhya/python-script-to-track-amazon-prices-4b2610da5f49

import requests
import smtplib
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Acer-Display-Graphics-Keyboard-A515-43-R19L/dp/B07RF1XD36/ref=lp_16225007011_1_8"
from_email = ""
from_password = ""
to_email = ""

def check_price(URL, threshold_amt):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54"}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle") # .get_text().strip() #None만 나와서 get_text()가 안된다.
    price = soup.find(id="priceblock_ourprice") # .get_text()[1:].strip().replace(',','') #None만 나와서 get_text()가 안된다.

    Fprice = float(price)

    if Fprice < threshold_amt:
        alert_mail(URL, title, price)

def alert_mail(URL, title, price):
    server = smtplib.SMTP('smtp.gmail.com', 587) #587 == port=587
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('from_email', 'from_password')

    subject = price + "for" + title
    body = 'Link: ' + URL
    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail('from_email', 'to_email', msg)
    print('Email sent')

    server.quit()