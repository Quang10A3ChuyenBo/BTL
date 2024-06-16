import requests
import datetime
import csv
from github import Github

access_token = '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'
g = Github(access_token)
repo = g.get_repo('opencv/opencv')
commits = repo.get_commits(since=datetime.datetime(2023, 1, 1), until=datetime.datetime(2023, 12, 31))
# Create csv
csv_file = 'commits.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([ 'Author', 'Commited Date', 'Contributor','Files','Passed'])
    for commit in commits:
        combined_status = repo.get_commit(commit.sha).get_combined_status()
        # Get specified data
        author = commit.commit.author.name
        contributor = commit.author.login if commit.author else commit.commit.author.name
        commited_date = commit.commit.author.date.strftime("%Y-%m-%d")
        files = [file.filename for file in commit.files]
        passed = 'Success' if all(status.state == 'success' for status in combined_status.statuses) else 'Fail'

        # Write to csv_file
        writer.writerow([ author, commited_date, contributor, files, passed])