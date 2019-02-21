# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 10:07:50 2019

@author: loren
"""

from requests import get
import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):    
#attempt to GET content at url. If content-type is HTML/XML then return text. Else return None. 
    with requests.Session() as se:
        se.headers = {
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
                }
    try:
        with closing(se.get(url, stream=True)) as resp:
            if is_good_response(resp):
                print(resp.content)
                print(resp)
                return resp.content
            else:
                print('bad response', resp.content)
                return None
    except RequestException as e:
        log_error("Horseface - Error during requests to {0}:{1}".format(url, str(e)))
        return None
    
def is_good_response(resp):
#return True if response is HTML. Else False. 
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)

def log_error(e):
#log errors to see them. 
    print(e)
    
    

    
    
    