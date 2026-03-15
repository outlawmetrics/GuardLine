import requests
import os

def post_pr_comment(report_text):
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    pr_number = os.environ.get("PR_NUMBER")

    if not all([token, repo, pr_number]):
        print("Missing GitHub environment variables. Skipping PR comment.")
        print(report_text)
        return

    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    body = {"body": report_text}

    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 201:
        print("Report posted to PR successfully.")
    else:
        print(f"Failed to post PR comment: {response.status_code}")
        print(report_text)