import requests
import pandas as pd
from bs4 import BeautifulSoup

r=requests.get('https://www.webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
#print(r)
soup=BeautifulSoup(r.text,"lxml")
name=soup.find_all("a",class_ = "title")
product_name=[]

for i in name:
    name=i.text
    product_name.append(name)
    #print(product_name)   
    
price=soup.find_all("h4",class_="price float-end card-title pull-right")
product_price=[]

for i in price:
    price=i.text
    product_price.append(price)
    #print(product_price)

desc=soup.find_all("p",class_="description card-text")

desc_list=[]
for i in desc:
    desc=i.text
    desc_list.append(desc)
#print(desc_list)  

rev=soup.find_all("p",class_="review-count float-end")

rev_list=[]
for i in rev:
    rev=i.text
    rev_list.append(rev)
    #print(rev_list)

df=pd.DataFrame({"product name":product_name,"price":product_price,"descript":desc_list,"review":rev_list})
df.to_csv("product_details.csv")