import env
import openai
from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS

openai.api_key = env.api_key
initialPrompt = """hace de cuenta que sos un analizador de sentimientos. yo te paso sentimientos y vos analizas
                   el sentimiento de los mensaje y me das una respuesta con al menos 1 caracter y un máximo de 4 caracteres
                   SOLO RESPUESTAS NUMÉRICAS, -1 es negatividad máxima, 0 es neutral y 1 es positivo. (podes usar valores flotantes)."""
messages = [
    {"role": "system", "content": initialPrompt}
]

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, polaridad):
        return polaridad

analizador = AnalizadorDeSentimientos()

app = Flask(__name__)
CORS(app)  # Allow all origins

# Add this route to serve static files (styles.css)
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# Update the existing route to use the static CSS file
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analizar_sentimientos', methods=['POST'])
def analizar_sentimientos():
    data = request.get_json()  # Parse JSON data
    user_prompt = data.get('user_prompt', '')

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Analiza el sentimiento del siguiente texto:"},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=1200
    )

    sentimiento = analizador.analizar_sentimiento(completion.choices[0].message['content'])

    return jsonify({'sentimiento': sentimiento})

if __name__ == '__main__':
    app.run(debug=True)









