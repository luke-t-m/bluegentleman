from logger import log, logtag

from pathlib import Path
import json
import shutil

def read_text(path):
    logtag("read")
    log(f"Reading text file: {path}")
    try:
        with open(path) as file:
            return file.read()
    except:
        log("Read failed!")
        return ""

def read_json(path):
    logtag("read")
    log(f"Reading json file: {path}")
    try:
        with open(path) as file:
            return json.load(file)
    except:
        log("Read failed!")
        return dict()

def write_json(path, data):
    logtag("write")
    log(f"Writing json file: {path}")
    try:
        with open(path, "w") as file:
            json.dump(data, file)
    except:
        log("Write failed!")

    

def make_backup(og_path, backup_limit):
    logtag("backup")
    log(f"Copying {og_path} to backup...")
    baka_path = Path(og_path + ".baka")
    for i in range(1, backup_limit):
        if not baka_path.exists():
            shutil.copy(og_path, baka_path)
            break
        baka_path = Path(og_path + f".baka{i}")
    else:
        log("Backup not made. Too many existing backups. Please raise limit or delete.")
        return
    log(f"Backup made at {baka_path}")