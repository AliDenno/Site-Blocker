import time
from datetime import datetime as dt


hosts_temp=r"hosts\hosts" # Dummy Test File
hosts_path=r"C:\Windows\System32\drivers\etc\hosts" # Actual File
redirect="127.0.0.1" # Redirect IP
website_list=["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"]
    
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_temp, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            content=file.readlines()
            file.seek(0) # returns to the begining of the file so that we dont get any duplicates 
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() # remove everything after pointer 
        print("Fun hours...")
    time.sleep(5)