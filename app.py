import time
from flask import Flask
from flask import jsonify
from flask import request


print (host)
app = Flask(__name__)


@app.route('/healthz')
def healthx():
  return "<h1><center>Healthz check completed</center><h1>"

@app.route('/ip')
def ip():
  ip_addr = request.remote_addr
  return ip_addr

@app.route("/")
def hello():
  return "<h1><center>Flask App v1.0</center><h1>" + str(host)

if __name__ == "__main__":

  app.run(host='0.0.0.0',port=5000)
