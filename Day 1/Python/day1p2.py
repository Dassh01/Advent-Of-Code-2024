import requests
import re
from dasshtag import dassh_tag
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

def contains(list1,list2):
    """
    Returns the amount of times comparator appears in list_local
    """
    similarity_score = 0
    for number in list1:
        amount_of_times_appeared = 0
        
        for other_number in list2:
            if number == other_number:
                amount_of_times_appeared += 1
        
        local_sim_score = number * amount_of_times_appeared
        similarity_score += local_sim_score
    
    return similarity_score

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
    
def main():
    print("Day One Part Two")
    print(festivefy_text(dassh_tag))
    raw_html = get_raw_html(input("Enter session key: "))
    list1, list2 = parse_html_to_lists(raw_html)
    similarity_score = str(contains(list2,list1))
    print("\nSimilarity Score = " + festivefy_text(similarity_score) + "\n")
    
    
if __name__ == "__main__":
    main()