from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
data = conn.read()
html_content = data.decode("utf-8")

soup = BeautifulSoup(html_content, "html.parser")
list_all = soup.find_all("td", "b_r_c")

for i in list_all:
    print(i.string)
    