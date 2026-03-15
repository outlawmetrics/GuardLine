import os
import subprocess
from src.orchestrator import Orchestrator
from src.reporter import Reporter
from src.config import load_config
from src.github_api import post_pr_comment

def get_changed_files():
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~1"],
            capture_output=True, text=True
        )
        files = [f.strip() for f in result.stdout.splitlines() if f.strip()]
        return files
    except Exception:
        return []

def main():
    config = load_config()

    changed_files = get_changed_files()

    if not changed_files:
        print("No changed files found.")
        return

    orchestrator = Orchestrator()
    reporter = Reporter()

    report = orchestrator.run(changed_files, config)
    output = reporter.generate(report)

    post_pr_comment(output)

if __name__ == "__main__":
    main()