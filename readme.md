# Load Balancer Tests

Testing an exposed service through AKS Load Balancer in Azure Kubernetes Service with a simple Flask application that will return the IP address of the caller and the hostname of respondent Pod.Testing an exposed service through AKS Load Balancer in Azure Kubernetes Service with a simple Flask application that will return the IP address of the caller and the hostname of respondent Pod.

Will use an AKS managed cluster configured with Outbound type of Load Balancer. We can use both internal and external Load Balancers services. We create a standard Kubernetes deployment with multiple replicas and will expose on port 80

```
kubectl create deployment netest --image=<your-registry>/flaskapp --port=80 --replicas=3
kubectl expose deploy netest --type=LoadBalancer 
```

If we need to expose as an internal LB service, we will add the following annotations to respective service:

```
annotations:
    service.beta.kubernetes.io/azure-load-balancer-internal: "true"
```
We will use a Python Flask application to run our server. Python3 interpreter needs to be available together with Python3-pip package manager and flask framework. We can install with following commands:

```
apt update
apt install python3-pip -y
apt install flask
```
or use the following:

**Dockerfile**

```
FROM alpine:3.8
RUN mkdir /var/net
WORKDIR /var/net
COPY .  .
RUN apk update
RUN apk add python3
RUN pip3 install -r requirement.txt
EXPOSE 80
CMD ["python3","app.py"]
```

**requirements**

```
flask
```

**app.py**

```
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
```

When we are testing the service through the Load Balancer exposed IP address, we will have the following output:

```
curl  4.231.137.95
```

netest-6fbb84f676-nq7ph 10.224.0.4

We observe that we are getting an internal IP address of the requestor, this is because of the externalTrafficPolicyconfigured by default as Cluster. In this case, there is a SNAT operation that changes the IP address. If we want to preserve the IP address of requestor, we need to change to Local. After the configuration change, we can observe the traffic is seen at the Pod level with the Public IP address:

curl 4.231.137.95

netest-6fbb84f676-7nk9d 13.73.161.90

We have by default defined following route in our Python code, healthz and ip. We can define our custom endpoints with the @app.route() section of the code plus the function that fill handle that route. In the main function, we define the listener ip address, which in our case is representing all interfaces and the port where our application is listening (default=5000).

