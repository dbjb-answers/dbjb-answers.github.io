import json
for puzl in json.loads(open("dbjb_answers.json").read()):
    print("**"+puzl['name']+"**"+"  ")
    for atype,ans in puzl['answers'].items():
        if atype.startswith("num"): print(atype.split("num")[1]+" Digit Number Lock: "+ans+"  ")
        if atype.startswith("word"): print(atype.split("word")[1]+" Letter Word Lock: "+ans+"  ")
        if atype.startswith("note"): print(atype.split("note")[1]+" Note Musical Lock: "+ans+"  ")
        if atype == "col": print("Color Lock: "+ans+"  ")
        if atype == "date": print("Date Lock: "+ans+"  ")
        if atype == "time": print("Time Lock: "+ans+"  ")
        if atype == "dir": print("Directional Lock: "+ans+"  ")
        if atype == "usd": print("US Dollars Money Lock: "+ans+"  ")
        if atype == "2words" : print("2 Word Lock: "+ans+"  ")
    print("\r\n")
