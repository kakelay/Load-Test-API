Here's a `README.md` snippet that includes the steps to run the Locust test:

```markdown
# Locust Load Testing

This guide will help you run the load test for your API using Locust.

## Prerequisites

Ensure that you have **Locust** installed. If not, you can install it using `pip`.

### Install Locust

To install Locust, run the following command:

```powershell
python -m pip install locust
```

## Running the Test

Once Locust is installed, follow these steps to run your test:

1. **Navigate to your test directory** where `load_test_api.py` is located.

2. **Run Locust** with the following command:

```powershell
locust -f load_test_api.py
```

3. **Open the Locust Web Interface** by navigating to `http://localhost:8089` in your browser. 

This will allow you to configure the load test parameters and start the test.

## Notes

- Running Locust via `os.system` is unnecessary when executing the script manually.
- Make sure the script `load_test_api.py` is properly configured to simulate the load for your API.

Enjoy testing your API performance with Locust!
```

This `README.md` gives clear instructions on how to install and run the test using Locust manually. Let me know if you need further adjustments!