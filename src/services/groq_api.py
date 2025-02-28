#
# Responsável por fazer a chamada da API (via POST), passando a pergunta como parâmetro

import requests, json
from config import GROQ_API_KEY, GROQ_API_URL

def consultar_groqcloud(pergunta: str) -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{
            "role": "user",
            "content": pergunta
        }]
    }

    try:
        response = requests.post(GROQ_API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Garante que erros HTTP gerem exceção

        # Converte a resposta em JSON (a resposta é retornada como bytes)
        json_bytes = response.content
        json_str = json_bytes.decode('utf-8')
        json_dict = json.loads(json_str)

        # Extrai o valor do nó 'content'
        conteudo = json_dict.get("choices", [{}])[0].get("message", {}).get("content")

        if conteudo:
            return f"Resposta da IA: {conteudo}"
        return "Resposta não encontrada no JSON."

    except (json.JSONDecodeError, KeyError, IndexError, AttributeError, UnicodeDecodeError) as e:
        return f"Erro ao processar a resposta da API: {e}"
    except requests.RequestException as e:
        return f"Erro ao consultar a API GroqCloud: {e}"
