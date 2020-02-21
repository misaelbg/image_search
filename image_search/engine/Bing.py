from bs4 import BeautifulSoup
import urllib.parse as urlparse
from fake_useragent import UserAgent
from .utils import json_parse, get_random_user_agent

import lxml.html
import requests
import json

class Bing:
    """ Bing Engine Soup """
    def __init__(self):
        self.bing_url = "https://www.bing.com/images/async"
    
    def set_request_headers(self):
        return {"User-Agent": get_random_user_agent()}
    
    def set_payload(self, q: str, first: int, adlt: str):
        return (("q", str(q)), ("first", first), ("adlt", adlt))
    
    def get_image_link(self, page_content):
        page_content = page_content.get("m").replace('\r\n', "")
        page_content = json_parse(page_content)
        return page_content.get('murl')
        
    def search_images(self, query: str, delta: int, adult_content: bool=False):
        image_links = []
        adult_content = "on" if adult_content else "off"
        search_delta = 0
        page_counter = 0
        
        while search_delta < delta:
            # Parse the page source
            payload = self.set_payload(query, page_counter, adult_content)
            headers = self.set_request_headers()
            
            with requests.get(self.bing_url, params=payload, headers=headers) as response:
                page_content = str(response.content).replace('\r\n', "")
                soup = BeautifulSoup(page_content, "html.parser")
        
                for i in soup.find_all("a", class_="iusc"):
                    if search_delta >= delta:
                        break
                    
                    image_links.append(self.get_image_link(i))

                    search_delta+=1
                    
                page_counter += 1
                
        return image_links
            