from locust import HttpUser, TaskSet, task, between

class CardListTaskSet(TaskSet):

    headers = {
        "Content-Type": "application/json",
        # Uncomment and replace with actual values if required
        # "Token": "Replace_Your_Token",
        # "Language": "EN"
    }

    @task
    def get_all_books(self):
        response = self.client.get("/api/books", headers=self.headers)
        print(f"Status Code: {response.status_code}, Response: {response.text}")

class WebsiteUser(HttpUser):
    tasks = [CardListTaskSet]
    wait_time = between(1, 3)  # Simulate user wait time between 1 and 3 seconds
    host = "http://localhost:8080"  # Ensure this is the correct host and port

if __name__ == "__main__":
    import os
    os.system("locust -f load_test_api.py")
