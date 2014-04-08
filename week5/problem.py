import requests
import json
from local_config import GITHUB_USERNAME,GITHUB_PASS

def main():
    r = requests.get('https://api.github.com/users/mimipaskova', auth=(GITHUB_USERNAME, GITHUB_PASS))
    r.status_code
    json_format=r.json()
    print(json_format['following'])

if __name__ == '__main__':
    main()
