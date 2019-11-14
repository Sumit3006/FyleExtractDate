import requests
import os

for filename in os.listdir('Test_Photos'):
    resp = requests.post("http://localhost:5000/predict",
                        files={"file": open('Test_Photos' + '/' + filename,'rb')})