import telegram
import feedparser
from datetime import datetime, timedelta
import pytz
from config import CHAT_ID, TOKEN

# Crea una instancia del bot de Telegram utilizando el token de acceso
bot = telegram.Bot(token=TOKEN)
# Define la funci?n que recuperar? y enviar? los ?ltimos art?culos del feed de RSS


def send_rss_feed():
    # Recupera el feed de RSS utilizando feedparser
    feed = feedparser.parse(
        'https://www.tiempodesanjuan.com/rss/pages/home.xml')
    # Obtener la fecha actual
    fecha_actual = datetime.now(tz=pytz.timezone('America/Argentina/San_Juan'))    
    fecha_resta = fecha_actual - timedelta(hours=6)
    
    for entry in feed.entries[:20]:
        # Convertimos las fechas a objetos datetime
        fecha_publicadcion = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")        
        if(fecha_resta <=  fecha_publicadcion and fecha_publicadcion <= fecha_actual):
            bot.send_message(
                chat_id=CHAT_ID, text=f"{entry.title}\n{entry.link}")
           
def handler(event, context):
    send_rss_feed()