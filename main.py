import os
import sys
import traceback
import textwrap
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from telegram.error import NetworkError

from agent.setup_agent import agent

load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👩‍🌾 Olá! Sou seu assistente técnico da fazenda. Pergunte o que quiser sobre gado, lavoura, clima ou manejo."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_input = update.message.text
        user_id = str(update.message.from_user.id)

        print(f"📥 Pergunta de {user_id}: {user_input}")

        response = agent.run(user_input, user_id=user_id)
        reply_text = response.content.strip()

        if not reply_text:
            await update.message.reply_text("⚠️ Resposta vazia. Tente novamente.")
            return

        print(f"📤 Resposta do bot: {reply_text[:200]}{'...' if len(reply_text) > 200 else ''}")

        # Break reply into chunks of up to 4096 chars, preserving formatting
        chunks = textwrap.wrap(
            reply_text, width=4096, break_long_words=False, replace_whitespace=False
        )

        for chunk in chunks:
            await update.message.reply_text(chunk)

    except Exception as e:
        error_msg = "❌ Ocorreu um erro processando sua mensagem. Tente novamente mais tarde."
        await update.message.reply_text(error_msg)
        print("🔥 Erro em handle_message():")
        traceback.print_exc()

def main():
    try:
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        if not token:
            print("❌ TELEGRAM_BOT_TOKEN não encontrado no .env")
            sys.exit(1)

        app = ApplicationBuilder().token(token).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

        print("✅ Bot online e aguardando mensagens...")
        print("🔑 Token (preview):", token[:10], "...")
        app.run_polling(drop_pending_updates=True)

    except KeyboardInterrupt:
        print("\n👋 Bot encerrado pelo usuário.")
    except NetworkError:
        print("❌ Erro de rede durante polling do Telegram:")
        traceback.print_exc()
    except Exception:
        print("❌ Erro inesperado:")
        traceback.print_exc()

if __name__ == "__main__":
    main()
