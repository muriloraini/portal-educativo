import openpyxl

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
