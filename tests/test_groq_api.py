import pytest
from unittest.mock import patch
from src.services.groq_api import consultar_groqcloud

@patch("src.services.groq_api.requests.post")
def test_consultar_groqcloud(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"resposta": "Resposta de teste."}

    resposta = consultar_groqcloud("Olá?")
    assert resposta == "Resposta de teste."


def test_erro_consulta_api():
    with patch("src.services.groq_api.requests.post", side_effect=Exception("Erro")):
        resposta = consultar_groqcloud("Olá?")
        assert "Erro ao consultar a API GroqCloud" in resposta