from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
 
url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2018/1/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'

html_content = urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(html_content,"html.parser")
data = soup.find("table", id ="tableContent")

list_vnm = []
data_list = data.find_all('td','b_r_c')

for i in range(0,len(data_list),6):
    vnm = {}
    vnm["Quy 2 - 2017"] = data_list[i+1].string
    vnm["Quy 3 - 2017"] = data_list[i+2].string
    vnm["Quy 4 - 2017"] = data_list[i+3].string
    vnm["Quy 1 - 2018"] = data_list[i+4].string
    list_vnm.append(vnm)

pyexcel.save_as(records= list_vnm, dest_file_name= "vinamilk.xlsx")

