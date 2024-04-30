from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Bot tokeningizni bu yerga kiriting
TOKEN = '6700360878:AAEba-rL5reaYhcl8BJ2M_ddjUUxUZImI5c'

def remove_user(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        try:
            # Yangi qo'shilgan foydalanuvchini guruhdan o'chirish
            context.bot.kick_chat_member(chat_id=update.message.chat.id, user_id=member.id)
            # Xabar berish uchun, bu qismni izohdan chiqarib olishingiz mumkin
            # update.message.reply_text(f"{member.full_name} guruhdan o'chirildi.")
        except Exception as e:
            print(f"Xato: {e}")

def main():
    updater = Updater('6700360878:AAEba-rL5reaYhcl8BJ2M_ddjUUxUZImI5c', use_context=True)
    dp = updater.dispatcher

    # Yangi a'zolar qo'shilganda ishga tushadigan handler
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, remove_user))

    # Botni ishga tushirish
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
