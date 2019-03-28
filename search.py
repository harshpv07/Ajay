import urllib.request
from urllib.parse import quote_plus
import json , requests

def getresult(searchname):
    url_request = "https://www.googleapis.com/customsearch/v1?key=AIzaSyCyJQX4ctD4M31j-RXGszyp-HpZzzykfxE&cx=013148004188954828251:hzqxefrcnfg&q="+searchname
    r = requests.get(url_request)
    j_objs = json.loads(r.text)
    link = []
    
    for i in range(5):
        data = {
            'title' : j_objs['items'][i]['title'],
            'link' : j_objs['items'][i]['link'], 
            'snippet' : j_objs['items'][i]['snippet']
        }
        link.append(data)
    return link