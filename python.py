import requests, json
from threading import Thread

def check_on_solve(_id):
    url = 'https://poseidon.boroinc.com/api/solve/check'
    data={
            "solveId": str(_id)
        }
    headers={'x-api-key':'user_api_key_here'}

    r = requests.Session()
    content=r.post(url=url,json=data,headers=headers).json()
    return content

def wait_for_solve(_id):
    done = False
    solve = None
    while done != True:
        solve = check_on_solve(_id)
        done = solve['status'] != 'pending' and solve['status'] != 'started'
    
    print("Status: " + solve['status'])
    if solve['token']:
        print("Token: " + solve['token'])

def request_solve():
    url = 'https://poseidon.boroinc.com/api/solve/request'
    data={
            "site_key": "6LeWwRkUAAAAAOBsau7KpuC9AV-6J8mhw4AjC3Xz",
            "site_url": "https://www.supremenewyork.com/",
            "requester": "Developer Sample"
        }
    headers={'x-api-key':'user_api_key_here'}

    r = requests.Session()
    content=r.post(url=url,json=data,headers=headers).json()
    return content['id']

def main():
    wait_for_solve(request_solve())

if __name__=='__main__':
    main()
