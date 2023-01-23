import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://api.github.com/repos/octocat/Spoon-Knife/issues"
try:
    github_token = os.environ.get("GITHUB_TOKEN")
    assert github_token
    headers = {"Authorization": f"token {github_token}"}

    login = requests.get("https://api.github.com/user", headers=headers)
    assert login.json().get("login")
except AssertionError:
    headers = {}
    msg = (
        "Warning: the command will be run without github credentials.\n- This might "
        "cause the github rate limit to be exceeded.\n- To fix this please look in the "
        "readme on how to provide your github credentials"
    )
    print(msg)


def f_auth(count):
    res = requests.get(url, headers=headers)
    print(f"{res.status_code} for {count}")
    res.raise_for_status()


def f_no_auth(count):
    res = requests.get(url)
    print(f"{res.status_code} for {count}")
    res.raise_for_status()


def call_github_api(with_auth=True, call_limit=100):
    count = 0
    if with_auth:
        api_func = f_auth
    else:
        api_func = f_no_auth
    for i in range(call_limit):
        count += 1
        api_func(count)
