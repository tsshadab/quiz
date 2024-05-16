# Base image - latest opensuse
FROM opensuse/tumbleweed:latest
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_BREAK_SYSTEM_PACKAGES 1
ENV PIP_NO_CACHE_DIR=1
# Install packages
RUN zypper --non-interactive up
RUN zypper --non-interactive in python3-devel python3-pip python311
# Clean zypper cache
RUN zypper cc -a
# Copy all files to /usr/src/app
COPY . /usr/src/app
# Set working directory
WORKDIR /usr/src/app
# Install python packages
RUN pip3 install -r requirements.txt
# Create a user idp with uid 1000 and add it to the root group
RUN useradd -m -u 1000 idp && chown -R idp /usr/src/app
# Switch to user idp
USER 1000
# Run the application on port 8080 when the container launches  
ENTRYPOINT ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "frontend.main:app", "--bind", "0.0.0.0:8080"]