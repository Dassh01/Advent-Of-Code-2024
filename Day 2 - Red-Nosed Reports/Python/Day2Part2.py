from grand_grabber import get_list,festivefy_text

link = "https://adventofcode.com/2024/day/2/input"

def is_safe_report(report):
    levels = list(map(int, report.split()))
    increasing = True
    for i in range(len(levels) - 1):
        if not (1 <= levels[i+1] - levels[i] <= 3):
            increasing = False
            break
    decreasing = True
    for i in range(len(levels) - 1):
        if not (1 <= levels[i] - levels[i+1] <= 3):
            decreasing = False
            break
    
    return increasing or decreasing

def can_be_safe_by_removing_one(levels):
    for i in range(len(levels)):
        #Splice just one element out
        new_levels = levels[:i] + levels[i+1:]
        if is_safe_report(" ".join(map(str, new_levels))):
            return True
    return False

def count_safe_reports(reports):
    amount_of_safe_reports = 0
    
    for report in reports:
        levels = list(map(int, report.split()))
        if is_safe_report(report) or can_be_safe_by_removing_one(levels):
            amount_of_safe_reports += 1
    
    return amount_of_safe_reports

def main():
    all_reports = get_list(link)
    safe_reports = count_safe_reports(all_reports)
    print("\nCorrected Safe Reports: "+festivefy_text(safe_reports))

if __name__ == "__main__":
    main()