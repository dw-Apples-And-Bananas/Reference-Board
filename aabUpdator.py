import requests
from git import Repo
import os, shutil, sys



def check(git):
    with open("./info") as f:
        info = f.read()
        currVer = info.splitlines()[0]
    class response: text = info

    try:
        response = requests.get(f"https://raw.githubusercontent.com/dw-Apples-And-Bananas/{git}/main/info")
    except requests.exceptions.ConnectionError:
        print("Update Request Failed")

    line = response.text.splitlines()

    if currVer != line[0]:
        clone(git)



def clone(git):
    Repo.clone_from(f"https://github.com/dw-Apples-And-Bananas/{git}.git", "./temp")
    for item in os.listdir("./temp"):
        if not item.startswith("."):
            if os.path.exists(f"./{item}"):
                try:
                    os.remove(f"./{item}")
                except PermissionError:
                    shutil.rmtree(f"./{item}")
            shutil.move(f"./temp/{item}", "./")
    shutil.rmtree('./temp')
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
