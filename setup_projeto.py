import os

def criar_projeto():
    print("🛠️ Criando projeto 'Mãos à Obra' do zero...")

    # 1. Pastas do projeto
    os.makedirs("templates", exist_ok=True)
    os.makedirs("static/css", exist_ok=True)
    os.makedirs("static/js", exist_ok=True)

    # 2. app.py
    app_py = """from flask import Flask, render_template, request, jsonify

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
"""
    with open("app.py", "w", encoding="utf-8") as f:
        f.write(app_py)

    # 3. gerar_planilha.py
    gerar_planilha_py = """import openpyxl

def criar_excel():
    wb = openpyxl.Workbook()

    ws_info = wb.active
    ws_info.title = "Informacao"
    info_data = [
        ["Campo", "Detalhes"],
        ["Nome da Dupla", "Dupla Elétrica - Módulo 3.3"],
        ["Nome dos participantes", "Participante 1, Participante 2"],
        ["URL do projeto", "https://github.com/dupla/portal-educativo"],
        ["Nome das tecnologias", "Python, Flask, HTML5, CSS3, JavaScript, VS Code"],
        ["Etapa 01", "Organização do projeto"],
        ["Etapa 02", "Pesquisa técnica"],
        ["Etapa 03", "Desenvolvimento"],
        ["Etapa 04", "Apresentação"],
        ["Referências - Imagens", "Unsplash / Pexels (Licença Gratuita)"],
        ["Referências - Textos", "Boylestad (Análise de Circuitos), Sadiku (Circuitos Elétricos)"],
        ["Referências - PDF", "Apostilas Técnicas de Eletrotécnica"]
    ]
    for row in info_data:
        ws_info.append(row)

    ws_dados = wb.create_sheet(title="Dados")
    headers = ["Número", "Etapa", "Responsável", "Descrição", "Data prevista", "Data real", "Status", "Percentual", "Observação"]
    ws_dados.append(headers)

    tasks_data = [
        [1, "Etapa 01: Organização do projeto", "Participante 1", "Criação do repositório no GitHub e estrutura inicial", "2026-10-21", "2026-10-21", "Concluído", "100%", "Repositório compartilhado"],
        [2, "Etapa 01: Organização do projeto", "Participante 2", "Preenchimento da planilha de controle de projeto", "2026-10-21", "2026-10-21", "Concluído", "100%", "Abas Informacao e Dados organizadas"],
        [3, "Etapa 02: Pesquisa técnica", "Participante 1", "Levantamento teórico de Potência Elétrica e Efeito Joule", "2026-10-22", "2026-10-22", "Concluído", "100%", "Pesquisa técnica concluída"],
        [4, "Etapa 02: Pesquisa técnica", "Participante 2", "Seleção de imagens gratuitas e elaboração do Quiz", "2026-10-22", "2026-10-22", "Concluído", "100%", "Imagens gratuitas Unsplash"],
        [5, "Etapa 03: Desenvolvimento", "Participante 1", "Desenvolvimento da estrutura HTML e rotas em Python (Flask)", "2026-10-23", "2026-10-23", "Concluído", "100%", "Estrutura Mãos à Obra"],
        [6, "Etapa 03: Desenvolvimento", "Participante 2", "Estilização CSS e interatividade do Quiz em JS", "2026-10-24", "2026-10-24", "Concluído", "100%", "Design Mãos à Obra"],
        [7, "Etapa 04: Apresentação", "Dupla", "Elaboração da apresentação e explicação do portal", "2026-10-25", "2026-10-25", "Pendente", "0%", "Preparação final"]
    ]
    for row in tasks_data:
        ws_dados.append(row)

    wb.save("controle_projeto.xlsx")
    print("  [✓] Planilha 'controle_projeto.xlsx' gerada com sucesso!")

if __name__ == '__main__':
    criar_excel()
"""
    with open("gerar_planilha.py", "w", encoding="utf-8") as f:
        f.write(gerar_planilha_py)

    # 4. index.html
    index_html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mãos à Obra - Potência Elétrica e Efeito Joule</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>

    <header class="header">
        <div class="logo">
            <span class="icon">🔨⚡</span>
            <h1>Mãos à Obra</h1>
        </div>
        <nav class="nav-menu">
            <a href="#">Início</a>
            <a href="#conteudo">Conteúdo Técnico</a>
            <a href="#exemplos">Exemplos</a>
            <a href="#quiz">Quiz</a>
        </nav>
        <div class="search-box">
            <input type="text" id="searchInput" placeholder="Buscar no portal...">
            <button onclick="executarBusca()">Buscar</button>
        </div>
        <div class="cta-buttons">
            <a href="#contato" class="btn btn-secondary">Contato</a>
            <a href="#" class="btn btn-primary">Entrar</a>
        </div>
    </header>

    <div class="main-layout">
        <main class="content-area">
            <article class="topic-card">
                <header class="topic-header">
                    <span class="badge">Módulo Exclusivo</span>
                    <h1>Potência Elétrica e Efeito Joule</h1>
                </header>

                <section class="topic-section">
                    <h2>Introdução</h2>
                    <p>A potência elétrica e o efeito Joule são conceitos centrais para o projeto e análise de sistemas eletroeletrônicos. Compreender a taxa de conversão de energia e o aquecimento derivado da passagem de corrente é fundamental para o dimensionamento seguro de cabos, escolha de componentes, desenvolvimento de sistemas de refrigeração e prevenção de falhas em circuitos residenciais e industriais.</p>
                </section>

                <section class="topic-section" id="conteudo">
                    <h2>Conteúdo Técnico</h2>
                    
                    <h3>1. Potência Elétrica</h3>
                    <p>Potência elétrica (\\(P\\)) é a quantidade de trabalho elétrico realizado por unidade de tempo, ou seja, a taxa com que a energia elétrica é convertida em outra forma de energia (como luz, calor ou movimento). A unidade de medida no Sistema Internacional é o Watt (W).</p>
                    
                    <p>A fórmula fundamental para circuitos de Corrente Contínua (CC) é:</p>
                    <div class="formula-box">\\(P = V \\times I\\)</div>
                    <p>Onde \\(P\\) é a potência em Watts (W), \\(V\\) é a tensão em Volts (V) e \\(I\\) é a intensidade da corrente em Ampères (A).</p>

                    <p>Combinando essa relação com a Lei de Ohm (\\(V = I \\times R\\)), podemos expressar a potência em termos da resistência elétrica (\\(R\\)):</p>
                    <div class="formula-box">\\(P = I^2 \\times R \\quad \\text{ou} \\quad P = \\frac{V^2}{R}\\)</div>

                    <h3>2. Efeito Joule</h3>
                    <p>O Efeito Joule é o fenômeno físico no qual a passagem de corrente elétrica através de um condutor gera calor, resultante das colisões entre os elétrons em movimento e a estrutura atômica do condutor.</p>
                    
                    <p>A quantidade de energia térmica (\\(Q\\)) dissipada em Joules (J) durante um tempo \\(t\\) (em segundos) é dada por:</p>
                    <div class="formula-box">\\(Q = I^2 \\times R \\times t\\)</div>

                    <p>Quando expressa em calorias (cal), utiliza-se o fator de conversão de equivalência térmica (\\(1\\text{ cal} \\approx 4{,}18\\text{ J}\\)):</p>
                    <div class="formula-box">\\(Q_{\\text{cal}} \\approx 0{,}24 \\times I^2 \\times R \\times t\\)</div>
                </section>

                <section class="topic-section" id="exemplos">
                    <h2>Exemplos Práticos</h2>
                    <div class="example-grid">
                        <div class="example-card">
                            <h4>Chuveiro Elétrico</h4>
                            <p>Um chuveiro de \\(5500\\text{ W}\\) ligado em \\(220\\text{ V}\\) exige uma corrente de \\(I = \\frac{5500}{220} = 25\\text{ A}\\). O aquecimento rápido da água ocorre justamente pelo efeito Joule no resistor do chuveiro.</p>
                        </div>
                        <div class="example-card">
                            <h4>Dimensionamento de Condutores</h4>
                            <p>Se a fiação elétrica de uma instalação possui resistência elevada ou Bitola incorreta, a corrente gerará um aquecimento indesejado (perda por efeito Joule), podendo derreter o isolamento térmico e causar curto-circuito.</p>
                        </div>
                        <div class="example-card">
                            <h4>Fusíveis Térmicos</h4>
                            <p>Dispositivos de segurança usam o efeito Joule a seu favor: quando a corrente ultrapassa o limite do projeto, o aquecimento derrete um elemento condutor interno, abrindo o circuito e protegendo a instalação.</p>
                        </div>
                    </div>
                </section>

                <section class="topic-section">
                    <h2>Recursos Visuais</h2>
                    <div class="image-gallery">
                        <figure>
                            <img src="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600" alt="Placa de circuito e dissipador de calor">
                            <figcaption>Figura 1: Dissipadores de calor em circuitos eletrônicos evitam sobreaquecimento por Efeito Joule. (Fonte: Unsplash)</figcaption>
                        </figure>
                        <figure>
                            <img src="https://images.unsplash.com/photo-1544724569-5f546fd6f2b5?w=600" alt="Resistor com código de cores">
                            <figcaption>Figura 2: Resistores convertem energia elétrica excedente em calor em circuitos. (Fonte: Unsplash)</figcaption>
                        </figure>
                    </div>
                </section>

                <section class="topic-section summary-box">
                    <h2>Resumo para o Caderno 📝</h2>
                    <ul>
                        <li><strong>Potência Elétrica (\\(P\\)):</strong> Medida em Watts (W). Representa a velocidade de conversão de energia.</li>
                        <li><strong>Fórmula Principal:</strong> \\(P = V \\times I\\).</li>
                        <li><strong>Fórmulas Secundárias:</strong> \\(P = I^2 \\times R\\) e \\(P = \\frac{V^2}{R}\\).</li>
                        <li><strong>Efeito Joule:</strong> Transformação de energia elétrica em energia térmica devido às colisões de elétrons no condutor (\\(Q = I^2 \\times R \\times t\\)).</li>
                        <li><strong>Aplicação Principal:</strong> Aquecedores, fusíveis, chuveiros (desejável) e perdas em linhas de transmissão (indesejável).</li>
                    </ul>
                </section>

                <section class="topic-section" id="quiz">
                    <h2>Quiz de Fixação 🧠</h2>
                    <div id="quiz-container">
                        <div class="question" id="q1">
                            <p>1. Um resistor de \\(10\\ \\Omega\\) é percorrido por uma corrente de \\(2\\text{ A}\\). Qual é a potência dissipada por ele?</p>
                            <button onclick="checarResposta('q1', false)">A) \\(20\\text{ W}\\)</button>
                            <button onclick="checarResposta('q1', true)">B) \\(40\\text{ W}\\)</button>
                            <button onclick="checarResposta('q1', false)">C) \\(100\\text{ W}\\)</button>
                            <div class="feedback"></div>
                        </div>

                        <div class="question" id="q2">
                            <p>2. Por que as linhas de transmissão operam em alta tensão para longas distâncias?</p>
                            <button onclick="checarResposta('q2', false)">A) Para aumentar a corrente nos cabos.</button>
                            <button onclick="checarResposta('q2', true)">B) Para reduzir a corrente e minimizar as perdas por Efeito Joule.</button>
                            <button onclick="checarResposta('q2', false)">C) Para eliminar a resistência dos condutores.</button>
                            <div class="feedback"></div>
                        </div>
                    </div>
                </section>

                <section class="topic-section">
                    <h2>Referências</h2>
                    <ul>
                        <li>BOYLESTAD, Robert L. <em>Introdução à Análise de Circuitos</em>. 13ª ed. São Paulo: Pearson, 2019.</li>
                        <li>SADIKU, Matthew N. O.; ALEXANDER, Charles K. <em>Fundamentos de Circuitos Elétricos</em>. 6ª ed. Porto Alegre: AMGH, 2017.</li>
                        <li>Imagens gratuitas obtidas via Unsplash (Licença Aberta/Livre uso).</li>
                    </ul>
                </section>
            </article>
        </main>
    </div>

    <footer class="footer" id="contato">
        <div class="footer-container">
            <div class="footer-col">
                <h4>Mãos à Obra</h4>
                <p>Portal educacional focado em Eletroeletrônica: Potência Elétrica e Efeito Joule.</p>
                <p>© 2026 Mãos à Obra. Todos os direitos reservados.</p>
            </div>
            <div class="footer-col">
                <h4>Links Institucionais</h4>
                <ul>
                    <li><a href="#">Quem Somos</a></li>
                    <li><a href="#">Políticas de Privacidade</a></li>
                    <li><a href="#">Termos de Uso</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Contato</h4>
                <p>Email: contato@maosaobra.com.br</p>
                <p>Tel: (51) 3700-0000</p>
                <p>CNPJ: 00.123.456/0001-89</p>
            </div>
            <div class="footer-col">
                <h4>Redes Sociais & Mapa</h4>
                <div class="social-links">
                    <a href="#">LinkedIn</a> | <a href="#">GitHub</a> | <a href="#">YouTube</a>
                </div>
                <p><a href="#">Mapa do Site (Sitemap)</a></p>
            </div>
        </div>
    </footer>

    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
