
ckerfile to build Flask Application Containers
# Based on Ubuntu 14.04
############################################################

#base image to Ubuntu
FROM ubuntu:14.04

# File Author / Maintainer
MAINTAINER Iplu Saha

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y git curl wget build-essential

# Install Python and Basic Python Tools
RUN apt-get install -y python-dev python-pip

# Copy the application folder inside the container
RUN git clone https://github.com/iplusaha/docker_python.git /docker_python

# Get pip to download and install requirements:
RUN pip install -r /docker_python/requirements.txt

# Expose ports
EXPOSE 8080

# Set the default directory where CMD will execute
WORKDIR /docker_python

RUN wget https://a0.awsstatic.com/pricing/1/deprecated/ec2/pricing-on-demand-instances.json

RUN python setup.py install

CMD python run.py
