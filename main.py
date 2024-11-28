from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, filters
#import json
from core import sendVideo, response

TOKEN_BOT = '7795577887:AAEiKujadZF94J9d3PzIm6gIE_KpqkoE3Nk'
PATH_VIDEO = 'assets/videos/'

async def start_no_register(update, context) -> None:
    text = f"✍🏼 INGRESA TU ID DE CUENTA 1WIN EN EL CHAT:\n\n👇 Si no tienes una cuenta, haz clic en el botón para crear una:\n\n⭐️ UTILIZA EL CÓDIGO PROMOCIONAL PRIVADO PARA OBTENER BONIFICACIÓN DEL 500% Y GIROS GRATIS: MNS24GPT"
    video_path = PATH_VIDEO + 'register.mp4'
    button = ['📎REGISTRO', 'https://bonus-betando.com/registro']
    await sendVideo(text, video_path, update, button)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await start_no_register(update, context)

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = f"💣 Minas\n\n📝 Descripción:\nUn juego en el que debes adivinar las celdas que no tienen minas. Por cada celda abierta ganas dinero.\n\n🤖 Hay un hack bot disponible para este juego, que muestra celdas sin minas."
    await response(update, text, True)

# Configuração do bot
def main():
    app = ApplicationBuilder().token(TOKEN_BOT).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Regex(r"^\d{9}$"), get_id))
    #app.add_handler(CallbackQueryHandler(start_bot, pattern="start_bot"))

    print("Bot está rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()