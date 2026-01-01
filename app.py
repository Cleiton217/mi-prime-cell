import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from supabase import create_client, Client
from dotenv import load_dotenv

# 1. Carrega as variáveis do seu arquivo .env
load_dotenv()

app = Flask(__name__)

# 2. Configuração do CORS (Vital para o Front-end acessar a API)
CORS(app)

# 3. Configurações de conexão com o Supabase
SUPABASE_URL = "https://oixxpvupokedqfetyarz.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9peHhwdnVwb2tlZHFmZXR5YXJ6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjMyNDc0OTMsImV4cCI6MjA3ODgyMzQ5M30.rJthexTj2qtKPVQ2ogQrMHjFT-w0HmVlrq7JVMe6eQU"

# Inicializa o cliente do Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# =========================================================
# ROTAS DA API
# =========================================================

@app.route('/api/config', methods=['GET'])
def get_config():
    """Retorna o status da conexão para o front-end."""
    return jsonify({
        "loja": "MI-PRIME-CELL",
        "numero_da_loja": "5521999999999", # SUBSTITUA PELO SEU WHATSAPP REAL (DDI+DDD+NUMERO)
        "status": "online",
        "database": "Supabase Connected"
    })

@app.route('/api/produtos', methods=['GET'])
def get_produtos():
    try:
        response = supabase.table('produtos').select("*").execute()
        produtos_raw = response.data
        
        produtos_formatados = []
        for index, p in enumerate(produtos_raw):
            # Tenta pegar o ID da coluna 'eu_ia', se for nulo, usa o índice
            prod_id = p.get('eu_ia') if p.get('eu_ia') is not None else index
            
            produtos_formatados.append({
                "id": prod_id,
                "nome": p.get('nome', 'Sem nome'),
                "marca": p.get('marca', 'Apple'),
                "modelo": p.get('modelo', ''),
                "preco": float(p.get('preco', 0)),
                "url_imagem": p.get('url_imagem'),
                "descricao": p.get('descricao', '')
            })
            
        return jsonify(produtos_formatados)
    except Exception as e:
        print(f"Erro: {e}")
        return jsonify([]), 500
# =========================================================
# EXECUÇÃO
# =========================================================

if __name__ == '__main__':
    print("--- SERVIDOR MI-PRIME-CELL RODANDO ---")
    print("API disponível em: http://127.0.0.1:5000/api/produtos")
    app.run(debug=True, port=5000)