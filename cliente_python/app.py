import requests
import urllib3
import tkinter as tk
from tkinter import filedialog
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_URL = "https://localhost:44371/Pessoa"

def escolher_arquivo_csv():
    """
    Abre uma janela para o usuário selecionar um arquivo CSV.
    Retorna o caminho do arquivo selecionado ou None se o usuário cancelar.
    """
    root = tk.Tk()
    root.withdraw()
    arquivo_path = filedialog.askopenfilename(
        title="Selecione um arquivo CSV",
        filetypes=[("Arquivos CSV", "*.csv")],
    )
    return arquivo_path

def listar_todas_pessoas():
    """ Faz uma requisição para obter todas as pessoas cadastradas """
    try:
        resposta = requests.get(API_URL, verify=False)
        resposta.raise_for_status()

        pessoas = resposta.json()
        if not pessoas:
            print("Nenhuma pessoa cadastrada.")
            return
        
        for pessoa in pessoas:
            print(f"ID: {pessoa.get('id')}, Nome: {pessoa.get('nome')}, Idade: {pessoa.get('idade')}")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao buscar as pessoas: {e}")

def buscar_pessoa_por_id():
    """ Solicita um ID ao usuário e busca essa pessoa na API """
    pessoa_id = input("Digite o ID da pessoa: ").strip()
    if not pessoa_id.isdigit():
        print("⚠️ ID inválido. Digite um número.")
        return
    
    url = f"{API_URL}/{pessoa_id}"

    try:
        resposta = requests.get(url, verify=False)
        resposta.raise_for_status()

        dados = resposta.json()
        categoria = categorizar_idade(dados.get("idade", 0))
        
        print("\n🔹 Pessoa Encontrada 🔹")
        print(f"🆔 ID: {dados.get('id')}")
        print(f"👤 Nome: {dados.get('nome')}")
        print(f"🎂 Idade: {dados.get('idade')} anos")
        print(f"🏷️ Categoria: {categoria}")
        print("-" * 30)

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao buscar pessoa: {e}")

def categorizar_idade(idade):
    """ Categoriza a idade da pessoa """
    if idade < 30:
        return "Jovem"
    elif 30 <= idade <= 40:
        return "Adulto"
    else:
        return "Sênior"

def cadastrar_pessoas_via_csv():
    """
    Permite ao usuário escolher um arquivo CSV e envia-o no body da requisição para a API .NET.
    """
    arquivo_csv = escolher_arquivo_csv()
    
    if not arquivo_csv:
        print("⚠ Nenhum arquivo selecionado.")
        return
    
    try:
        with open(arquivo_csv, "rb") as file:
            headers = {"Content-Type": "text/csv"}
            response = requests.post(API_URL+"/importar-csv", data=file, headers=headers, verify=False)

        print("🔹 Status Code:", response.status_code)
        print("🔹 Resposta da API:", response.text)

        if response.status_code == 200 or response.status_code == 201:
            print("✅ Arquivo enviado com sucesso!")
        else:
            print("❌ Erro ao enviar o arquivo.")

    except Exception as e:
        print(f"❌ Erro ao processar o arquivo: {e}")

def menu():
    """ Exibe o menu de opções """
    while True:
        print("\n📌 Sistema de Gestão de Pessoas")
        print("1️⃣ Buscar pessoa por ID")
        print("2️⃣ Listar todas as pessoas")
        print("3️⃣ Cadastrar pessoas via CSV")
        print("0️⃣ Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            buscar_pessoa_por_id()
        elif opcao == "2":
            listar_todas_pessoas()
        elif opcao == "3":
            cadastrar_pessoas_via_csv()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
