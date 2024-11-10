# Dockerfile

# Usa a imagem oficial do Python 3.12.6
FROM python:3.12.6-slim

# Instalar dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    curl \
    git \
    make \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    python3-dev \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo requirements.txt (gerado a partir do Pipfile.lock ou pip freeze)
COPY requirements.txt /app/

# Instalar as dependências do projeto usando o pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o resto dos arquivos do projeto
COPY . .

# Comando para rodar a aplicação
CMD ["python", "organizex.py"]
