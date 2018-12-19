import webbrowser
import time

idol = ["IU","TY","DD","HEYEHEYEHEHEHEHY"]
base_url = 'https://www.google.com/search?q='

for i in idol:
    webbrowser.open(base_url+i)
    time.sleep(0.3)