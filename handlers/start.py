from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

I am Mafia Music Player🇱🇰, an  bot that lets you play music in your Telegram groups.

Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Source", url="https://t.me/MafiaTechX"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👥 Group", url="https://t.me/su_Chats"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/MafiaTechX"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("yts")
    & filters.group
    & ~ filters.edited
)
async def yts(client: Client, message: Message):
    await message.reply_text(
        "🔍 ඔයාට Inline Music Search කරන්න පහල  Yes Button එක Click කරන්න  🙈",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
