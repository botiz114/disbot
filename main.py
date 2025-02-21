import discord
import asyncio
import os
import logging
from discord.ext import commands
from pymongo import MongoClient

# Настройка логирования
logger = logging.getLogger("bot")
logging.basicConfig(level=logging.INFO)

# Подключение к MongoDB (замени YOUR_CONNECTION_STRING на реальный URI)
cll = MongoClient("YOUR_CONNECTION_STRING")
moderators_db = cll.moderation.moderators  # Коллекция для хранения данных

# Указываем префикс команд и включаем все интенты
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

# Удаляем стандартную команду help
bot.remove_command('help')

@bot.event
async def on_ready():
    print('[SYSTEM]: Бот успешно запущен!')
    logger.info(f"User: {bot.user} (ID {bot.user.id})")
    await bot.tree.sync()  # Синхронизация слэш-команд

# Функция загрузки Cogs (расширений)
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    await load_extensions()
    await bot.start("YOUR_DISCORD_BOT_TOKEN")  # Вставь сюда токен бота

# Запуск бота
asyncio.run(main())

