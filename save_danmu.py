import json

def saveFile(data):
    with open('danmu.json', 'a', encoding='utf-8') as f:
        data = json.dumps(data, ensure_ascii=False) + ',\n'
        f.write(data)
    return "save OK"
def saveFile2(data):
    with open('danmu2.json', 'a', encoding='utf-8') as f:
        data = json.dumps(data, ensure_ascii=False) + ',\n'
        f.write(data)
    return "save OK"