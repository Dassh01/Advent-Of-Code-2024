import re
from grand_grabber import get_all_text, festivefy_text

link = "https://adventofcode.com/2024/day/3/input"
data, request_success = get_all_text(link, "53616c7465645f5f4919cc06fa75d4e0ef835d5ce2540f919f002e5cdf45e7470168e61ea095ddf87376856f5453dcd5008fc8008c3637ebd36be0ee1b903b36")

if request_success:
    mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")

    total_sum = 0
    last_operation = None

    combined_pattern = re.compile(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)')
    matches = combined_pattern.finditer(data)
    print("Matches found:")
    for match in matches:
        print(match.group())

    print("Total sum:", total_sum)