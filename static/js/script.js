function checarResposta(questionId, isCorrect) {
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
