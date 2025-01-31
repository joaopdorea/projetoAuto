from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os
import spacy
import pdfplumber

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Garante que a pasta de uploads existe

client = OpenAI(api_key="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")  # Substitua pela sua API Key

nlp = spacy.load("pt_core_news_sm")

def extrair_texto(arquivo_path):
    """Extrai texto de arquivos .txt e .pdf"""
    if arquivo_path.endswith(".txt"):
        with open(arquivo_path, "r", encoding="utf-8") as f:
            return f.read()
    elif arquivo_path.endswith(".pdf"):
        with pdfplumber.open(arquivo_path) as pdf:
            return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return "Formato não suportado."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = ""
    prompt = ""

    # Verifica se um arquivo foi enviado
    if "file" in request.files:
        file = request.files["file"]
        if file.filename != "":
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)  # Salvar o arquivo
            user_input = extrair_texto(filepath)  # Extrair o texto do arquivo

    # Se não houver arquivo, usa o input de texto
    if not user_input:
        data = request.json
        user_input = data.get("input", "")

    # Processamento de NLP (Lematização)
    doc = nlp(user_input)
    for token in doc:
        prompt += token.lemma_ + " "

    if not user_input:
        return jsonify({"error": "Nenhuma mensagem enviada"}), 400

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Considere o seguinte e-mail com as seguintes palavras-chave: {prompt}. Você considera esse e-mail PRODUTIVO (pergunta sobre alguma tarefa ou prazo) ou IMPRODUTIVO (não pergunta sobre prazo ou tarefa específica)? Responda somente com PRODUTIVO ou IMPRODUTIVO mais um delimitador ( | ) mais uma resposta adequada para o e-mail."
                }
            ],
            model="gpt-4o",
        )
        message = chat_completion.choices[0].message.content
        return jsonify({"response": message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
