from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "7945875447:AAGcHury3N2B6loTPaQVEOuMoE3DYiZyS_4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 Ganhar Dinheiro Online", callback_data='ganhar_dinheiro')],
        [InlineKeyboardButton("🔥 Emagrecimento", callback_data='emagrecimento')],
        [InlineKeyboardButton("💅 Beleza / Estética", callback_data='beleza')],
        [InlineKeyboardButton("🧠 Ansiedade / Saúde Mental", callback_data='ansiedade')],
        [InlineKeyboardButton("💘 Relacionamentos", callback_data='relacionamentos')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Escolha um nicho para ver um produto recomendado:', reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    produtos = {
        'ganhar_dinheiro': '💰 *Produto de Ganhar Dinheiro*\n👉 https://hotmart.com/link-ganhar',
        'emagrecimento': '🔥 *Produto de Emagrecimento*\n👉 https://kiwify.com/link-emagrecer',
        'beleza': '💅 *Produto de Beleza e Estética*\n👉 https://monetizze.com/link-beleza',
        'ansiedade': '🧠 *Produto para Ansiedade e Saúde Mental*\n👉 https://eduzz.com/link-ansiedade',
        'relacionamentos': '💘 *Produto de Relacionamentos*\n👉 https://hotmart.com/link-amor',
    }

    texto = produtos.get(query.data, "Produto não encontrado.")
    await query.edit_message_text(texto, parse_mode='Markdown')

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == '__main__':
    main()
