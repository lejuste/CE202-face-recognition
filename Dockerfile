 
# This is a sample Dockerfile you can modify to deploy your own app based on face_recognition

FROM python:3.4-slim

# Set the working directory to /app
#WORKDIR /app
# Copy the current directory contents into the container at /app
#ADD . /app

RUN apt-get -y update
RUN apt-get install -y --fix-missing \
	parallel \
    	build-essential \
   	cmake \
    	gfortran \
	git \
	wget \
	curl \
	graphicsmagick \
	libgraphicsmagick1-dev \
	libatlas-dev \
	libavcodec-dev \
	libavformat-dev \
	libgtk2.0-dev \
	libjpeg-dev \
	liblapack-dev \
	libswscale-dev \
	pkg-config \
	python3-dev \
	python3-numpy \
	software-properties-common \
	zip \
	&& apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN cd ~ && \
    	mkdir -p dlib && \
    	git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    	cd  dlib/ && \
    	python3 setup.py install --yes USE_AVX_INSTRUCTIONS


ADD runTests.py /runTests.py
ADD runThreads.py /runThreads.py
ADD throughPutRun.py /throughPutRun.py
ADD obama-480p.jpg /obama-480p.jpg
ADD obama_small.jpg /obama_small.jpg
ADD biden.jpg /biden.jpg

# Install any needed packages specified in requirements.txt
#RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable


COPY . /face_recognition
RUN cd /face_recognition && \
    pip3 install -r requirements.txt && \
    python3 setup.py install



# Run app.py when the container launches

CMD python3 runTests.py
