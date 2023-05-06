from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import config
import kb

class FSM(StatesGroup):
    good = State()
    weight = State()

bot = Bot(config.TOKEN, parse_mode="HTML")
dp = Dispatcher(bot=bot, storage=MemoryStorage())

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer(config.get_start(message.from_user.username), reply_markup=kb.get_city())
    await message.delete()

@dp.message_handler(text="Москва")
async def msk(message: types.Message):
    await message.answer(text="Выбери товар бля!", reply_markup=kb.get_goods())

@dp.message_handler(text="Санкт-Петербург")
async def spb(message: types.Message):
    await message.answer(text="Выбери товар бля!", reply_markup=kb.get_goods())

@dp.message_handler(text="Гречка бля")
async def grecha(message: types.Message, state: FSMContext):
    await FSM.good.set()
    await state.update_data(good=-1)
    await message.answer(text="Выбери вес бля!", reply_markup=kb.get_weight())

@dp.message_handler(text="Рис бля")
async def ris(message: types.Message, state: FSMContext):
    await FSM.good.set()
    await state.update_data(good=2)
    await message.answer(text="Выбери вес бля!", reply_markup=kb.get_weight())

@dp.message_handler(text="Макароны бля")
async def mac(message: types.Message, state: FSMContext):
    await FSM.good.set()
    await state.update_data(good=5)
    await message.answer(text="Выбери вес бля!", reply_markup=kb.get_weight())

@dp.message_handler(text="1 кг нах", state=FSM.good)
async def one(message: types.Message, state: FSMContext):
    await FSM.weight.set()
    await state.update_data(weight=1)
    await message.answer(text="Выбирай нах способ получения!", reply_markup=kb.get_ship())

@dp.message_handler(text="2 кг нах", state=FSM.good)
async def two(message: types.Message, state: FSMContext):
    await FSM.weight.set()
    await state.update_data(weight=2)
    await message.answer(text="Выбирай нах способ получения!", reply_markup=kb.get_ship())

@dp.message_handler(text="3 кг нах", state=FSM.good)
async def three(message: types.Message, state: FSMContext):
    await FSM.weight.set()
    await state.update_data(weight=3)
    await message.answer(text="Выбирай нах способ получения!", reply_markup=kb.get_ship())

@dp.message_handler(text="Доставка", state=FSM.weight)
async def three(message: types.Message):
    await message.answer(text="Почти готово!", reply_markup=kb.get_pay())

@dp.message_handler(text="ОПЛАТИТЬ!", state=FSM.weight)
async def three(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(text=config.oplata[data["weight"]+data["good"]], reply_markup=kb.get_check())
    await state.finish()

@dp.message_handler(text="Проверить оплату епта")
async def check(message: types.Message):
    await message.answer(text="НИХУЯ НЕТУ БЛЯ, ОТСОСИ!")

@dp.message_handler(text="Контакты")
async def check(message: types.Message):
    await message.answer(text=config.CONTACTS, reply_markup=kb.get_home())

@dp.message_handler(text="НАЗАД", state="*")
async def back(message: types.Message, state: FSMContext):
    cur = await state.get_state()
    if cur != None:
        await state.finish()
    await message.answer(config.get_start(message.from_user.username), reply_markup=kb.get_city())

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)