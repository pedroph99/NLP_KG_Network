import os
import spacy
from spacy import displacy
from spacy.matcher import Matcher
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
nlp = spacy.load("pt_core_news_lg")
def get_spacy():
    nlp = spacy.load("pt_core_news_sm")

# Texto em português para análise
    texto = get_file_corpus(3)

# Processar o texto
    doc = nlp(texto)
# Extrair e imprimir entidades nomeadas
    #for ent in doc.ents:
       # print(ent.text, ent.label_)
def get_file_corpus(number):
    path = os.path.dirname(__file__)
    source_path = os.path.join(path, 'source', 'texts')

    file_name = os.path.join(source_path, f"txt{number}.txt")
    file = open(file_name, 'r', encoding='utf-8')
    texto = file.read()
    return texto
    

def clean_txt(number):
    texto = get_file_corpus(number)
    
    clean_texto = texto.split('.')
    if not clean_texto[-1].isalpha():
       del(clean_texto[-1])
    while "\n" in clean_texto: clean_texto.remove("\n")
    #print(clean_texto)
    return clean_texto

def get_entities(sent):
  ## chunk 1
  ent1 = ""
  ent2 = ""

  prv_tok_dep = ""    # dependency tag of previous token in the sentence
  prv_tok_text = ""   # previous token in the sentence

  prefix = ""
  modifier = ""
  

  #############################################################
  
  for tok in nlp(sent):
    ## chunk 2
    # if token is a punctuation mark then move on to the next token
    if tok.dep_ != "punct" and not tok.is_stop:
      
      #print(f"{tok.text} ||    {tok.dep_},")
      # check: token is a compound word or not
      if tok.dep_ == "compound":
        prefix = tok.text
        # if the previous word was also a 'compound' then add the current word to it
        if prv_tok_dep == "compound":
          prefix = prv_tok_text + " "+ tok.text
      
      # check: token is a modifier or not
      if tok.dep_.endswith("mod") == True:
        modifier = tok.text
        # if the previous word was also a 'compound' then add the current word to it
        if prv_tok_dep == "compound":
          modifier = prv_tok_text + " "+ tok.text
      
      ## chunk 3
      if tok.dep_.find("subj") == True:
        
        ent1 = tok.lemma_
           

      ## chunk 4
      if tok.dep_  == "obj":
      
        ent2 =  tok.lemma_
      elif tok.dep_ == "root":
         ent2 = tok.lemma_
        
        
      ## chunk 5  
      # update variables
      prv_tok_dep = tok.dep_
      prv_tok_text = tok.text
  #############################################################

  #print([ent1.strip(), ent2.strip()])
  return [ent1.strip(), ent2.strip()]

def get_relation(sent):

  doc = nlp(sent)

  # Matcher class object 
  matcher = Matcher(nlp.vocab)

  #define the pattern 
  pattern = [{'DEP':'ROOT'}, 
            {'DEP':'prep','OP':"?"},
            {'DEP':'agent','OP':"?"},  
            {'POS':'ADJ','OP':"?"}] 

  matcher.add("matching_1",[pattern]) 

  matches = matcher(doc)
  k = len(matches) - 1

  span = doc[matches[k][1]:matches[k][2]] 

  return(span.text)


def multiple_txt():
   has = True
   lista_textos = []
   counter = 1
   while has:
      
      try:
        current_text = clean_txt(counter)
        counter+=1
        lista_textos.extend(current_text)
      except:
         has = False
   #print(lista_textos)   
   return lista_textos
         
def clear_database(entidades, relacoes):
   #print(len(entidades))
   #print(len(relacoes))
   #print(entidades)
   #print(relacoes)
   counter = 0
   for x in entidades:
      if x[0] == "" or x[1] =="":
         print(f"{entidades[counter]}, real: {x}")
         del(entidades[counter])
         del(relacoes[counter])
         counter+=1
      else:
         counter+=1
   
    

def gera_grafo():
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
    G=nx.from_pandas_edgelist(kg_df, "source", "target", 
                          edge_attr="edge", create_using=nx.MultiDiGraph())
    plt.figure(figsize=(12,12))

    pos = nx.spring_layout(G)
    edges = nx.get_edge_attributes(G,"edge")
    
    nx.draw_networkx_edge_labels(G, pos, edges)
    nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
    plt.show()
      
       

if __name__ == '__main__':
   
   gera_grafo()
   
    

    
    #displacy.serve(doc, style="dep", port=3000) # port=3000 specifies the port