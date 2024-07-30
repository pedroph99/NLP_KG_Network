import spacy
import os
import sys
import inspect
import pandas as pd
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from teste_spacy import *
class Graph:
    nlp = spacy.load("pt_core_news_lg")
    def __init__(self) -> None:
        self.grafo = pd.DataFrame()
        self.grafo_original = self.generate_graph()
    

    def generate_graph(self):
        segmented_text = multiple_txt()
    
        entidades = []
        relacoes = []
        
        for x in segmented_text:
            entidades.append(get_entities(x))
            relacoes.append(get_relation(x))
            clear_database(entidades, relacoes)

            
            # extract subject
        source = [i[0] for i in entidades]

    # extract object
        target = [i[1] for i in entidades]
        kg_df = pd.DataFrame({'source':source, 'target':target, 'edge':relacoes})
        
        
        return kg_df
    
    def get_graph(self):
        print(self.grafo)
    def filter_graph(self, keyword = None):
        if keyword != None:
            new_graph = self.grafo_original.query(f'source == "{keyword}" or target == "{keyword}" or edge == "{keyword}"')
            print(new_graph)
            self.grafo = new_graph
        else:
            self.grafo = self.grafo_original
 
    def append_graph(self, source, target, edge):
        
        dataframe_cell = {"source": source, "target": target, "edge": edge}
        df2 = self.grafo_original._append(dataframe_cell, ignore_index=True)
  
        self.grafo_original = df2
    def draw(self, filter = None):
        
        if filter != None or self.grafo.empty:
            self.filter_graph(filter)
        print(self.grafo)
        G=nx.from_pandas_edgelist(self.grafo, "source", "target", 
                            edge_attr="edge", create_using=nx.MultiDiGraph())
        plt.figure(figsize=(12,12))

        pos = nx.spring_layout(G)
        edges = nx.get_edge_attributes(G,"edge")
        
        nx.draw_networkx_edge_labels(G, pos, edges)
        nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
        plt.show()

if __name__ == '__main__':
    objeto = Graph()
    objeto.generate_graph()
    #objeto.filter_graph("Q-learning")
    #objeto.get_graph()
    
    objeto.append_graph("algoritmo", "Q-learning", "atualiza")
    objeto.append_graph("algoritmo", "Teste", "atualiza")
    objeto.draw("algoritmo")
        