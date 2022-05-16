# curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
# Use an official Ubuntu as a parent image
FROM ubuntu:20.04

# set the working directory to /cutlet
WORKDIR /bunkai

# install dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
        git \
        python3 \
        python3-pip \
        curl && \
    apt-get clean && pip3 install atheris

# Install dependencies
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 - 

# copy bunkai code to the docker image
COPY . /bunkai

# Use poetry to install the project and pip to install the wheel
RUN ~/.poetry/bin/poetry build && pip3 install dist/*.whl

# Allow the fuzzer to be able to execute
RUN chmod +x fuzz/fuzz.py