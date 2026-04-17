# Sietch

**Sietch** es un microservicio diseñado para filtrar y organizar noticias de **Hacker News**. El sistema extrae datos de la API de **Algolia**, los limpia y los entrega en un formato optimizado para ser visualizado en una interfaz tipo **Bento Grid** en un sitio web.

## Funcionalidad del Script

```python
import requests
import html

filtro_actual = "ask_hn"
n_news = 10
URL = f"https://hn.algolia.com/api/v1/search?tags={filtro_actual}&hitsPerPage={n_news}"
response = requests.get(URL)
data = response.json()
```

***requests***: Nos permitirá comunicarnos con la API de **Algolia**, la cual utilizaremos en este proyecto para extraer las noticias de **Hacker News**.

***html***: Nos permite limpiar el texto, ya que la respuesta de la API puede venir con formato HTML. Esto facilita ajustarlo posteriormente a nuestras necesidades.

***URL***: Es el endpoint que utilizamos para realizar la petición. Contiene un parámetro llamado `filtro_actual`, con el cual podemos elegir el tipo de respuesta que queremos obtener y tambien el parametro `n_news` que son la cantidad de noticias para mostrar.

***response***: Contiene la respuesta de la petición realizada a la API.

***data***: Convierte la respuesta a formato JSON, que en Python se maneja como un diccionario, facilitando su manipulación.

```python
noticias = data.get('hits', "error")

for i, noticia in enumerate(noticias, 1):
    
    titulo = noticia.get('title')
    autor = noticia.get('author')
    url_externa = noticia.get('url')
    id_noticia = noticia.get('objectID')
    url_debate = f"https://news.ycombinator.com/item?id={id_noticia}"
    texto_sucio = noticia.get('story_text', '')
    
    print(f"{i}. {titulo}")
    print(f"Autor: {autor}")
    
    if url_externa:
        print(f"Noticia: {url_externa}")
        
    print(f"Debate: {url_debate}")
```

***noticias***: Dado que el objeto JSON contiene muchos más datos de los que necesitamos, solo tomamos la clave hits, que es donde vienen las noticias.

**Ciclo** `for`: Recorremos cada elemento de la lista hits, la cual es una lista de diccionarios. Cada diccionario contiene la información de una noticia. Durante el recorrido, vamos extrayendo las claves que nos interesan, como el título, el autor y los enlaces.


```python
    if texto_sucio:
        texto_limpio = html.unescape(texto_sucio)
        texto_limpio = texto_limpio.replace('<p>', '\n').replace('</p>', '')
        
        print(f"Resumen: {texto_limpio[:200]}...")
```
***texto_sucio***: Es una variable que contiene un fragmento (preview) del texto de la noticia. Este contenido incluye formato HTML.

***Proceso de limpieza***: Primero utilizamos html.unescape() para convertir entidades HTML en texto legible. Después, reemplazamos las etiquetas `<p>` por saltos de línea y eliminamos `</p>` para mejorar la presentación.

***texto_limpio***: Es el resultado del texto procesado, listo para mostrarse de forma más clara.

## Códico Actual ##
```python

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
  ```  
