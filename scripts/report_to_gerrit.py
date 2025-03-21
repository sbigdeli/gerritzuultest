import requests

GERRIT_URL = "https://your-gerrit-server.com" ## ÄNDRA TILL GERRIT !!!!!
CHANGE_ID = "your-change-id"
STATUS = "SUCCESS"  # eller "FAIL" beroende på resultat

def report_to_gerrit(change_id, status):
    url = f"{GERRIT_URL}/a/changes/{change_id}/checks"
    data = {
        "check": {
            "name": "Test - Hello World",
            "status": status,
            "url": "https://your-ci-system.com/job/test-hello-world/1/" ##ÄNDRA TILL ZUUL !!!!!!!
        }
    }
    headers = {
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=data, headers=headers, auth=("username", "password"))
    if response.status_code == 200:
        print("Reported status to Gerrit successfully")
    else:
        print(f"Failed to report status to Gerrit: {response.status_code}")

# Kör detta skript efter att testerna har kört
report_to_gerrit(CHANGE_ID, STATUS)
