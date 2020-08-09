from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from flask_cors import CORS
import urllib
import re

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
  return ("welcome")
@app.route('/tp', methods=['GET','OPTIONS'])
def get_file():
  num = int(request.args.get('num'))
  file = urllib.request.urlopen('http://terriblytinytales.com/test.txt')
  data = file.read()
  data1 = re.findall(r'\b[a-zA-Z@./_:\']*\b',data.decode())
  dict1 = dict()
  result = {}
  list1 = []
  for i in data1:
    if i!=' ' or i!='\n':
        i1 = i.lower()
        dict1[i1] = dict1.get(i1,0)+1
  keys = sorted(dict1, key=dict1.__getitem__)
  i = -2
  j = 1
  for n in range(num):
    x = keys[i]
    result = {'key':x,'value':dict1[x],'no': j}
    list1.append(result)
    i = i - 1
    j = j + 1
  
  return jsonify(list1)
  

if __name__ == '__main__':
   app.run(host='0.0.0.0')
