"""

███╗░░░███╗░█████╗░░██████╗████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗██████╗░░░░░░░██╗░░░██╗██████╗░████████╗██╗░░██╗
████╗░████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗░░░░░░██║░░░██║██╔══██╗╚══██╔══╝╚██╗██╔╝
██╔████╔██║███████║╚█████╗░░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║██║░░██║█████╗╚██╗░██╔╝██████╔╝░░░██║░░░░╚███╔╝░
██║╚██╔╝██║██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██║░░██║╚════╝░╚████╔╝░██╔══██╗░░░██║░░░░██╔██╗░
██║░╚═╝░██║██║░░██║██████╔╝░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██████╔╝░░░░░░░░╚██╔╝░░██║░░██║░░░██║░░░██╔╝╚██╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═════╝░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

"""

from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["youtubelink"]), group=-2)
async def love(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⭕ @TellyFun ⭕", url="https://t.me/+VLVXL_BjK5dge1iW")],
        [InlineKeyboardButton("⭕ @HindiWebNetwork ⭕", url="https://t.me/+ffu_vfyIiU01NTZl")],
        [InlineKeyboardButton("⭕ BotsList ⭕", url="https://t.me/joinchat/t1ko_FOJxhFiOThl")],
        [InlineKeyboardButton("⭕ Leech & Mirror ⭕", url="https://t.me/+N9Pi9xjYX6E3YmE9")],
        [InlineKeyboardButton("⭕ Movies & Demand ⭕", url="https://t.me/+jD86CLZqqUBjZDk1")]
    ])
    youtube_ex = "\x1f**Some example youtube channels and songs if you don't know then what u want**\x1f- type /github if I helped u in AnyWay. \x1f```Pʀᴇᴅ∆ᴛᴏʀ``` "


       

    await message.reply_text(youtube_ex, reply_markup=joinButton)
    raise StopPropagation






