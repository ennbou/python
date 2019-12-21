import os
import shutil


ttf_path = "C:/Users/DJK/AppData/Local/Microsoft/Windows/Fonts/fonts-master"
path = "C:/Users/DJK/AppData/Local/Microsoft/Windows/Fonts/dd/"

for root, dirs, files in os.walk(ttf_path):
    for name in files:
        if name.endswith(".ttf"):
            print(os.path.join(root, name))
            shutil.copy2(os.path.join(root, name), path)

