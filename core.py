from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def sendVideo(text, path, update, button = False):
    if button:
        button = InlineKeyboardButton(text=button[0], url=button[1])
        reply_markup = InlineKeyboardMarkup([[button]])
        await update.message.reply_video(
            video=path,
            caption=text,
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_video(
            video=path,
            caption=text
        )

async def response(update, text, button=False):
    if button:
        keyboard = [
            [InlineKeyboardButton("INICIAR HACKER", web_app={'url': 'https://minesgpt.online/'})]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        if update.message:
            await update.message.reply_text(text, reply_markup=reply_markup)
        elif update.callback_query:
            await update.callback_query.message.reply_text(text, reply_markup=reply_markup)
    else:
        if update.message:
            await update.message.reply_text(text)
        elif update.callback_query:
            await update.callback_query.message.reply_text(text)