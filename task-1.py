import os
import shutil
import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description='Recursively copy and sort files by extension.')
    parser.add_argument('src', type=str, nargs='?', help='Source directory path', default="src")
    parser.add_argument('dist', type=str, nargs='?', default='dist', help='Destination directory path')
    return parser.parse_args()

def walkman(src, dist):
    # os.walk(src) - Як альтернатива, тоді можна і без рекурсії
    for item in os.listdir(src): 
        path_src = os.path.join(src, item)

        if os.path.isdir(path_src):
            walkman(path_src, dist)
        elif os.path.isfile(path_src):
            extension = Path(path_src).suffix[1:]
            
            if not extension:
                extension = "without_extension"

            dir_dist = os.path.join(dist, extension)

            if not os.path.exists(dir_dist):
                os.makedirs(dir_dist)

            path_dist = os.path.join(dir_dist, item)

            try:
                shutil.copy2(path_src, path_dist)
                print(f'Copied {path_src} to {path_dist}')
            except Exception as e:
                print(f'Failed to copy {path_src} to {path_dist}: {e}')

            print(item)

def main():
    args = parse_args()

    if not os.path.isdir(args.src):
        print(f"Source directory {args.src} does not exist.")
        return
    
    if not os.path.exists(args.dist):
        os.makedirs(args.dist)

    walkman(args.src, args.dist)

    print(f"Files copied and sorted by extension to {args.dist}")

if __name__ == "__main__":
    main()