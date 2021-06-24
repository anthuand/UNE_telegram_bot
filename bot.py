import logging
from tarifa import calcularTarifa
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,ConversationHandler
import os

PORT = int(os.environ.get('PORT', 5000))
introducir_consumo=1

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = os.getenv('TOKEN')



def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Este bot te ayudará a saber el importe te du tarifa electrica a partir del consumo en Kw!')

def calcular_tarifa(update, context):
    update.message.reply_text('Introduce solo el numero del consumo: \n Ej: 450')
    return introducir_consumo

def received_information(update, context):
    print("estoy dentro de recived")
    text = update.message.text
    print(text)
    tarifa=calcularTarifa(int(text))
    update.message.reply_text("Importe de la tarifa electrica: {} cup".format(tarifa))

    return ConversationHandler.END


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        """ Este bot te ayudara con el pago de tu tarifa electrica,
        lo unico que tienes es que seleccionar el comando /calcular_tarifa e introducir el numero del consumo.
        Como saber el consumo?
        R/ Existen dos vias:
           1- Viendo el contador y restar la lectura actual a la lectura del mes pasado
           2- Revisar el ticket de la empresa electrica , ahi se muestra el consumo
        Espero que este bot sea de tu agrado y que te sea util 😁!!
        """
        )

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('calcular_tarifa', calcular_tarifa)
        ],
        states={
            introducir_consumo: [

                MessageHandler(Filters.text, received_information),
               
            ],

        },
        fallbacks=[],
    ))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://unebot.herokuapp.com/' + TOKEN)

    updater.idle()

if __name__ == '__main__':
    main()


