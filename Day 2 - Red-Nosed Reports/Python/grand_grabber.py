import requests

cookies = {
        "_ga": "GA1.2.2044113419.1733035196",
        "_gid": "GA1.2.863456346.1733035196",
        "_ga_MHSNPJKWC7": "GS1.2.1733035196.1.1.1733035261.0.0.0"
    }

def get_raw_html(link,session):
    cookies["session"] = session

    response = requests.get(link, cookies=cookies)
    if response.status_code == 200:
        print("Response status code: " + str(response.status_code) + ". Successful Request.")
        return response.text,True
    else:
        print("\nResponse status: "+str(response.status_code))
        print("Invalid session key")
        return "err",False
    
def convert_to_lists(raw_html):
    lines = raw_html.split('\n')
    if len(lines) > 1:
        lines = lines[:-1]
    return lines

def get_list(link,session_key=""):
    if len(session_key) == 0:
        session_key = input("Enter session key: ")
    requested_list = convert_to_lists(get_raw_html(link,session_key))
    return requested_list

def get_all_text(link,session_key=""):
    if len(session_key) == 0:
        session_key = input("Enter session key: ")
    all_text,request_status = get_raw_html(link,session_key)
    return all_text,request_status

def festivefy_text(text):
    
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"
    
    festive_text = ""
    
    for i, char in enumerate(str(text)):
        if i % 2 == 0:
            festive_text += GREEN + char + RESET
        else:
            festive_text += RED + char + RESET
    
    return festive_text