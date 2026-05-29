from django.shortcuts import render
import requests
import html

# Create your views here.



def noticias(request):
    filtro = request.GET.get('filtro', 'ask_hn')
    n_news = int(request.GET.get('n', 16))
    
    URL = f"https://hn.algolia.com/api/v1/search?tags={filtro}&hitsPerPage={n_news}"
    response = requests.get(URL)
    data = response.json()
    lista_noticias = data.get('hits', [])

    for noticia in lista_noticias:
        # URL externa (puede no existir)
        noticia['url_externa'] = noticia.get('url', None)
        
        # URL del debate siempre existe
        id_noticia = noticia.get('objectID')
        noticia['url_debate'] = f"https://news.ycombinator.com/item?id={id_noticia}"
        
        # Texto del resumen (puede no existir)
        texto_sucio = noticia.get('story_text', '') or ''
        if texto_sucio:
            texto_limpio = html.unescape(texto_sucio)
            texto_limpio = texto_limpio.replace('<p>', '\n').replace('</p>', '')
            noticia['texto_limpio'] = texto_limpio[:200]
        else:
            noticia['texto_limpio'] = None

    return render(request, 'hnews.html', {
        'noticias': lista_noticias,
        'filtro_actual': filtro,
    })
