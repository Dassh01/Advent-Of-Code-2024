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

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe_report(report):
            safe_count += 1
    return safe_count

def main():
    all_reports = get_list(link)
    safe_reports = count_safe_reports(all_reports)
    print("\nSafe Reports: "+festivefy_text(safe_reports))

if __name__ == "__main__":
    main()