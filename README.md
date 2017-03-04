Goals

Demonstrate proficiency in docker, python and web-services

Description

Need to write a Python REST-API service which returns the hourly price of an Amazon AWS instance given the parameters instance size and region. The service should be self-contained in a docker image and listen to port 8080. The latest pricing json-file should be freshly downloaded when the service startups up. The pricing information is linked below.

The submission should be committed to a publicly accessible github repository and should contain the following items:
- Dockerfile with which the service can be build and run
- README.md documentation using markdown
- python code including:
   - logging
   - unit tests
   - integration tests
   
Deployment

To deploy the project a Dockerfile is placed into the project in order to setup and automate the Deployment.

Installation

1. Download and install docker on local linux host, to install docker on ubuntu14.04 execute these following commands:
   - sudo apt-get update
   - sudo apt-get -y upgrade
   - sudo apt-get install linux-image-extra-`uname -r`
   - sudo apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
   - echo "deb https://apt.dockerproject.org/repo ubuntu-trusty main" | sudo tee /etc/apt/sources.list.d/docker.list
   - sudo apt-get update
   - sudo apt-get install docker-engine

2. Once Docker has been installed then we need to pull the Ubuntu14.04 image which we are going to use as our base image for this deployment. The command is:
   - sudo docker pull ubuntu:14.04

3. Now we containerize the application using Dockerfile, the execution command is as follows:
   - sudo docker build -t docker-python-api .

4. Now to run the container execute following command
   - sudo docker run -d -p 8080:8080 docker_python_api:latest python run.py

5. In this project we have also added unit and integration testing scope. "test_unit.py" is the file where unit testing test case has defined, in similar way "test_intgr.py" is the file where integration test scope has defined.

Usage:

Once the docker container has built and running it can be checked simply using GET:
   - curl http://127.0.0.1:8080/ 
    
      OK 
By default this API runs on port 8080

GET /v1/pricing:
 To check the price of an instance type (for example: m3.xlarge) for eu-west-1 region, this following command can be executed:
   - curl http://127.0.0.1:8080/v1/pricing?instance_type=m3.xlarge\&region=eu-west-1
    
     0.495

POST /v1/pricing:
   - curl -H "Content-Type: application/json" -X POST -d '{"instance_type":"m3.xlarge","region":"eu-west-1"}' http://127.0.0.1:8080/v1/pricing
     
     0.0495

To run unit testing:

1.First check the docker container list
   - sudo docker container ls

Output

CONTAINER ID        IMAGE                      COMMAND             CREATED             STATUS              PORTS                    NAMES
63fbbb611969        docker_python_api:latest   "python run.py"     About an hour ago   Up About an hour    0.0.0.0:8080->8080/tcp   amazing_bartik

2. Now using the container ID this following command will run unit testing

   - sudo docker exec -it 63fbbb611969 sudo python test_unit.py 

      Output
     
      .
      ----------------------------------------------------------------------
      Ran 1 test in 0.000s

      OK

3. using the same container ID this command will execute Integration testing:
    - sudo docker exec -it 63fbbb611969 sudo python test_intgr.py

     Output
     
----------------------------------------------------------------------


    OK
    sudo docker exec -it 63fbbb611969 sudo python test_intgr.py
    2017-03-04 07:50:20,501 ec2_costing  DEBUG    Handling request
    2017-03-04 07:50:20,501 ec2_costing  ERROR    Not found
    2017-03-04 07:50:20,502 ec2_costing  DEBUG    Finished handling request
    2017-03-04 07:50:20,507 ec2_costing  DEBUG    Handling request 
    2017-03-04 07:50:20,508 ec2_costing  DEBUG    Returned price: 0.450
    2017-03-04 07:50:20,508 ec2_costing  DEBUG    Finished handling request
    2017-03-04 07:50:20,510 ec2_costing  DEBUG    Handling request
    2017-03-04 07:50:20,510 ec2_costing  ERROR    Method not allowed
    2017-03-04 07:50:20,510 ec2_costing  DEBUG    Finished handling request
    2017-03-04 07:50:20,511 ec2_costing  DEBUG    Handling request
    2017-03-04 07:50:20,512 ec2_costing  ERROR    InstanceType r3.xlarge does not exist in region eu-west-1
    2017-03-04 07:50:20,512 ec2_costing  DEBUG    Finished handling request
    2017-03-04 07:50:20,513 ec2_costing  DEBUG    Handling request
    2017-03-04 07:50:20,514 ec2_costing  DEBUG    Returned price: 0.900
    2017-03-04 07:50:20,514 ec2_costing  DEBUG    Finished handling request
    2017-03-04 07:50:20,515 ec2_costing  DEBUG    Handling request
    2017-03-04 07:50:20,515 ec2_costing  DEBUG    Returned price: 0.240
    2017-03-04 07:50:20,515 ec2_costing  DEBUG    Finished handling request
    .
----------------------------------------------------------------------
    Ran 6 tests in 0.021s

    OK
   
   
