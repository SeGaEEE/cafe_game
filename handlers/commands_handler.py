from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, types
import handlers.messages_handler
from bot_lexicon import replics
router = Router()
@router.message(Command(commands=['start']))
async def command_start(message: Message):
    print("написали старт")
    await message.answer(replics['start'])



@router.message(Command(commands=['help']))
async def command_help(message: Message):
    await message.answer(replics['help'])

@router.message(Command(commands=['stats']))
async def command_statistics(message: Message):
    await message.answer(replics['stats'])
