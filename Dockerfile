
# Based on Ubuntu 14.04
############################################################

#base image to Ubuntu
FROM ubuntu:14.04

# File Author / Maintainer
MAINTAINER Iplu Saha

# Source list update
RUN su -c "apt-get update"

#basic application install
RUN su -c "apt-get install -y git curl wget build-essential"

# python install
RUN su -c "apt-get install -y python-dev python-pip"

# Copy the application folder inside the container
RUN su -c "git clone https://github.com/iplusaha/docker_python_api.git /docker_python_api"

# Get pip to download and install requirements:
RUN su -c "pip install -qr /docker_python_api/requirements.txt"

# Expose ports
EXPOSE 8080

# Set the default directory where CMD will execute
WORKDIR /docker_python_api

RUN su -c "wget https://a0.awsstatic.com/pricing/1/deprecated/ec2/pricing-on-demand-instances.json"

RUN python setup.py install

CMD su -c "python run.py &"
