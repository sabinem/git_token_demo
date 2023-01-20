import requests
from dotenv import load_dotenv
import pdb
import os

load_dotenv()


#i'm providing username and API-Token in headers like
url = 'https://api.github.com/repos/octocat/Spoon-Knife/issues'
headers = {'Authorization': 'token ' + os.getenv('MY_TOKEN')}

login = requests.get('https://api.github.com/user', headers=headers)
print(login.json())

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
