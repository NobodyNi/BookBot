from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def send_answer(message: Message):
    await message.answer(f'не пиши сюда! {message.text}')

