import os
import random
import time
from keep_alive import keep_alive
from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext

print("Funca B)")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"""¡Hola {update.effective_user.first_name}!

Este bot tiene solo tres comandos:
/start	<= Despliega este menú
/memide	<= Te mide el amigo
/acerca	<= Despliega información del bot

Antes de empezar, tené en cuenta que esto no es un clón exacto. Además de los claros comandos con el 'slash', en este bot también hay ligeras modificaciones en las lineas que el bot dice, y como actúa. Eso es todo, ahora podés proseguir. ¡Y suerte titán!""")

def memide(update: Update, context: CallbackContext) -> None:
  update.message.reply_photo(open("imgs/0.jpg", 'rb'), f"Calculando la tula-medida de @{update.effective_user.username}...")
  tula = random.randint(1, 50)
  if tula < 10:
    imagen = "1"
    opinion = "<i>Lamentable...</i>"
  elif tula < 20:
    imagen = "2"
    opinion = "Casi juega..."
  elif tula < 30:
    imagen = "3"
    opinion = "Felicidades!"
  elif tula < 40:
    imagen = "4"
    opinion = "Jugador 😎"
  else:
    imagen = "5"
    opinion = "😳<i>!?</i> <b>Menudo pollón!!!</b>"
  time.sleep(3)
  update.message.reply_photo(open(f"imgs/{imagen}.jpg", 'rb'), f"{opinion} Te mide <b>{tula}cm</b>, @{update.effective_user.username}", reply_to_message_id=True, parse_mode=ParseMode.HTML)

def acerca(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""<b>MemideBot v1.0.0</b>
Hecho por Not4xp

Sí te interesa saber como está hecho este bot por dentro, podés encontrar el código fuente en uq.now.sh/memidebot

Saludos al Jotita
twitch.tv/eljotita""")


updater = Updater(os.getenv("token"))

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('memide', memide))
updater.dispatcher.add_handler(CommandHandler('acerca', acerca))

if os.getenv("keep_alive") == "1": keep_alive()
updater.start_polling()
updater.idle()