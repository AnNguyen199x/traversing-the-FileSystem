"""
Print file in OS
"""

import os

def main():
    """
    main function
    """
    for root, directories, files in os.walk("/workspaces/traversing-the-FileSystem/"):
        # print(f"Root :{root}")
        # print(f"Directiries: {directories}")
        for _dicrectory in directories:
            absolute_path = os.path.join(root, _dicrectory)
            print(f"Dir path: {absolute_path}")

        #  print all files in ffolder
        # print(f"Files: {files}")

        # Return all file path in subfolder:
        # for _file in files:
        #     absolute_path = os.path.join(root, _file)
        #     print(f"File path: {absolute_path}")

if __name__ == "__main__":
    main()
