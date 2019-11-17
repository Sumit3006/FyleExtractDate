import requests
import os
import time

cnt=0
for filename in os.listdir('Original_Photos'):
    resp = requests.post("http://127.0.0.1:5000/extract_date",
                        files={"file": open('Original_Photos' + '/' + filename,'rb')})
    time.sleep(1)
    print(filename+" : "+resp.text)
    if resp.text[-1:].isdigit():
        cnt+=1
ac=cnt/595
with open("Accuracy.txt", "w") as text_file:
        text_file.write("{0}".format(ac))
