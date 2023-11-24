from openai import OpenAI
import telegram
import asyncio

client = OpenAI(
    api_key="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"
)
messages = "반가워"

async def send():

  token = "6802394554:AAEn560wF6oRAx0dtdTiWP24cZd-zBht6vs"
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