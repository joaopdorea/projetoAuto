# 📧 Classificador de E-mails com Flask e OpenAI

## 📌 Sobre o Projeto

Este projeto é um Web App desenvolvido com **Python e Flask**, que utiliza a **API do ChatGPT** para classificar e-mails como **PRODUTIVOS** ou **IMPRODUTIVOS**. Além disso, ele sugere uma resposta adequada para o e-mail analisado.

### 🔍 Como Funciona?

1. O usuário pode inserir um texto manualmente ou fazer upload de um **arquivo .txt ou .pdf** contendo o texto do e-mail.
2. O Web App processa o texto enviado e envia a solicitação para a **API do ChatGPT**.
3. A API analisa o conteúdo e retorna:
   - Se o e-mail é **PRODUTIVO** (se faz uma pergunta sobre prazo ou tarefa específica) ou **IMPRODUTIVO** (se não contém uma pergunta relevante).
   - Uma **resposta sugerida** para o e-mail.
4. O diagnóstico e a sugestão de resposta são exibidos na tela.

## 🛠️ Tecnologias Utilizadas

- **Python** 🐍
- **Flask** (framework web)
- **HTML, CSS e JavaScript** (interface front-end)
- **pdfplumber** (para extração de texto de arquivos PDF)
- **OpenAI API** (para análise do e-mail e geração de respostas)

## 🚀 Como Rodar o Projeto Localmente

### 1️⃣ Clonar o repositório

```sh
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2️⃣ Criar e ativar um ambiente virtual (opcional, mas recomendado)

```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3️⃣ Instalar as dependências

```sh
pip install -r requirements.txt
```

### 4️⃣ Configurar a API Key da OpenAI

Crie um arquivo `.env` e adicione sua chave de API:

```
YOUR_API_KEY=sua-chave-aqui
```

Ou configure diretamente no código (não recomendado para produção):

```python
client = OpenAI(api_key="sua-chave-aqui")
```

### 5️⃣ Executar o servidor Flask

```sh
python app.py
```

O servidor será iniciado em `http://127.0.0.1:5000/`.

## 📂 Estrutura do Projeto

```
📂 projeto/
├── app.py  # Código principal do Flask
├── templates/
│   ├── index.html  # Página principal
├── static/
│   ├── styles.css  # Estilos do front-end
├── uploads/  # Pasta para armazenar arquivos temporários
├── requirements.txt  # Dependências do projeto
└── README.md  # Documentação
```


