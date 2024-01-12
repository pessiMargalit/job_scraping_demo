import subprocess
import sys
from Scrapers.ScrapersFactory import ScrapersFactory


def get_scrapers_from_branch(branch_name):
    # Fetch and checkout the specified branch
    subprocess.run(["git", "fetch", "origin", branch_name], check=True)
    subprocess.run(["git", "checkout", branch_name], check=True)
    subprocess.run(["git", "reset", "--hard", f"origin/{branch_name}"], check=True)

    # Instantiate the factory and get scraper names
    factory = ScrapersFactory()
    return set(factory.get_scrapers_names())


def main():
    main_branch = "main"

    # Fetch the PR branch name from GitHub Actions environment variable
    # This variable is set to the name of the branch for the pull request
    pr_branch = os.getenv('GITHUB_HEAD_REF', '')

    # Check if we are on a PR branch
    if pr_branch:
        # Get scrapers from the PR branch
        scrapers_pr = get_scrapers_from_branch(pr_branch)
    else:
        # If not on a PR branch, use the current branch
        factory = ScrapersFactory()
        scrapers_pr = set(factory.get_scrapers_names())

    # Get scrapers from the main branch
    scrapers_main = get_scrapers_from_branch(main_branch)

    # Find new scrapers
    new_scrapers = scrapers_pr - scrapers_main
    print(",".join(new_scrapers))


if __name__ == "__main__":
    main()
