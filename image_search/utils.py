from io import BytesIO
from fake_useragent import UserAgent

import os
import json
import requests

def json_parse(json_message=None):
    result = None
    try:        
        result = json.loads(json_message)
    except Exception as e:      
        # Find the offending character index:
        idx_to_replace = int(str(e).split(' ')[-1].replace(')', ''))      
        # Remove the offending character:
        json_message = list(json_message)
        json_message[idx_to_replace] = ' '
        new_message = ''.join(json_message)     
        return json_parse(json_message=new_message)
    return result

def filename_from_url(file_url: str):
    return str(file_url).split("/")[-1]

def download_file_from_url(src: str, dst: str):
    """
    Download file from remote url
    """
    if not (src or dst):
        raise Exception('src url and destination path is required!')
    
    basename = filename_from_url(src)
    
    with requests.get(src, stream=True) as response:
        dst_path = os.path.join(dst, basename)

        if not os.path.isdir(dst):
            raise Exception("Destination path does not exists")
        
        with open(dst_path, 'wb') as f:
            f.write(response.content)
            f.close()
            
    return True

def get_random_user_agent():
    return UserAgent(verify_ssl=False).random


