import requests
import re
from dasshtag import dassh_tag

GREEN = "\033[32m"
RESET = "\033[0m"

link = "https://adventofcode.com/2024/day/1/input"

def parse_html_to_lists(html_input):
    numbers = re.findall(r'\d+', html_input)
    numbers = list(map(int, numbers))
    list1 = numbers[::2]  
    list2 = numbers[1::2]
    return list1, list2

def get_raw_html(session):
    cookies = {
        "_ga": "GA1.2.2044113419.1733035196",
        "_gid": "GA1.2.863456346.1733035196",
        "session": session,
        "_ga_MHSNPJKWC7": "GS1.2.1733035196.1.1.1733035261.0.0.0"
    }
    response = requests.get(link, cookies=cookies)
    if response.status_code == 200:
        return response.text
    else:
        print("\nResponse status: "+str(response.status_code))
        print("Invalid session key")
        return "err"

def create_pairs(list1,list2):
    pairs_2d_array = []
    for i in range(len(list1)):
        min_from_list1 = min(list1)
        min_from_list2 = min(list2)
        list1.remove(min_from_list1)
        list2.remove(min_from_list2)
        pairs_2d_array.append([min_from_list1,min_from_list2])
        
    return pairs_2d_array    

def festivefy_text(text):
    
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"
    
    festive_text = ""
    
    for i, char in enumerate(text):
        if i % 2 == 0:
            festive_text += GREEN + char + RESET
        else:
            festive_text += RED + char + RESET
                
    return festive_text

def calculate_total_distance(pairs_array):
    total_distance = 0
    for pair in pairs_array:
        total_distance += abs(pair[0] - pair[1])
    return total_distance

def main():
    print("Day One Part One")
    print(festivefy_text(dassh_tag))
    raw_html = get_raw_html(input("Enter session key: "))
    list1, list2 = parse_html_to_lists(raw_html)
    pairs_array = create_pairs(list1,list2)
    print("Distance = " + festivefy_text(str(calculate_total_distance(pairs_array))))
    
if __name__ == "__main__":
    main()