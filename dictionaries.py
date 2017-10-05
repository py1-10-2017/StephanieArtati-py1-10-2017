
def build_dict(key,value,dict=None):
    if (dict is None):
        dict = {}
    dict[key] = value
    return dict

def read_dict(dict):
    for key,data in dict.items():
        print("My",key,"is",data)

dict = build_dict("Name","Stephanie Artati")
dict = build_dict("Country","USA", dict)
dict = build_dict("City","Redmond", dict)
dict = build_dict("Age", 35, dict)

read_dict(dict)
