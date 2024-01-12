import subprocess
import sys
from Scrapers.ScrapersFactory import ScrapersFactory


def get_scrapers_from_branch(branch_name):
    # Fetch the branch first
    subprocess.run(["git", "fetch", "origin", branch_name], check=True)
    # Checkout the specified branch
    subprocess.run(["git", "checkout", branch_name], check=True)
    # Reset to make sure the working directory matches the branch
    subprocess.run(["git", "reset", "--hard", f"origin/{branch_name}"], check=True)

    # Instantiate the factory and get scraper names
    factory = ScrapersFactory()
    return set(factory.get_scrapers_names())


def main():
    main_branch = "main"
    pr_branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True,
                               text=True).stdout.strip()

    # If we're already on the PR branch, no need to checkout again
    if pr_branch != "HEAD":
        # Get scrapers from the PR branch
        scrapers_pr = get_scrapers_from_branch(pr_branch)
    else:
        factory = ScrapersFactory()
        scrapers_pr = set(factory.get_scrapers_names())

    # Get scrapers from the main branch
    scrapers_main = get_scrapers_from_branch(main_branch)

    # Find new scrapers
    new_scrapers = scrapers_pr - scrapers_main
    print(",".join(new_scrapers))


if __name__ == "__main__":
    main()
