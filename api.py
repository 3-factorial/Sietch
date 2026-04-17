import requests
import html
"""
filtros:
front_page = Lo más relevante
show_hn = Proyectos y herramientas creadas por la comunidad
ask_hn  = Preguntas y debates 

"""
filtro_actual = "front_page"
n_news=10
URL = f"https://hn.algolia.com/api/v1/search?tags={filtro_actual}&hitsPerPage={n_news}"
response = requests.get(URL)

#Diccionario con toda la informacion
data = response.json()

#Nos enfocamos en las noticias
noticias = data.get('hits', "error")



for i, noticia in enumerate(noticias, 1):
    
    titulo = noticia.get('title')
    autor = noticia.get('author')
    url_externa = noticia.get('url')
    id_noticia = noticia.get('objectID')
    url_debate = f"https://news.ycombinator.com/item?id={id_noticia}"
    texto_sucio = noticia.get('story_text', '')
    print(f"{i}. {titulo}")
    print(f"autor: {autor}")
    if url_externa:
        print(f"Noticia: {url_externa}")
        
    print(f"Debate:  {url_debate}")


    if texto_sucio:
        texto_limpio = html.unescape(texto_sucio)
        texto_limpio = texto_limpio.replace('<p>', '\n').replace('</p>', '')
        
        print(f"Resumen: {texto_limpio[:200]}...") 
    print("-" * 30)
