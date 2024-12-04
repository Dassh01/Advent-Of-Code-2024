import re
from grand_grabber import get_all_text,festivefy_text
def main():
    link = "https://adventofcode.com/2024/day/3/input"
    data,request_success = get_all_text(link,"53616c7465645f5f4919cc06fa75d4e0ef835d5ce2540f919f002e5cdf45e7470168e61ea095ddf87376856f5453dcd5008fc8008c3637ebd36be0ee1b903b36")
    if request_success:
        pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
        matches = pattern.findall(data)
        total_sum = 0
        for x, y in matches:
            total_sum += int(x) * int(y)
        print("\nTotal of all operations = "+festivefy_text(total_sum)+"\n")
if __name__ == "__main__":
    main()