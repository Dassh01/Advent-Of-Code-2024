import requests
import re

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
    return response.text

def create_pairs(list1,list2):
    pairs_2d_array = []
    for i in range(len(list1)):
        min_from_list1 = min(list1)
        min_from_list2 = min(list2)
        list1.remove(min_from_list1)
        list2.remove(min_from_list2)
        pairs_2d_array.append([min_from_list1,min_from_list2])
        
    return pairs_2d_array    

def calculate_total_distance(pairs_array):
    total_distance = 0
    for pair in pairs_array:
        total_distance += abs(pair[0] - pair[1])
    return total_distance

def main():
    raw_html = get_raw_html(input("Enter session key: "))
    list1, list2 = parse_html_to_lists(raw_html)
    pairs_array = create_pairs(list1,list2)
    print("Distance = "+ GREEN + str(calculate_total_distance(pairs_array)) + RESET)
    
if __name__ == "__main__":
    main()