
from locust import HttpUser, TaskSet, task, between

class CardListTaskSet(TaskSet):

    headers = {
        "Content-Type": "application/json",
        "Token": "Replace_Your_Token",
        "Language": "EN"
    }
    
    payload = {
        "customerId": "2042429",
        "accountNumber": "47890737",
        "status": "All"
    }
    
    @task
    def post_card_list(self):
        response = self.client.post("/cms/v1/cardList", json=self.payload, headers=self.headers)
        print(f"Status Code: {response.status_code}, Response: {response.text}")

class WebsiteUser(HttpUser):
    tasks = [CardListTaskSet]
    wait_time = between(1, 3)  # Simulate user wait time between 1 and 3 seconds
    host = "Replace_Your_URL"

if __name__ == "__main__":
    import os
    os.system("locust -f load_test_api.py")


#  locust -f load_test_api.py  ( command for run project)