# PROBLEM: Full Ubuntu base — huge attack surface
  # Better: use python:3.12-slim or a distroless image
  FROM ubuntu:20.04
  
  # PROBLEM: No USER directive — runs as root inside the container
  
  RUN apt-get update && apt-get install -y \
      python3 python3-pip \
      curl wget vim git    # PROBLEM: Tools the app never needs
  
  WORKDIR /app
  COPY requirements.txt .
  RUN pip3 install -r requirements.txt
  COPY . .
  
  EXPOSE 5000
  CMD ["python3", "app.py"]
