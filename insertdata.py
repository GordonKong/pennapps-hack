import json, pymongo, sys
  
# Opening JSON file 
f = open(sys.argv[1]) 
  
# returns JSON object as  
# a dictionary

data = json.load(f) 

client = pymongo.MongoClient('mongodb+srv://pennapps:.@cluster0.cpkso.mongodb.net/pennapps?retryWrites=true&w=majority')
db = client.pennapps
collection = db.cat

def parse_amazondata(data):
    for i in data["image"]:
        if 'amount' in i:
            amountlist = i["amount"]
            value = ""
            for j in amountlist:
                value += j["name"]
            _data = {}
            _data["store"] = "amazon"
            _data["item"] = "sanitizers"
            _data["image"] = i["image"]
            _data["url"] = i["url"]
            _data["label"] = i["label"]
            try:
                _data["value"] = float(value.replace("$", ""))
            except:
                _data["value"] = 0
            post_id = collection.insert_one(_data).inserted_id
            post_id
            
def parse_walmartdata(data):
    for i in data["image"]:
        if 'amount' in i:
            amountlist = i["amount"]
            value = ""
            for j in amountlist:
                value += j["name"]
            _data = {}
            _data["store"] = "walmart"
            _data["item"] = "sanitizers"
            _data["image"] = i["image"]
            _data["url"] = i["url"]
            _data["label"] = i["label"]
            try:
                _data["value"] = float(value.replace("$", ""))
            except:
                _data["value"] = 0
            post_id = collection.insert_one(_data).inserted_id
            post_id
            
def parse_ebaydata(data):
    for i in data["image"]:
        _data = {}
        _data["store"] = "ebay"
        _data["item"] = "sanitizers"
        _data["image"] = i["image"]
        _data["url"] = i["url"]
        _data["label"] = i["label"]
        try:
            _data["value"] = float(i["amount"].replace("$", ""))
        except:
            _data["value"] = 0
        post_id = collection.insert_one(_data).inserted_id
        post_id
            
print(sys.argv)
if sys.argv[2] == "amazon":
    parse_amazondata(data)
if sys.argv[2] == "walmart":
    parse_walmartdata(data)
if sys.argv[2] == "ebay":
    parse_ebaydata(data)
    
#if sys.argv[2] = "walmart":    
    

