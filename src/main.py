#
# Código principal em loop com opção de saída
#

from services.groq_api import consultar_groqcloud


def main():
    print("🤖 Bem-vindo ao Agente IA - GroqCloud!")
    print("Digite 'sair' para encerrar o programa.\n")

    while True:
        # Entrada do usuário
        pergunta = input("Digite sua pergunta: ")

        # 🚪 Opção para sair do loop
        if pergunta.lower() == 'sair':
            print("Encerrando o programa. Até mais!")
            break

        # Consulta à API GroqCloud e exibição da resposta
        resposta = consultar_groqcloud(pergunta)
        print(f"Resposta da IA: {resposta}\n")


if __name__ == "__main__":
    main()
