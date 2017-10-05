from google import search
from IPython.core.display import HTML

html=""
for url in search("FF15", num=10, stop=10, tpe="vid"):
    if "?v=" in url:
        id=ur.split("?v=")[1]
        html+='<iframe src="//www.youtube.com/embed/{}" width="560" height="315" frameborder="0" allowfullscreen></iframe>'.format(id)
HTML(html)
