#!/bin/ksh

# Function to clone repository
clone_repo() {
    username=$USER

    # Clean the directory
    if [ -d "$directory" ]; then
        echo "Cleaning directory '$directory'..."
        for file in "$directory"/*; do
            if [ -e "$file" ]; then
                rm -rf "$file"
            fi
        done
    else
        echo "Directory '$directory' does not exist. Creating it..."
        mkdir -p "$directory"
    fi

    # Clone repository
    git clone "https://$username@$repo_url" "$directory"

    # Check if clone was successful
    if [ $? -eq 0 ]; then
        echo "Repository cloned successfully."
    else
        echo "Failed to clone repository. Exiting."
        exit 1
    fi
}

# Main script

# Check if Git is installed, if not, try loading it
if ! command -v git > /dev/null 2>&1; then
    echo "Git is not installed. Attempting to load Git module..."
    if module load msde/git; then
        echo "Git module loaded successfully."
    else
        echo "Failed to load Git module. Please install Git or load the module manually."
        exit 1
    fi
fi

# Assign Git repository URL and clone directory
repo_url="example.com/repo.git"
directory="/path/to/clone/directory"

clone_repo
