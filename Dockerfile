FROM alpine:3.8
RUN mkdir /var/net
WORKDIR /var/net
COPY .  .
RUN apk update
RUN apk add python3
RUN apk add curl
RUN apk add tcptraceroute
RUN apk add tcpdump
RUN apk add openssh
RUN apk add busybox-extras
RUN apk add bash
RUN apk add bind-tools
RUN apk add iperf
RUN apk add mc
RUN pip3 install -r requirement.txt
EXPOSE 80
CMD ["python3","app.py"]
