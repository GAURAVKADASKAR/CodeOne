# executor/views.py
import requests
import time


JUDGE0_URL = "https://judge0-ce.p.rapidapi.com/submissions"
HEADERS = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": "a9e2f22759msh814bc202ab273dbp12fdfdjsn2ba3e1086960",
    "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
}

def CompileCode(source_code , language_id , input):
        source_code = source_code
        language_id = language_id
        stdin = input

        response = requests.post(
            JUDGE0_URL + "?base64_encoded=false&wait=false",
            headers=HEADERS,
            json={
                "source_code": source_code,
                "language_id": language_id,
                "stdin": stdin
            }
        )
        token = response.json().get("token")

        result = {}
        for _ in range(10):
            time.sleep(1)
            res = requests.get(
                JUDGE0_URL + f"/{token}?base64_encoded=false",
                headers=HEADERS
            )
            result = res.json()
            if result.get("status", {}).get("id") in [3, 6, 7, 11]:
                break

        return result