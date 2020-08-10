import requests
from lxml import etree
import re

def get_oid(url):
    head = {
        'user-agent':'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    html = requests.get(url, headers = head).text
    html = etree.HTML(html)
    script = html.xpath('//script/text()')
    script_str = ""
    for i in script:
        script_str += str(i)
    #print(script_str)
    text = str(script).replace(" ","")
    text = text.replace("\n","")
    #print(type(text))
    oid = re.search('.*baseUrl(.*)base_url.*', text)[1].split("/")[6]
    return oid
