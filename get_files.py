import os

def list_files_in_paths(paths):
    all_files = []
    for path in paths:
        if os.path.isdir(path):
            files = [os.path.join(path, file) for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
            all_files.extend(files)
    return all_files

paths = ["/tmp/dump1", "/tmp/dump2"]
combined_files = list_files_in_paths(paths)
print(combined_files)
