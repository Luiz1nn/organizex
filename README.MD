# OrganizeX

**OrganizeX** é uma ferramenta inovadora projetada para simplificar a gestão financeira. Ela permite que os usuários importem dados de diferentes formatos, como **XLSX**, **CSV** e **PDF**, e os converta de maneira automatizada em um arquivo **XLS** personalizado, pronto para ser integrado ao aplicativo **Organize**, um sistema de controle financeiro.

## Recursos

- **Importação de Múltiplos Formatos**: Suporte para arquivos XLSX, CSV e PDF.
- **Conversão Automatizada**: Transforma dados financeiros em um formato organizado e fácil de usar.
- **Integração Simples**: Arquivos convertidos são prontos para serem usados diretamente no aplicativo **Organize**.

## Requisitos do Sistema

- **Python 3.12.6**: Certifique-se de usar a versão correta do Python. Caso você tenha múltiplas versões, pode usar um gerenciador de versões como o **asdf** para alternar facilmente entre as versões.
- **Docker (opcional)**: Caso prefira, você pode rodar o **OrganizeX** em um container Docker.

## Instalação

### Usando Python

Para utilizar o **OrganizeX** no seu ambiente local, você precisará ter o **Python 3.12.6** instalado em sua máquina.

#### Passos para instalar o OrganizeX:

1. **Clone o repositório** (se ainda não fez isso):

   ```bash
   git clone https://github.com/Luiz1nn/organizex.git
   ```

2. **Navegue até o diretório do projeto**:

   ```bash
   cd organizex
   ```

3. **Execute o `setup.py` para instalar as dependências**:
   - Isso vai verificar e instalar o `pipenv`, e instalar as dependências do projeto.
   ```bash
   python setup.py
   ```

### Como usar:

1. **Para usar o OrganizeX**:

   - Sempre que precisar usar o OrganizeX, entre no ambiente virtual com o comando:

     ```bash
     pipenv shell
     ```

     Isso irá ativar o ambiente virtual do `pipenv`, e você poderá rodar o OrganizeX normalmente.

   - Para rodar o **OrganizeX**, use o comando:
     ```bash
     python organizex.py --input <caminho_do_arquivo> --output <caminho_do_arquivo_saida>
     ```

### Usando Docker

Caso você prefira não instalar o Python localmente, pode rodar o **OrganizeX** utilizando o Docker. Para isso, siga os passos abaixo:

#### Passos para rodar via Docker:

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/Luiz1nn/organizex.git
   ```

2. **Navegue até o diretório do projeto**:

   ```bash
   cd organizex
   ```

3. **Baixe a imagem mais recente do Docker Hub**:

   ```bash
   docker pull luizinn/organizex:v1.5.0
   ```

4. **Execute o container Docker**:

   Para rodar o OrganizeX com Docker Compose, use o comando abaixo, substituindo <caminho_do_arquivo> e <caminho_do_arquivo_saida> pelos caminhos reais no seu sistema:

   ```bash
   docker compose -f docker/docker-compose.yml run --rm organizex --input files/file.xlsx --output files/converted-file.xls
   ```

## Uso

Para usar o **OrganizeX**, basta executar o seguinte comando no terminal, seja no ambiente Python ou Docker:

```bash
python organizex.py --input <caminho_do_arquivo> --output <caminho_do_arquivo_saida>
```

- **`<caminho_do_arquivo>`**: O caminho para o arquivo de entrada (pode ser um arquivo XLSX, CSV ou PDF).
- **`<caminho_do_arquivo_saida>`**: O caminho e nome do arquivo XLS gerado após a conversão.

### Exemplo

Para importar um arquivo **XLSX** e gerar um novo arquivo **XLS**:

```bash
python organizex.py --input files/file.xlsx --output files/converted-file.xls
```

Ou, se estiver utilizando Docker:

```bash
docker compose -f docker/docker-compose.yml run --rm organizex --input files/file.xlsx --output files/converted-file.xls
```

## Contato

Para mais informações ou ajuda:

- **Autor**: Luiz1nn
- **LinkedIn**: [Luis Fernando da Silva](https://www.linkedin.com/in/luis-fernando-s/)
