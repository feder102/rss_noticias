import requests
import feedparser
from datetime import datetime, timedelta
import pytz
from config import CHAT_ID, TOKEN
import tracemalloc

# Crea una instancia del bot de Telegram utilizando el token de acceso

delay = 3
# Define la funci?n que recuperar? y enviar? los ?ltimos art?culos del feed de RSS

def enviar_mensaje(entry):
    fecha_publicadcion = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
    fecha_str = fecha_publicadcion.strftime("%d/%m/%Y")
    message = f"{entry.title}\n{entry.link}\nFecha: {fecha_str}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url).json()

def send_rss_feed():
    # Recupera el feed de RSS utilizando feedparser
    feed = feedparser.parse(
        'https://www.tiempodesanjuan.com/rss/pages/home.xml')
    # Obtener la fecha actual
    fecha_actual = datetime.now(tz=pytz.timezone('America/Argentina/San_Juan'))    
    fecha_resta = fecha_actual - timedelta(hours=delay)
    tracemalloc.start()
    for entry in feed.entries[:20]:
        # Convertimos las fechas a objetos datetime
        fecha_publicacion = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")        
        if(fecha_resta <=  fecha_publicacion and fecha_publicacion <= fecha_actual):            
            enviar_mensaje(entry)            
            #print(f"{entry.title}\n{entry.link}")
    tracemalloc.get_traceback_limit

           
def handler(event, context):    
    send_rss_feed()
handler('',"")