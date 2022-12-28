import telegram
import feedparser
import datetime
import pytz


# Obt�n el token de acceso de tu bot y el ID de chat de tu canal de Telegram
TOKEN = '**'
CHAT_ID = '**'

# Crea una instancia del bot de Telegram utilizando el token de acceso
bot = telegram.Bot(token=TOKEN)

# Define la funci?n que recuperar? y enviar? los ?ltimos art?culos del feed de RSS


def send_rss_feed():
    # Recupera el feed de RSS utilizando feedparser
    feed = feedparser.parse(
        'https://www.tiempodesanjuan.com/rss/pages/home.xml')
    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now(tz=pytz.timezone('America/Argentina/San_Juan'))

    # Obtener el d�a, el mes y la fecha
    # dia = fecha_actual.day
    # mes = fecha_actual.month
    # ano = fecha_actual.year
    hour = fecha_actual.hour
    # Recorre los ?ltimos art?culos del feed
    for entry in feed.entries[:20]:
        # Convertimos las fechas a objetos datetime
        fecha1 = fecha_actual.strftime("%Y-%m-%d")
        # Convertimos el string a un objeto datetime
        fecha2 = datetime.datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
        fecha_hora = datetime.datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
        # Convertimos el objeto datetime a un string con formato "%Y-%m-%d"
        fecha_formateada = fecha2.strftime("%Y-%m-%d")
        fecha1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d")
        fecha2 = datetime.datetime.strptime(fecha_formateada, "%Y-%m-%d")
        # Calculamos la diferencia en d�as entre las dos fechas
        diferencia_dias = fecha1 - fecha2
        if(hour == 20):
            # Env�a el t�tulo y el enlace del art?culo a trav?s del bot de Telegram
            if (diferencia_dias.days == 0):
                if(fecha_hora.hour <= 20 and fecha_hora.hour >= 14):
                    bot.send_message(
                        chat_id=CHAT_ID, text=f"{entry.title}\n{entry.link}")
        elif(hour == 14):
            # Env�a el t?tulo y el enlace del art?culo a trav?s del bot de Telegram
            if (diferencia_dias.days == 0):
                if(fecha_hora.hour <= 14 and fecha_hora.hour >= 8):
                    bot.send_message(
                        chat_id=CHAT_ID, text=f"{entry.title}\n{entry.link}")
        elif(hour == 8):            
            if (diferencia_dias.days <= 1):
                if(fecha_hora.hour <= 8 and fecha_hora.hour >= 20):
                    bot.send_message(
                        chat_id=CHAT_ID, text=f"{entry.title}\n{entry.link}")
        else:
            bot.send_message(
                        chat_id=CHAT_ID, text=f"No hay noticias para mostrar")
            break

send_rss_feed()