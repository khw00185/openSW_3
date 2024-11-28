from openai import OpenAI
import telegram
import asyncio

client = OpenAI(
    api_key=""
)
messages = "반가워"

async def send():

  token = ""
  bot = telegram.Bot(token = token)
  public_chat_name = '@k201912052test'
  
  message = chatGpt(messages)
  await bot.sendMessage(chat_id=public_chat_name, text= message)
  print(f"Sent message: ", {message})


def chatGpt(message):
  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "친구랑 대화하듯이 말해줘"},
    {"role": "user", "content": message}
  ]
  )
  return completion.choices[0].message

asyncio.run(send())
