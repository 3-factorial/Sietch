import requests
import html

filtro_actual = "ask_hn"

URL = f"https://hn.algolia.com/api/v1/search?tags={filtro_actual}&hitsPerPage=5"

print("Conectando con la api...")
response = requests.get(URL)

data = response.json()

noticias = data.get('hits', [])


for i, noticia in enumerate(noticias, 1):
    titulo = noticia.get('title')
    
    # EXTRACCIÓN DE LINKS
    url_externa = noticia.get('url')
    id_noticia = noticia.get('objectID')
    url_debate = f"https://news.ycombinator.com/item?id={id_noticia}"
    texto_sucio = noticia.get('story_text', '')
    print(f"{i}. {titulo}")
    if url_externa:
        print(f"   🔗 Noticia: {url_externa}")
        
    print(f"   💬 Debate:  {url_debate}")


    if texto_sucio:
        # 1. Traducir entidades (&#x27; -> ')
        texto_limpio = html.unescape(texto_sucio)
        
        # 2. Quitar etiquetas <p> (las cambiamos por un espacio o salto)
        texto_limpio = texto_limpio.replace('<p>', '\n').replace('</p>', '')
        
        print(f"   📝 Resumen: {texto_limpio[:200]}...") # Mostramos solo los primeros 100 caracteres
        print("-" * 30)
    
