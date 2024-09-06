# Change it to the version that is compatible with your Nvidia drivers
FROM nvidia/cuda:11.7.1-base-ubuntu20.04

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
    python3-pip \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Change it to the version that is compatible with your Nvidia drivers
RUN pip3 install torch==1.13.1+cu117 \
                torchvision==0.14.1+cu117 \
                torchaudio==0.13.1+cu117 \
                --extra-index-url https://download.pytorch.org/whl/cu117

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]
