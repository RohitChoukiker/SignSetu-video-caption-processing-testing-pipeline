import requests
import time

class APIClient:
    def __init__(self, base_url, candidate_id):
        self.base_url = base_url
        self.headers = {
            "X-Candidate-ID": candidate_id
        }
        self.token = None

    def auth(self):
        for attempt in range(3):
            res = requests.post(f"{self.base_url}/api/auth", headers=self.headers)

         
            if res.status_code == 200:
                self.token = res.json().get("token")
                self.headers["Authorization"] = f"Bearer {self.token}"
                return res

           
            if res.status_code == 409:
              
                time.sleep(2)
                continue

           
           
            time.sleep(1)

       
        print(" Auth unstable returning last response")
        return res

    def post(self, endpoint, data=None):
        return requests.post(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=self.headers
        )

    def get(self, endpoint):
        return requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers
        )

    def delete(self, endpoint):
        return requests.delete(
            f"{self.base_url}{endpoint}",
            headers=self.headers
        )