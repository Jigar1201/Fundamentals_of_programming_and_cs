import os
import sys
import zipfile

def _exit():
    if sys.flags.interactive:
        try:
            exit()
            sys.exit()
        except:
            os._exit(0)
    else: sys.exit()

def add_to_zip(path, zipf, required=False):
    if not os.path.exists(path):
        if required:
            print('Fail: Unable to find file %s' % path)
            raise Exception
        return
    print('Adding: %s' % path)
    zipf.write(path)

def intro():
    print("""\
 _ _ ____    ____       _
/ / |___ \  |  _ \ _ __(_)_   _____ _ __
| | | __) | | | | | '__| \ \ / / _ \ '__|
| | |/ __/  | |_| | |  | |\ V /  __/ |
|_|_|_____| |____/|_|  |_| \_/ \___|_|
""")

def main():
    intro()
    zip_name = 'hw6.zip'
    zipf = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    required_files = ['hw6-tetris.py', 'hw6-targets.py']
    optional_files = []
    try:
        for file in required_files: add_to_zip(file, zipf, required=True)
        for file in optional_files: add_to_zip(file, zipf, required=False)
    except:
        zipf.close()
        os.remove(zip_name)
        _exit()
    zipf.close()
    print("Success!")

if __name__ == '__main__':
    main()
