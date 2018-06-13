#1. Download web page

#1.1 Create a connection
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import pyexcel

url = "http://dantri.com.vn/"
# conn = urlopen(url)

#1.2 Read data
# data = conn.read()
# print(data)

#1.3 Decocde
html_content = urlopen(url).read().decode("utf-8")

#1.4 Save Html Content
# urlretrieve(url, "dantri.html")  #Cách dùng thư viện urlretrive
# f = open('dantri.html','w')
# f.write(html_content)
# f.close


#2. Extract ROI(Region of Interest)
soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())     soup.find_all("a", attrs={"class": "sister"})
ul = soup.find("ul","ul1 ulnew")
li_list = ul.find_all("li")

list_of_dict = []

for li in li_list:
    # print(li.prettify())
    # print("* " * 20)
    # h4 = li.find("h4")
    # a = h4.find("a")
    dict1 = {}
    a = li.h4.a
    dict1["Title"] = a.string
    dict1["Link"] = url + a["href"]
    list_of_dict.append(dict1)
    # print(a.string)
    # print("* "* 20)
    # print(url + a["href"])


#3. Extract info
pyexcel.save_as(records=list_of_dict, dest_file_name="dantri.xlsx")
    




