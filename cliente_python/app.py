import requests
import urllib3
import tkinter as tk
from tkinter import filedialog

# Desativa avisos de requisições HTTPS não verificadas
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_URL = "https://localhost:44371/Pessoa"

def escolher_arquivo_csv():
    """ Abre uma janela para o usuário selecionar um arquivo CSV. """
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(title="Selecione um arquivo CSV", filetypes=[("Arquivos CSV", "*.csv")])

def fazer_requisicao(url, metodo="GET", **kwargs):
    """ Centraliza as chamadas HTTP para evitar código repetitivo. """
    try:
        response = requests.request(metodo, url, verify=False, **kwargs)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
        return None

def listar_todas_pessoas():
    """ Obtém e exibe todas as pessoas cadastradas. """
    resposta = fazer_requisicao(API_URL)
    if resposta and resposta.ok:
        pessoas = resposta.json()
        if pessoas:
            for pessoa in pessoas:
                print(f"ID: {pessoa.get('id')}, Nome: {pessoa.get('nome')}, Idade: {pessoa.get('idade')}")
        else:
            print("Nenhuma pessoa cadastrada.")

def buscar_pessoa_por_id():
    """ Solicita um ID ao usuário e busca essa pessoa na API. """
    pessoa_id = input("Digite o ID da pessoa: ").strip()
    if not pessoa_id.isdigit():
        print("⚠️ ID inválido. Digite um número.")
        return
    
    resposta = fazer_requisicao(f"{API_URL}/{pessoa_id}")
    if resposta and resposta.ok:
        dados = resposta.json()
        print(f"\n🔹 Pessoa Encontrada 🔹\n🆔 ID: {dados.get('id')}\n👤 Nome: {dados.get('nome')}\n🎂 Idade: {dados.get('idade')} anos\n🏷️ Categoria: {categorizar_idade(dados.get('idade', 0))}\n" + "-" * 30)

def categorizar_idade(idade):
    """ Retorna a categoria da idade. """
    return "Jovem" if idade < 30 else "Adulto" if 30 <= idade <= 40 else "Sênior"

def cadastrar_pessoas_via_csv():
    """ Permite ao usuário escolher um arquivo CSV e enviá-lo para a API. """
    arquivo_csv = escolher_arquivo_csv()
    if not arquivo_csv:
        print("⚠ Nenhum arquivo selecionado.")
        return
    
    try:
        with open(arquivo_csv, "rb") as file:
            resposta = fazer_requisicao(f"{API_URL}/importar-csv", metodo="POST", data=file, headers={"Content-Type": "text/csv"})

        if resposta and resposta.ok:
            print("✅ Arquivo enviado com sucesso!")
        else:
            print("❌ Erro ao enviar o arquivo.")

    except Exception as e:
        print(f"❌ Erro ao processar o arquivo: {e}")

def menu():
    """ Exibe o menu de opções e chama a função correspondente. """
    opcoes = {
        "1": buscar_pessoa_por_id,
        "2": listar_todas_pessoas,
        "3": cadastrar_pessoas_via_csv
    }

    while True:
        print("\n📌 Sistema de Gestão de Pessoas")
        print("1️⃣ Buscar pessoa por ID")
        print("2️⃣ Listar todas as pessoas")
        print("3️⃣ Cadastrar pessoas via CSV")
        print("0️⃣ Sair")

        opcao = input("Escolha uma opção: ").strip()
        if opcao == "0":
            print("Saindo...")
            break
        opcoes.get(opcao, lambda: print("Opção inválida, tente novamente."))()

if __name__ == "__main__":
    menu()