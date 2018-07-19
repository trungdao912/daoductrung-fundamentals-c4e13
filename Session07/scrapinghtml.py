from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import pyexcel

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
data = conn.read()
html_content = data.decode("utf-8")

# f = open("itunes.html", "wb")
# f.write(data)
# f.close()

soup = BeautifulSoup(html_content, "html.parser")
div = soup.find_all("div", "section-content")

li_list = div[1].find_all("li")

d = []

for list in li_list:
    h3 = list.h3
    x = h3.a
    h4 = list.h4
    y = h4.a
    title = x.string
    artist = y.string
    d.append({"title":title, "artist":artist})

pyexcel.save_as(records = d, dest_file_name = "file1.xls")