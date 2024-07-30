import requests as rq
import os
import bs4 as bs

def get_urls():
    try:
        path = os.path.dirname(__file__)

        source_path = os.path.join(path, 'source', 'links.txt')
        
        source_files = open(source_path, 'r')
        
    except:
        return []
    
    new_list = []
    for x in source_files:
        if(x[0].isalpha()):
            new_list.append(x)

    
    return new_list



def get_corpus(url):
    
    html = rq.get(url).content
    corpus = bs.BeautifulSoup(html, 'html.parser')
    p_tags = corpus.find_all('p')
    string = ''
    # Exibir o texto de cada elemento <p>
    for p in p_tags:
        string = string + p.text

    return string
def get_all_corpus():
    links = get_urls()
    for x in links:
        content = get_corpus(x)
        create_file(content)

def create_file(content):
    path = os.path.dirname(__file__)

    source_path = os.path.join(path, 'source', 'texts')
    number  = len(os.listdir(source_path))
    file_name = os.path.join(source_path, f"txt{number+1}.txt")
    with open(file_name, 'w', encoding='utf-8') as file:
    # Escrever o conteúdo no arquivo
        file.write(content)
if __name__ == '__main__':
    
    print(get_all_corpus())