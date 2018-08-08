import mongoengine

host = "ds155461.mlab.com"
port = 55461
db_name = "muadongkhonglanh-c4e19"
user_name = "trungdao912"
password = "english1996"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())