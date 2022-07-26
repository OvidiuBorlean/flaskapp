import time
import os
from flask import Flask
from flask import jsonify
from flask import request
import subprocess as sp

app = Flask(__name__)

hostName = sp.getoutput("hostname")

@app.route('/healthz')
def healthx():
  return "<h1><center>Healthz check completed</center><h1>"

@app.route('/ip')
def ip():
  ip_addr = request.remote_addr
  return ip_addr

@app.route("/")
def hello():
  ip_addr = request.remote_addr
  return str(hostName) + " " + ip_addr

if __name__ == "__main__":

  app.run(host='0.0.0.0',port=5000)
