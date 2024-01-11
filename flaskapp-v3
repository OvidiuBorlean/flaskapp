import time
import os
import logging
from flask import Flask, jsonify, request
import subprocess as sp

app = Flask(__name__)

hostName = sp.getoutput("hostname")

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

customEndpoint = os.environ.get('FLASK_CUSTOM_ENDPOINT', "/custom")


@app.route(customEndpoint)
def custom():
   return "Custom endpoint succeeded\n"

@app.route('/header')
def header():
    all_hdr = request.headers
    return str(all_hdr)

@app.route('/delay')
def delay():
    sleepTime = 5
    time.sleep(int(sleepTime))
    user_agent = request.headers.get('User-Agent')
    url = request.url
    logging.info(f"{request.remote_addr} - - [{time.strftime('%d/%b/%Y %H:%M:%S')}] \"{request.method} {url} {request.environ.get('SERVER_PROTOCOL')}\" {user_agent}")
    return "Delayed for " + str(sleepTime) + " seconds" + "\n"

@app.route('/healthz')
def healthz():
    return "Health check completed\n"

@app.route("/")
def hello():
    user_agent = request.headers.get('User-Agent')
    url = request.url
    hdr = request.headers.get('Host')
    all_hdr = request.headers
    req_ip = request.remote_addr
    logging.info(f"{request.remote_addr} - - [{time.strftime('%d/%b/%Y %H:%M:%S')}] \"{request.method} {url} {request.environ.get('SERVER_PROTOCOL')}\" {user_agent}")
    return_values = str(all_hdr) + url + "\n" + req_ip + "\n" + hostName + "\n"
    return return_values



if __name__ == "__main__":
    listenerPort = os.environ.get('FLASK_LISTENER', "8080")
    print(listenerPort)
    app.run(host='0.0.0.0', port=int(listenerPort))
