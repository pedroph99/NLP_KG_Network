from Grafo.graph import Graph
def on_button_click(button, grafo_var, button2, text, button3):
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

   
    button.update()
def show_graph(grafo_var):
    grafo_var.draw()
    return 
def aplly_filter(grafo, filter):
    get_text = filter.get()
    if get_text != None and get_text != "":
        grafo.filter_graph(get_text)

    return 