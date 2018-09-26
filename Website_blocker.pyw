import time
from datetime import datetime as dt

hosts_path = r"C:\Users\Vishnu's World\Desktop\app3\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","www.flipkart.com","www.amazon.in"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9)>dt.now()>=dt(dt.now().year,dt.now().month,dt.now().day,3):
        print ("College...")
        with open(hosts_path,'r+')as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+""+website)
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in content for website in website_list):
                    file.write(line)
                file.truncate()
        print ("study...")
    time.sleep (5)
