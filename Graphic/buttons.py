from Grafo.graph import Graph
import customtkinter as ctk
def on_button_click(button, grafo_var, button2, text, button3, button4):
    print("Testeee")
    print(button)
    button.configure(text= "Retornar padrão")
    grafo_var = Graph()
    print(grafo_var.grafo_original)
    button2.configure(command =lambda  grafo = grafo_var :  show_graph(grafo)) 
    button2.pack()
    text.pack()
    button3.pack()
    button3.configure(command =lambda  grafo = grafo_var, filtro = text :  aplly_filter(grafo, filtro)) 
    button4.pack()
    button4.configure(command =lambda  grafo = grafo_var :  cria_janela_add(grafo)) 

   
    button.update()
def show_graph(grafo_var):
    grafo_var.draw()
    return 
def aplly_filter(grafo, filter):
    get_text = filter.get()
    if get_text != None and get_text != "":
        grafo.filter_graph(get_text)

    return

def cria_janela_add(grafo):
        def acao_botao():
             print(texto1.get())
             grafo.append_graph(texto1.get(), texto2.get(), texto3.get())
    # Cria a janela principal
        print('ok')
        janela = ctk.CTk()
        janela.title("Adiciona relação")
        janela.geometry("400x300")

        # Cria três TextInputs
        texto1 = ctk.CTkEntry(janela, placeholder_text="Texto 1")
        texto1.pack(pady=10)

        texto2 = ctk.CTkEntry(janela, placeholder_text="Texto 2")
        texto2.pack(pady=10)

        texto3 = ctk.CTkEntry(janela, placeholder_text="Texto 3")
        texto3.pack(pady=10)

        # Cria um botão
        botao = ctk.CTkButton(janela, text="Clique Aqui", command=lambda source=texto1.get(), target= texto2.get(), edge=texto3.get(): acao_botao())
        botao.pack(pady=20)

        # Inicia o loop da interface gráfica
        janela.mainloop()

