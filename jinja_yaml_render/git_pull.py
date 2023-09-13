import os
from git import Repo

def pull_git_repo(repo_url, local_directory):
    """
    Pull or clone a Git repository from a Stash (Bitbucket) server.

    Args:
        repo_url (str): The URL of the Git repository.
        local_directory (str): The local directory to clone or pull the repository into.

    Returns:
        bool: True if the operation was successful, False otherwise.
    """
    try:
        # Check if the local directory already exists
        if os.path.exists(local_directory):
            repo = Repo(local_directory)
            origin = repo.remote(name='origin')
            origin.pull()
            print(f"Repository in '{local_directory}' successfully pulled.")
        else:
            Repo.clone_from(repo_url, local_directory)
            print(f"Repository cloned into '{local_directory}'.")
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

# Example usage:
if __name__ == "__main__":
    repository_url = "https://github.com/sachin0987/CLI2Structured.git"
    local_directory = "/home/sachin/test"

    if pull_git_repo(repository_url, local_directory):
        print("Operation completed successfully.")
    else:
        print("Operation failed.")
