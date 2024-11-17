### Gerando um Novo `requirements.txt` Quando o `Pipfile` For Atualizado

Esta documentação descreve os passos necessários para gerar um novo arquivo `requirements.txt` sempre que o `Pipfile` ou `Pipfile.lock` for atualizado. Este arquivo é destinado exclusivamente para uso em containers Docker, garantindo que o ambiente do Docker possa instalar as dependências necessárias para rodar o projeto.

---

#### **Pré-requisitos**

- Python instalado na máquina.
- `pipenv` instalado. Se ainda não tiver, instale com:
  ```bash
  pip install pipenv
  ```

---

#### **Passos**

1. **Atualize o `Pipfile`**

- Certifique-se de que as dependências no `Pipfile` estejam atualizadas.
- Caso tenha adicionado ou alterado dependências, execute:
  ```bash
  pipenv install
  ```

2. **Gere o `requirements.txt`**

- O arquivo `requirements.txt` deve ser gerado para ser usado especificamente pelo Docker. Use o comando:
  ```bash
  pipenv requirements > requirements.txt
  ```
- Este comando exporta as dependências do ambiente virtual gerenciado pelo `pipenv` em um formato que o Docker consegue interpretar.

3. **Verifique o `requirements.txt`**

- Abra o arquivo gerado e confirme que ele contém as dependências necessárias no formato adequado, por exemplo:
  ```plaintext
  -i https://pypi.org/simple
  pandas==2.2.3
  openpyxl==3.1.5
  ```

4. **Configure o Dockerfile**

- No seu `Dockerfile`, certifique-se de incluir a instalação das dependências a partir do `requirements.txt`. Um exemplo de trecho para o `Dockerfile` seria:
  ```dockerfile
  COPY requirements.txt /app/
  RUN pip install --no-cache-dir -r requirements.txt
  ```

5. **Construa a Imagem Docker**

- Após gerar o `requirements.txt`, você pode construir a imagem do Docker normalmente:
  ```bash
  docker build -t nome-da-imagem .
  ```

---

#### **Considerações**

- O arquivo `requirements.txt` é gerado exclusivamente para uso com o Docker, pois o Docker não reconhece o `Pipfile` ou o ambiente virtual gerenciado pelo `pipenv` diretamente.
- Este processo garante consistência entre o ambiente local e o container Docker, evitando problemas de dependências ao rodar o projeto em containers.
