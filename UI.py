import customtkinter as ctk
from functools import partial
from Graphic import buttons

# Cria a janela principal
class GUI:
    root = None
    grafo = None
    button1 = None
    button2 = None
    button3 = None
    def __init__(self) -> None:
        self.root = self.gera_janela()
        self.grafo = "Teste"
        self.button1 = None
        self.button2 = None
        self.button3 = None
        
    def gera_janela(self):

        root = ctk.CTk()
        root.title("Knoledge Graphs")
        root.geometry("400x300")
        root.resizable(False, False)
        # Cria um frame para centralizar o conteúdo
        frame = ctk.CTkFrame(root, corner_radius=10)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Título
        title_label = ctk.CTkLabel(frame, text="Knoledge")
        title_label.pack(pady=20)
        self.gera_botoes(frame)
        # Botões
        
        return root

        # Executa a aplicação
    def gera_botoes(self, frame):
        print(self.button1)
        self.button1 = ctk.CTkButton(frame, text="Gerar Grafo")
        self.button2 = ctk.CTkButton(frame, text="Ver grafo", command=buttons.on_button_click)
        entrada = ctk.CTkEntry(frame, width=250)
        self.button3 = ctk.CTkButton(frame, text="Aplicar filtro")
        
        self.button1.configure(command =lambda botao=self.button1, grafo = self.grafo, botao2 = self.button2, entrada = entrada, botao3 =self.button3  :  
                               buttons.on_button_click(botao, grafo, botao2, entrada, botao3))
        
        

          
        self.button1.pack(pady=10)

       
        #self.button2.configure(command =lambda  grafo = self.grafo :  buttons.show_graph(grafo)) 
    
        #self.button2.pack(pady=10)
    
        
        #entrada.pack(pady=20)
        #self.button3.pack(pady=10)
    def loop(self):
        self.root.mainloop()
def main():
    gui = GUI()

    gui.loop()


if __name__ == '__main__':
    main()