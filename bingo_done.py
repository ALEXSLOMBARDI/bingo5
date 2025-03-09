import random
import tkinter as tk

# Definindo as letras do Bingo
letras = ['B', 'I', 'N', 'G', 'O']

# Criando a tabela de números de 1 a 70
tabela = {letra: list(range(i, i + 15)) for i, letra in zip(range(1, 71, 15), letras)}

# Lista de números sorteados
numeros_sorteados = []

# Função para sortear um número
def sortear_numero():
    numero_sorteado = random.randint(1, 70)
    while numero_sorteado in numeros_sorteados:
        numero_sorteado = random.randint(1, 70)
    numeros_sorteados.append(numero_sorteado)
    return numero_sorteado

# Função para encontrar a letra correspondente
def encontrar_letra(numero):
    for letra, numeros in tabela.items():
        if numero in numeros:
            return letra
    return None

# Função para atualizar a interface
def proximo_numero():
    numero_sorteado = sortear_numero()
    letra_sorteada = encontrar_letra(numero_sorteado)
    numero_grande_label.config(text=f"{letra_sorteada}-{numero_sorteado}", font=("Arial", 48))
    atualizar_tabela()

# Função para atualizar a tabela
def atualizar_tabela():
    for letra in letras:
        for i, numero in enumerate(tabela[letra]):
            if numero in numeros_sorteados:
                labels_tabela[letra][i].config(bg="yellow")

# Função para reiniciar o jogo
def novo_jogo():
    global numeros_sorteados
    numeros_sorteados = []
    numero_grande_label.config(text="Bingo!", font=("Arial", 48))
    for letra in letras:
        for label in labels_tabela[letra]:
            label.config(bg="SystemButtonFace")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Jogo de Bingo")
root.geometry("600x500")

# Frame para o número grande sorteado
numero_grande_frame = tk.Frame(root)
numero_grande_frame.pack(pady=20)

numero_grande_label = tk.Label(numero_grande_frame, text="Bingo!", font=("Arial", 48))
numero_grande_label.pack()

# Frame para a tabela de Bingo
tabela_frame = tk.Frame(root)
tabela_frame.pack(pady=20)

# Criando os labels da tabela
labels_tabela = {letra: [] for letra in letras}

for letra in letras:
    letra_label = tk.Label(tabela_frame, text=letra, font=("Arial", 14, "bold"))
    letra_label.grid(row=0, column=letras.index(letra), padx=10)
    for i, numero in enumerate(tabela[letra]):
        label = tk.Label(tabela_frame, text=str(numero), width=4, height=2, relief="solid", font=("Arial", 12))
        label.grid(row=i + 1, column=letras.index(letra), padx=5, pady=2)
        labels_tabela[letra].append(label)

# Frame para os botões
botoes_frame = tk.Frame(root)
botoes_frame.pack(pady=20)

# Botão "Próximo"
botao_proximo = tk.Button(botoes_frame, text="Próximo", command=proximo_numero, font=("Arial", 14))
botao_proximo.grid(row=0, column=0, padx=10)

# Botão "Novo Jogo"
botao_novo_jogo = tk.Button(botoes_frame, text="Novo Jogo", command=novo_jogo, font=("Arial", 14))
botao_novo_jogo.grid(row=0, column=1, padx=10)

# Iniciar o loop da interface gráfica
root.mainloop()