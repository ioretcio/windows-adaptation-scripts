import sys
import os
import datetime

def shorten_file_name(file_name, max_length=20):
    if len(file_name) <= max_length:
        return file_name
    else:
        name, extension = os.path.splitext(file_name)
        max_length -= len(extension)
        return name[:max_length//2] + "..." + name[-max_length//2:] + extension


def ls(directory):
    files = sorted(os.listdir(directory), key=lambda x: os.path.isdir(os.path.join(directory, x)), reverse=True)
    for file in files:
        file_path = os.path.join(directory, file)
        file_size = os.path.getsize(file_path)
        file_type = "Folder" if os.path.isdir(file_path) else "File"
        file_modified = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        file_name = shorten_file_name(file)
        
        if os.path.isdir(file_path):
            file_name = "\033[92m" + file_name + "\033[0m"
        else:
            file_name = "\033[0m" + file_name + "\033[0m"
        
        print(f"{file_name:<30} {file_size:>10} bytes   {file_type:<10} {file_modified:%Y-%m-%d %H:%M:%S}")




if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
        ls(directory)