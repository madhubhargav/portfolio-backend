# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /app

# Set the working directory to /app
WORKDIR /app

# Copy the required contents into the container at /app
ADD . /app/

# Install pipenv
RUN pip install pipenv

# Install requirements using pipenv
RUN pipenv install --dev --ignore-pipfile

# Set the working directory to /app/portfolio_backend
WORKDIR /app/portfolio_backend
