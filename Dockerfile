# Use uma imagem base do Ubuntu
FROM ubuntu:20.04

# Instale dependências essenciais
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libboost-all-dev \
    libopencv-dev \
    libopenblas-dev \
    liblapack-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libdcmtk-dev \
    libopenni2-dev \
    wget \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clone o repositório OpenFace
RUN git clone https://github.com/TadasBaltrusaitis/OpenFace.git /opt/OpenFace

# Compilar o OpenFace
WORKDIR /opt/OpenFace/build
RUN cmake ..
RUN make

# Definir o diretório de trabalho
WORKDIR /opt/OpenFace

# Comando padrão ao iniciar o container (substitua conforme necessário)
CMD ["./build/bin/FeatureExtraction"]
