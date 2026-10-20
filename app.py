from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

CONTEUDOS = [
    {"id": "3.3", "titulo": "Potência Elétrica e Efeito Joule", "categoria": "Grandezas e Circuitos Elétricos"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/busca', methods=['GET'])
def buscar():
    query = request.args.get('q', '').lower()
    resultados = [item for item in CONTEUDOS if query in item['titulo'].lower()]
    return jsonify(resultados)

if __name__ == '__main__':
    print("Servidor rodando em: http://127.0.0.1:5000")
    app.run(debug=True)
