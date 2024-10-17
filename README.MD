# OrganizeX

**OrganizeX** é uma ferramenta inovadora que simplifica a gestão financeira, permitindo que usuários importem facilmente dados de diferentes formatos, como XLSX, CSV e PDF. O projeto automatiza a leitura e conversão dessas informações em um arquivo XLSX personalizado, pronto para ser integrado ao aplicativo de controle de finanças, **Organize**.

## Recursos

- **Importação de Múltiplos Formatos**: Suporte para arquivos XLSX.
- **Conversão Automatizada**: Transforme dados financeiros em um formato organizado e fácil de usar.
- **Integração Simples**: Os arquivos convertidos são prontos para serem usados no aplicativo **Organize**.

## Instalação

Para utilizar o OrganizeX, você precisa ter o Python instalado em sua máquina. Siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/Luiz1nn/organizex.git
   ```
   
2. Navegue até o diretório do projeto:
   ```bash
   cd OrganizeX
   ```

3. Instale as dependências necessárias:
   ```bash
   python3 setup.py
   ```

## Uso

Para usar o OrganizeX, execute o seguinte comando no terminal:

```bash
python organizex.py --input <caminho_do_arquivo> --output <caminho_do_arquivo_saida>
```

Substitua `<caminho_do_arquivo>` pelo caminho do arquivo que você deseja importar e `<caminho_do_arquivo_saida>` pelo nome do arquivo XLSX que será gerado.

## Exemplos

- Importar um arquivo XLSX:
  ```bash
  python organizex.py --input ./dados/financas.xlsx --output ./saida/financas_convertidas.xlsx
  ```

## Contato

Para mais informações, entre em contato:

- Author: Luiz1nn
- Linkedin: [Luis Fernando da Silva](https://www.linkedin.com/in/luis-fernando-s/)
