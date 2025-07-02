import telegram
from functools import lru_cache
import re
import asyncio
from fastapi import FastAPI, Request

from config import settings, Settings

TOKEN = settings.telegram_bot_token
bot = telegram.Bot(token=TOKEN)
app = FastAPI()

@lru_cache
def get_settings():
    return Settings()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/{}'.format(TOKEN))
async def get_response(request: Request):
    # retrieve the message in JSON and then transform it to Telegram object
    messsage_data = await request.json()
    update = telegram.Update.de_json(messsage_data, bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode('utf-8').decode()
    # for debugging purposes only
    print("got text message :", text)
    # the first time you chat with the bot AKA the welcoming message
    if text == "/start":
        # print the welcoming message
        bot_welcome = """
           Welcome to coolAvatar bot, the bot is using the service from http://avatars.adorable.io/ to generate cool looking avatars based on the name you enter so please enter a name and the bot will reply with an avatar for your name.
           """
        # send the welcoming message
        await bot.sendChatAction(chat_id=chat_id, action="typing")
        await asyncio.sleep(1.5)
        await bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)


    else:
        try:
            # clear the message we got from any non alphabets
            text = re.sub(r"\W", "_", text)
            # create the api link for the avatar based on http://avatars.adorable.io/
            url = "https://api.adorable.io/avatars/285/{}.png".format(text.strip())
            # reply with a photo to the name the user sent,
            # note that you can send photos by url and telegram will fetch it for you
            await bot.sendChatAction(chat_id=chat_id, action="upload_photo")
            await asyncio.sleep(2)
            await bot.sendPhoto(chat_id=chat_id, photo=url, reply_to_message_id=msg_id)
        except Exception:
            # if things went wrong
            await bot.sendMessage(chat_id=chat_id,
                            text="There was a problem in the name you used, please enter different name",
                            reply_to_message_id=msg_id)
    return 'ok'

@app.get('/setwebhook')
async def set_webhook():
   s = await bot.setWebhook('{URL}{HOOK}'.format(URL=settings.base_url, HOOK=TOKEN))
   if s:
       return "webhook setup ok"
   else:
       return "webhook setup failed"
