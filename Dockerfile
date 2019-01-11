# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /wwq
WORKDIR /wwq

# Copy the current directory contents into the container at /wwq
COPY ./src/ /wwq/src
COPY ./requirements.txt /wwq
COPY ./api_queue.py /wwq

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["gunicorn", "-b", "0.0.0.0:80", "api_queue:__hug_wsgi__"]
