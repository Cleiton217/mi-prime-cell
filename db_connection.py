import json
import os

# Constante para identificar a loja (pode ser usada no frontend)
NUMERO_LOJA = "CSDEV001" 

# Nome do arquivo onde os dados serão armazenados
DB_FILE = 'produtos.json'

# Estrutura inicial do banco de dados (se o arquivo não existir)
# Formato: (id, nome, descricao, preco)
INITIAL_PRODUCTS = [
    (1, "Notebook Gamer Pro X", "Potência e performance para jogos de última geração.", 7500.00),
    (2, "Mouse Sem Fio Ultra", "Design ergonômico e bateria de longa duração.", 150.99),
    (3, "Monitor 4K OLED 32\"", "Cores vibrantes e contraste infinito para profissionais.", 4899.50)
]

def load_produtos():
    """
    Carrega a lista de produtos do arquivo JSON.
    Se o arquivo não existir, cria o arquivo com os produtos iniciais.
    """
    if not os.path.exists(DB_FILE):
        # Cria o arquivo inicial se ele não existir
        save_produtos(INITIAL_PRODUCTS)
        return INITIAL_PRODUCTS
    
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            # Carrega a lista de listas (produtos)
            return json.load(f)
    except json.JSONDecodeError:
        # Se o arquivo estiver vazio ou corrompido, retorna produtos iniciais
        print(f"AVISO: Arquivo {DB_FILE} vazio ou corrompido. Usando dados iniciais.")
        return INITIAL_PRODUCTS
    except Exception as e:
        print(f"ERRO ao ler {DB_FILE}: {e}")
        return INITIAL_PRODUCTS

def save_produtos(produtos):
    """
    Salva a lista atual de produtos no arquivo JSON.
    """
    try:
        # Usa indent=4 para formatação legível (útil para debug)
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(produtos, f, indent=4)
    except Exception as e:
        print(f"ERRO ao salvar em {DB_FILE}: {e}")

# Teste básico para garantir que o arquivo existe
load_produtos()