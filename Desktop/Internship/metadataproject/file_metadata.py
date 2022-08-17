import os
from PIL import Image
import time
import pandas as pd


while True:
    file_name = input("What is the file name:  ")
    image = Image.open(file_name)

    fs = os.path.getsize('/Users/ankithsherman/' + file_name)

    dom_sec = os.path.getmtime('/Users/ankithsherman/' + file_name)
    dom = time.ctime(dom_sec)

    doc_sec = os.stat('/Users/ankithsherman/' + file_name).st_birthtime
    doc = time.ctime(doc_sec)

    file_data = [fs, dom, doc]
    file_df = pd.DataFrame(file_data, columns = [file_name])
    print(file_df)