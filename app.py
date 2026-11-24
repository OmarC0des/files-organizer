# -- This script is made by --
# --      Omar Ashraf       --
# ----------------------------
import os
import shutil

def get_dir():
    get_dir = True
    while get_dir:
        main_dir = input("Please, enter the directory to work on: ")
        if not os.path.exists(main_dir):
            print("Path doesn't exist.")
        else:
            os.chdir(main_dir)
            return main_dir

def main(path):
    print("Script made by: Omar Ashraf")
    formats = {
    "Audio": [
    "mp3",
    "wav",
    "ogg",
    "flac",
    "aiff",
    "m4a",
    "aac",
    "wma",
    "opus",
    ],
    "Videos":[
    'mp4',
    'mov',
    'mkv',
    'webm',
    'mpeg',
    'mpg'
    ],
    "Archives": [
    'rar',
    'zip',
    '7z',
    'tar',
    'gz',
    'iso',
    'tar.gz',
    ],
    "Documents":[
    'pdf',
    'docx',
    'doc',
    'txt',
    'md',
    'html',
    'rtf',
    'tex',
    'odt',
    'epub',
    'xlsx',
    'xls',
    'csv',
    'pptx',
    'ppt',
    'ods',
    'odp',
    ],
    "Apps":[
    'exe',
    'msi',
    'apk',
    'deb',
    'app',
    'jar',
    'AppImage',
    ],
    "Images":[
    'png',
    'jpeg',
    'jpg',
    'gif',
    'bmp',
    ],
    }
    new_formats = {}
    done = False
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))] # done
    for file in files:
        done = False
        for format in formats:
            if file.split('.')[-1] in formats[format]:
                try:
                    os.mkdir(f"{format}")
                    shutil.move(f"{file}",f"{format}")
                except:
                    shutil.move(f"{file}",f"{format}")
                done = True
        if done:
            continue
        new_format = input(f"{file}.{file.split('.')[-1]} file has unknown format,\nProvide the folder name for that format (e.g., Videos, Photos, other...): ")
        try:
            formats[new_format].append([file.split('.')[-1]])
            shutil.move(f"{file}",f"{new_format}") 
        except:
            formats[new_format] = [file.split('.')[-1]]
            os.mkdir(f"{new_format}")
            shutil.move(f"{file}",f"{new_format}")
main(get_dir())
