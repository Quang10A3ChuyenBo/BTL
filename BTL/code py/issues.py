import requests
import datetime
import csv
from github import Github


access_token = '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'
g = Github(access_token)
repo = g.get_repo('opencv/opencv')

def fetch_github_issues(repo, state, filename, include_author=False):
    issues_data = []

    # Lấy thông tin issues
    for issue in repo.get_issues(state=state):
        if len(issues_data) >= 5500:  
            break
        issues_data.append(issue)

    # Định danh tên cột
    if include_author:
        fieldnames = ["Name", "Type", "Version", "Date Appear", "Author", "Solve Date"]
    else:
        fieldnames = ["Name", "Type", "Version", "Date Appear"]

    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Ghi header
        writer.writeheader()

        # Ghi dữ liệu mỗi issue
        for issue in issues_data:
            row = {
                "Name": issue.title,
                "Type": issue.labels[0].name if issue.labels else 'Uncategorized',
                "Version": issue.milestone.title if issue.milestone else 'Not specified',
                "Date Appear": issue.created_at
            }
            if include_author:
                row["Author"] = issue.user.login if issue.user else 'Unknown'
                row["Solve Date"] = issue.closed_at if issue.closed_at else 'Unsolved'
            writer.writerow(row)

# URL cho issues chưa giải quyết
open_issues_url = 'https://api.github.com/repos/opencv/opencv/issues?state=open'
fetch_github_issues(repo, 'open', 'issuesOpen.csv')

# URL cho issues đã giải quyết
closed_issues_url = 'https://api.github.com/repos/opencv/opencv/issues?state=closed'
fetch_github_issues(repo, 'closed', 'issuesClose.csv', include_author=True)

print('Dữ liệu đã được xuất thành công')
