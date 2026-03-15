import os
import subprocess
from src.orchestrator import Orchestrator
from src.reporter import Reporter
from src.config import load_config
from src.github_api import post_pr_comment

def get_changed_files():
    scan_target = os.environ.get("SCAN_TARGET", ".")

    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~1"],
            capture_output=True, text=True, cwd=scan_target
        )
        files = []
        for f in result.stdout.splitlines():
            f = f.strip()
            if f:
                files.append(os.path.join(scan_target, f))
        return files
    except Exception:
        return []

def main():
    scan_target = os.environ.get("SCAN_TARGET", ".")
    config = load_config(scan_target)

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