#!/usr/bin/python3

from logger import log, logtag
from helpers_fs import read_json, read_text
from helpers_ftd import check_valid_bp

from pathlib import Path
import os

import tkinter
import tkinter.filedialog

# TODO: handle argv. silent, make backup, etc.


# get stats about crams (how many parts, what they are.)
# select target (all pellets, six connections, etc)
# called constraints. constrain replacing all to only some.
# as above, figure out connections. rotations....
# set ceiling on replacements
# choose what to replace with.
# make backup and do replacement.
# loop.


#TODO
#falsetether
#cramsurgeon
#matoverride
#turretmanager - name turrets as master and copy, then run command to copy master turrets onto copies. also remove copies to make building easier.


class BPHand():
    def __init__(self):
        #---------- Filepathing and Reading. ----------
        logtag("bphand")
        log("Setting path variables...")
        exec_path = Path(__file__).resolve()
        base_dir = exec_path.parent
        data_dir = base_dir/"data"
        config_dir = base_dir/"config"
        ftd_dir_mem = config_dir/"ftd_dir_path"

        log("Loading data files...")
        blocks_path = data_dir/"blocks.json"
        blocks = read_json(blocks_path)


        # Find FTD directory.
        log("Starting search for FTD directory...")
        log(f"Checking config file...")
        raw = read_text(ftd_dir_mem)
        ftd_dir = Path(raw)
        if "Constructables" in raw and Path(ftd_dir).exists():
            log(f"Shorting search. Recalled FTD dir: {ftd_dir}")
        else:
            want = Path("From The Depths")/"Player Profiles"/"*"/"Constructables"
            rglob = list(Path.home().rglob(str(want)))
            if len(rglob) == 0:
                ftd_dir = Path.home()
                log(f"Couldn't find FTD dir. Please set at {ftd_dir_mem}")
            else:
                ftd_dir = rglob[0]
                log(f"Found FTD dir: {ftd_dir}")
                log("Saving path to config for future use...")
                with open(ftd_dir_mem, "w") as file:
                    file.write(str(ftd_dir))

        # Ask user to select blueprint.
        os.chdir(ftd_dir)
        tkinter.Tk().withdraw() # rootless.
        while True:
            log("Launching file selection dialogue...")
            bp_path = tkinter.filedialog.askopenfilename()
            if len(bp_path) == 0:
                log("No file selected. Exiting...")
                exit()
            bp = read_json(bp_path)
            if check_valid_bp(bp):
                break
        os.chdir(base_dir)
        print("win!")

if __name__ == "__main__":
    BPHand()
