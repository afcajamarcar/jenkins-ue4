import sys
import requests
if __name__=="__main__":
    r = requests.post('WEB_HOOK_URL', json={'text': sys.argv[1]})