</body>
</html>
"""
    with open("templates/index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

    # 5. style.css
    style_css = """:root {
    --primary: #0f172a;
    --primary-light: #2563eb;
    --accent: #f59e0b;
    --bg-light: #f8fafc;
    --text-dark: #1e293b;
    --card-bg: #ffffff;
    --border-color: #e2e8f0;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

body {
    background-color: var(--bg-light);
    color: var(--text-dark);
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.header {
    background-color: var(--primary);
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 2rem;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.logo {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.logo h1 { font-size: 1.5rem; }

.nav-menu a {
    color: white;
    text-decoration: none;
    margin: 0 1rem;
    font-weight: 500;
}

.search-box {
    display: flex;
    gap: 0.5rem;
}

.search-box input {
    padding: 0.5rem;
    border-radius: 4px;
    border: none;
}

.search-box button {
    padding: 0.5rem 1rem;
    background-color: var(--accent);
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-weight: bold;
}

.btn {
    padding: 0.5rem 1rem;
    border-radius: 4px;
    text-decoration: none;
    font-size: 0.9rem;
}

.btn-primary { background-color: var(--primary-light); color: white; }
.btn-secondary { background-color: transparent; border: 1px solid white; color: white; }

.main-layout {
    display: flex;
    justify-content: center;
    flex: 1;
    padding: 2rem 1rem;
}

.content-area {
    width: 100%;
    max-width: 900px;
}

.topic-card {
    background-color: var(--card-bg);
    padding: 2.5rem;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}

.badge {
    background-color: var(--accent);
    color: white;
    padding: 0.3rem 0.8rem;
    border-radius: 12px;
    font-size: 0.85rem;
    font-weight: bold;
}

.topic-header h1 {
    margin-top: 0.75rem;
    color: var(--primary);
    font-size: 2.2rem;
}

.topic-section { margin-top: 2rem; }

.topic-section h2 {
    color: var(--primary-light);
    border-bottom: 2px solid var(--border-color);
    padding-bottom: 0.5rem;
    margin-bottom: 1rem;
}

.topic-section h3 { margin: 1rem 0 0.5rem 0; }

.formula-box {
    background-color: #f1f5f9;
    padding: 1.2rem;
    border-left: 4px solid var(--primary-light);
    margin: 1rem 0;
    font-weight: bold;
    text-align: center;
    font-size: 1.1rem;
}

.example-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1rem;
}

.example-card {
    background-color: #f8fafc;
    padding: 1.2rem;
    border-radius: 6px;
    border: 1px solid var(--border-color);
}

.image-gallery {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}

.image-gallery figure { flex: 1; min-width: 250px; }

.image-gallery img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 6px;
}

.summary-box {
    background-color: #f0fdf4;
    border: 1px solid #bbf7d0;
    padding: 1.5rem;
    border-radius: 6px;
}

.question {
    background-color: #f8fafc;
    padding: 1rem;
    border-radius: 6px;
    margin-bottom: 1rem;
}

.question button {
    display: block;
    width: 100%;
    text-align: left;
    padding: 0.6rem;
    margin-top: 0.5rem;
    background-color: white;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    cursor: pointer;
}

.question button:hover { background-color: #e2e8f0; }

.feedback { margin-top: 0.5rem; font-weight: bold; }

.footer {
    background-color: #0f172a;
    color: white;
    padding: 2.5rem 2rem;
    margin-top: auto;
}

.footer-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
    max-width: 1200px;
    margin: 0 auto;
}

.footer h4 { margin-bottom: 1rem; color: var(--accent); }
.footer ul { list-style: none; }
.footer a { color: #94a3b8; text-decoration: none; }
.footer a:hover { color: white; }
"""
    with open("static/css/style.css", "w", encoding="utf-8") as f:
        f.write(style_css)

    # 6. script.js
    script_js = """function checarResposta(questionId, isCorrect) {
    const container = document.getElementById(questionId);
    const feedback = container.querySelector('.feedback');
    
    if (isCorrect) {
        feedback.textContent = "✅ Resposta Correta! Excelente trabalho.";
        feedback.style.color = "green";
    } else {
        feedback.textContent = "❌ Resposta Incorreta. Revise o conteúdo acima e tente novamente.";
        feedback.style.color = "red";
    }
}

function executarBusca() {
    const query = document.getElementById('searchInput').value.trim();
    if (!query) {
        alert("Por favor, digite um termo para busca.");
        return;
    }
    
    fetch(`/api/busca?q=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            if (data.length > 0) {
                alert(`Conteúdo encontrado: ${data[0].titulo}`);
            } else {
                alert("Nenhum resultado encontrado para essa busca.");
            }
        })
        .catch(err => console.error("Erro na busca:", err));
}
"""
    with open("static/js/script.js", "w", encoding="utf-8") as f:
        f.write(script_js)

    # 7. README.md
    readme_md = """# Mãos à Obra - Potência Elétrica e Efeito Joule 🔨⚡

## Objetivos do Projeto
Projeto focado exclusivamente no ensino de **Potência Elétrica e Efeito Joule**, trazendo conteúdo teórico, exemplos práticos, ilustrações, resumo e quiz de fixação.

## Tecnologias Utilizadas
- Python 3.x / Flask
- HTML5 / CSS3 / JavaScript
- openpyxl (Geração da planilha Excel)

## Como Executar
1. `python setup_projeto.py` (Gera todos os arquivos)
2. `python gerar_planilha.py` (Gera o Excel de controle)
3. `python app.py` (Inicia o servidor em http://127.0.0.1:5000)
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_md)

    print("🎉 Todos os arquivos do projeto 'Mãos à Obra' foram gerados com sucesso!")

if __name__ == "__main__":
    criar_projeto()