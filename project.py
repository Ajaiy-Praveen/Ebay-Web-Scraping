# Ajaiy Praveen (Section 2)

from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.error import URLError 
import time
import re


url ="https://www.ebay.com/sch/i.html?_nkw=amazon+gift+card&LH_Sold=1"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'lxml')

# Part A
local_path = "amazon_gift_card_01.html"

try:
     req = urllib.request.Request(url, None, headers)
     time.sleep(5)
     with urllib.request.urlopen(req) as response:
         html_content = response.read()
     with open(local_path,"wb") as fp:
         fp.write(html_content)
except URLError as e:
    print("Unable to download page: "+str(e.reason))


# Creating path names      
target_file_path =[]
for i in range(1,10):
    target_file_path.append("amazon_gift_card_0"+str(i)+".html")    
target_file_path.append("amazon_gift_card_10.html")

# Creating the URLs
urls = []
for j in range(1,11):
    urls.append("https://www.ebay.com/sch/i.html?_nkw=amazon+gift+card&LH_Sold=1&_pgn="+str(j))

# Part B

# downloading and writing the contents of the first 10 pages in a loop   
for i in range(0,10):
    try:
        req = urllib.request.Request(urls[i], None, headers)
        time.sleep(10)
        with urllib.request.urlopen(req) as response:
            html_content = response.read()
        with open(target_file_path[i],"wb") as fp:
            fp.write(html_content)
    except URLError as e:
        print("Unable to download page: "+str(e.reason))


#List of objects holding respective values of each element
price =[]
titles =[]
shipping =[]

# Part C & D
for j in range(0,10):
    try:
        # Reading the file and storing in a variable
        HTMLFileToBeOpened = open(target_file_path[j], "r",encoding="utf8")
        contents = HTMLFileToBeOpened.read()
        print("\n")
        print("Page Number:",j+1)
        print("\n")
        soup = BeautifulSoup(contents, 'lxml')

        #Selecting the until the common feature for the 3 elements
        t =soup.select("#srp-river-results > ul li > div > div.s-item__info.clearfix")

        for i in t:

          # Extracting and printing the title of the gift card
          print(i.select(" a > div > span")[0].text.replace('New Listing', ''))
          titles.append(i.select(" a > div > span")[0].text.replace('New Listing', ''))
          
          #Extracting and printing the price of the gift card
          price.append(i.select("div.s-item__details.clearfix > div:nth-child(1) > span ")[0].text)
          for k in i.select("div.s-item__details.clearfix > div:nth-child(1) > span "):
            print(k.text)
            
          #Extracting and printing the shippping price and assigning No Shipping if empty
          ship = "No Shipping" if i.find("span",attrs={"class":"s-item__logisticsCost"})==None else i.find("span",attrs={"class":"s-item__logisticsCost"}).text
          print(ship)
          shipping.append(ship)
            
          print("\n")
          print("------------------------------\n")

    except URLError as e:
        print("Unable to open page: "+str(e.reason))

print("------List of gift cards that sold above face value------\n")
# Counter variable
cnt = 0

# Part E
for i in range(0,len(price)):
    #Extracting the value from title
    value_amount = re.sub(r"(.*?)(\$)(\d+\.*[\d]*)(.*)",r"\3", titles[i]) if re.findall(r"(\$\d+\.*\d*)",titles[i]) else '0'
    #Extracting only the shipping amount
    shipping_amount = re.sub(r"(.*?)(\d+\.*\d*)(.*)",r"\2",shipping[i]) if re.findall(r"\d+\.*\d*", shipping [i]) else '0'
    #Extracting only the price
    price_amount = re.sub(r"(\$*)(\d+\.*[\d]*)(.*)",r"\2",price[i])
    v= float(value_amount)
    p= float(price_amount)
    s= float(shipping_amount)
    #Checking if value < price + shippping
    if(float(value_amount) < float(price_amount) + float(shipping_amount) and float(value_amount)>0):
        print("Gift Card Number:",i+1)
        print(titles[i])
        print("%(first).2f < %(second).2f + %(third).2f " % {"first": v, "second":p, "third":s})
        print("Sold above face value")
        cnt=cnt+1
        print("\n")
        print("---------------------------- \n")
    

# Part F
print("The number of Gift Cards which sell above the face value is:")
print(cnt)

per = (cnt/len(titles))*100
print("\n About", int(per), "percent  of the gift cards on EBay sell more than the face value. "+
"One interesting reason for this is primarily stolen credit cards. People can have both buyer and seller accounts.The buyer can make a "+
"fake transaction with the solen card, paying a little more than the actual amount. Now they can use this card without any worry of "
"getting caught as they have a legit Amazon card and can purchase online using it.")


######################################################################

# PART 2

print("\n\n\nPART 2 \n")
try:
            
    URL2 = "https://www.fctables.com/user/login/"

    #An open session carries the cookies and allows you to make post requests
    session_requests = requests.session()

    res = session_requests.post(URL2, 
                                    data = {"login_action": "1",
                                            "login_username": "test8635",
                                            "login_password": "pass8635",
                                            "user_remeber": "1",
                                            "submit": "1"},
                                    timeout = 15)

    cookies = session_requests.cookies.get_dict()

    URL3 ="https://www.fctables.com/tipster/my_bets/"

    time.sleep(5)
    page2 = session_requests.get(URL3,  
                                cookies=cookies)
            
    doc = BeautifulSoup(page2.content, 'lxml')

    #Printing the cookies
    print("\n\n Cookies :")
    print(cookies)
    
    #Checking if Wolfsburg text is present to see if logged in
    if (bool(doc.findAll(text = re.compile('Wolfsburg')))):
        print("\n Successfully logged in ( Wolfsburg Present)")
    else:
        print("\n Not logged in")

except Exception as ex:
        print('error: ' + str(ex))


###### END ######





