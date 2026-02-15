// URL da sua API Flask
const API_URL = "http://127.0.0.1:5000/api/produtos";

async function carregarCatalogo() {
    const vitrine = document.getElementById('vitrine-produtos'); // Certifique-se que esse ID existe no seu HTML
    
    try {
        const resposta = await fetch(API_URL);
        const celulares = await resposta.json();

        // Limpa a vitrine antes de carregar
        vitrine.innerHTML = "";

        celulares.forEach(celular => {
            // Criando o elemento do card
            const card = document.createElement('div');
            card.className = 'produto-card';

            // Montando o HTML do card com os dados do Supabase
            card.innerHTML = `
                <div class="tag-marca">${celular.marca}</div>
                <img src="${celular.imagem_url}" alt="${celular.nome}" class="produto-img">
                <div class="produto-info">
                    <h3>${celular.nome}</h3>
                    <p class="modelo-detalhe">${celular.modelo}</p>
                    <p class="preco">R$ ${celular.preco.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}</p>
                    <button class="btn-whatsapp" onclick="enviarWhatsapp('${celular.nome}', '${celular.modelo}')">
                        Tenho Interesse
                    </button>
                </div>
            `;
            vitrine.appendChild(card);
        });

    } catch (erro) {
        console.error("Erro ao carregar o catálogo:", erro);
        vitrine.innerHTML = "<p>Erro ao carregar produtos. Verifique se o servidor Flask está rodando.</p>";
    }
}

// Função para facilitar a venda pelo WhatsApp
function enviarWhatsapp(nome, modelo) {
    const numero = "55XXXXXXXXXXX"; // COLOQUE SEU NÚMERO AQUI (com DDD)
    const mensagem = encodeURIComponent(`Olá! Vi no catálogo o ${nome} (${modelo}) e gostaria de mais informações.`);
    window.open(`https://wa.me/${numero}?text=${mensagem}`, '_blank');
}

// Inicia o carregamento quando a página abre
document.addEventListener('DOMContentLoaded', carregarCatalogo);