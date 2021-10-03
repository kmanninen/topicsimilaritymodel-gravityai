import requests
import json
from urllib.parse import urljoin
class topicsimilaritymodel_gravityai:
    def __init__(self, URL):
        self.base_url = URL

    def addJob(self, docs):
        files = {
            'file': ('docs.json', json.dumps(docs), 'application/json')
        }
        return requests.post(
            urljoin(self.base_url, "/data/add-job"),
            files=files)
    
    def getStatus(self, id):
        return requests.get(urljoin(self.base_url, "/data/status/" + id))

    def getResult(self, id):
        return requests.get(urljoin(self.base_url, "/data/result/json/" + id))
    
    def deleteJob(self, id):
        return requests.delete(urljoin(self.base_url, "/data/delete/" + id))

    def health(self):
        return requests.get(urljoin(self.base_url, "/health"), headers={"content-type": "application/x-www-form-urlencoded"})