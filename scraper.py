# Amazon price drop alert via gmail


import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/BATA-Alfred-Formal-Shoes-7-8216103/dp/B07CDMXH8C/ref=sr_1_22?dchild=1&keywords=mens+formal+shoes&qid=1581518436&refinements=p_89%3ABATA&rnid=3837712031&sr=8-22'
headers ={
    "User-Agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')

    # print(soup.prettify())

    title= soup.find(id="productTitle").get_text()
    price= soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:5])

    if converted_price < 700:
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mymail','password')
    subject = 'Price fell down'
    body = 'Check amazone link https://www.amazon.in/BATA-Alfred-Formal-Shoes-7-8216103/dp/B07CDMXH8C/ref=sr_1_22?dchild=1&keywords=mens+formal+shoes&qid=1581518436&refinements=p_89%3ABATA&rnid=3837712031&sr=8-22'

    msg =f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'mymail',
        'sentto',
        msg
    )

    print("EMAIL HAS BEEN SENT!")

    server.quit()

check_price()