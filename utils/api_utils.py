import json
import requests
import urllib3

from base.utils import HOST


class ApiConnector:
    
    def __init__(self):
        self.base_url = HOST
    
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
    def get(self, endpoint, headers=None, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=headers, params=params, verify=False)
        return response

    def post(self, endpoint, data=None, json_file=None, headers=None, params=None):
        url = f"{self.base_url}/{endpoint}"
        if json_file is not None:
            with open(json_file, "r") as f:
                data = json.load(f)
        response = requests.post(url, headers=headers, json=data, params=params, verify=False)
        return response

    def put(self, endpoint, data=None, json_file=None, headers=None, params=None):
        url = f"{self.base_url}/{endpoint}"
        if json_file is not None:
            with open(json_file, "r") as f:
                data = json.load(f)
        response = requests.put(url, headers=headers, json=data, params=params, verify=False)
        return response

    def delete(self, endpoint, headers=None, params=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url, headers=headers, params=params, verify=False)
        return response
