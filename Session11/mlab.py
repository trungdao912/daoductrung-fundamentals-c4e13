import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds155461.mlab.com:55461/muadongkhonglanh-c4e19
# mongodb://admin:admin@ds021182.mlab.com:21182/c4e
host = "ds155461.mlab.com"
port = 55461
db_name = "muadongkhonglanh-c4e19"
user_name = "trungdao912"
password = "english1996"

# host = "ds021182.mlab.com"
# port = 21182
# db_name = "c4e"
# user_name = "admin"
# password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())