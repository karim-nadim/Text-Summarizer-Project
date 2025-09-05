FROM python:3.8-slim-bullseye

RUN apt update -y && apt install awscli -y
RUN apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        g++ \
        make \
        python3-dev \
        libffi-dev \
        libssl-dev \
        curl \
        git \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

CMD ["python3", "app.py"]