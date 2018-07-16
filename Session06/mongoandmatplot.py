from pymongo import MongoClient
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

url = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(url)

db = client.get_default_database()

customers = db["customers"]

# new_post = {
#     "title":"TEST",
#     "author":"Trung Dao",
#     "content":"""Râu tôm nấu với ruột bầu
#     Chồng chan vợ húp gật đầu khen ngon
#     Chỉ tội cho cái thằng con
#     Đứng ngoài chầu chực biết ngon là gì.


#     Má ơi đừng gả con xa
#     Chim kêu vượn hú biết nhà má đâu
#     Thôi má hãy gả nhà giàu
#     Có tiền chỉnh mặt, làm đầu cho con.


#     Sáng chia tay anh, lòng em buồn muốn chết
#     Chiều về đau khổ chẳng muốn ăn
#     Tối đến cô đơn em nằm nghĩ
#     Anh chàng hàng xóm cũng đẹp zai"""
# }
# posts.insert_one(new_post)

ads_number = db.customers.find({"ref":"ads"}).count()
events_number = db.customers.find({"ref":"events"}).count()
wom_number = db.customers.find({"ref":"wom"}).count()



labels = ["ads", "events", "wom"]
values = [ads_number, events_number, wom_number]
colors = ["red", "green", "blue"]

pyplot.pie(values, labels=labels, colors=colors, autopct='%1.1f%%')
pyplot.axis("equal")

pyplot.show()