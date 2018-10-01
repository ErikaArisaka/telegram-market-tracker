from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError
MAX_PRICE = float(input("input max price"))
keyword = input("What?")
email = input("Your email?")


def sendmail(url, title, price):
    msg = MIMEMultipart()
    msg['from'] = "erikaarisaka@gmail.com"
    msg['to'] = email
    msg['Subject'] = "EbayTracking"

    body = "<a href=\"" + url + "\">" + title + "</a>" + "</p><p>Price " + price + "</p>"
    msg.attach(MIMEText(body, 'html'))
    print(msg)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['From'], "EbayEbay")
    server.sendmail(msg['From'], msg['to'], msg.as_string())
    server.quit()


searches = []


def ebay_finding():
    try:
        api = Finding(config_file='config.yaml')
        response = api.execute('findItemsAdvanced', {'keywords': keyword})
        results = response.dict()
        items = results['searchResult']['item']

        for item in items:
            url = item['viewItemURL']
            title = item['title']
            price1 = float(item["sellingStatus"]["convertedCurrentPrice"]["value"])
            price = item["sellingStatus"]["convertedCurrentPrice"]["value"]
            if (MAX_PRICE + MAX_PRICE * 0.05) >= price1 >= (MAX_PRICE - MAX_PRICE * 0.05):
                print("I found something")
                sendmail(url, title, price)
    except ConnectionError as e:
        print(e)
        print(e.response.dict())


while True:
            ebay_finding()
            time.sleep(600)
