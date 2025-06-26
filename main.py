import sys
import os

# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
print("sys.path:", sys.path)
print("Current working directory:", os.getcwd())

from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler, filters
from handlers.telegram_handlers import (
    start, choose_platform, choose_action, choose_special_offer, input_cycles,
    choose_pack, input_purchase_requests, input_char_numbers, input_hex_body,
    input_credentials, choose_pack_mode, choose_chest_mode, cancel
)
from handlers.conversation_states import (
    CHOOSING_PLATFORM, CHOOSING_ACTION, CHOOSING_SPECIAL_OFFER, INPUT_CYCLES,
    INPUT_CHAR_NUMBERS, INPUT_HEX_BODY, INPUT_CREDENTIALS, CHOOSING_PACK,
    INPUT_PURCHASE_REQUESTS, CHOOSING_PACK_MODE, CHOOSING_CHEST_MODE
)
from config.constants import TOKEN

def main():
    app = Application.builder().token(TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSING_PLATFORM: [CallbackQueryHandler(choose_platform)],
            CHOOSING_ACTION: [CallbackQueryHandler(choose_action)],
            CHOOSING_SPECIAL_OFFER: [CallbackQueryHandler(choose_special_offer)],
            INPUT_CREDENTIALS: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, input_credentials),
                CallbackQueryHandler(input_credentials),
            ],
            INPUT_HEX_BODY: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, input_hex_body),
                CallbackQueryHandler(input_hex_body),
            ],
            INPUT_CYCLES: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, input_cycles),
                CallbackQueryHandler(input_cycles),
            ],
            INPUT_CHAR_NUMBERS: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, input_char_numbers),
                CallbackQueryHandler(input_char_numbers),
            ],
            CHOOSING_PACK: [CallbackQueryHandler(choose_pack)],
            INPUT_PURCHASE_REQUESTS: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, input_purchase_requests),
                CallbackQueryHandler(input_purchase_requests),
            ],
            CHOOSING_PACK_MODE: [CallbackQueryHandler(choose_pack_mode)],
            CHOOSING_CHEST_MODE: [CallbackQueryHandler(choose_chest_mode)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    app.add_handler(conv_handler)
    app.run_polling()

if __name__ == "__main__":
    main()