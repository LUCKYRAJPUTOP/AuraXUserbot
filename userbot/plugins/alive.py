from userbot import *
from AuraXBot.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

#-------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "AuraX User"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

AuraX = bot.uid

PM_IMG = "https://telegra.ph/file/62b6e6a1bb6ed711401ce.jpg"
pm_caption = "**⚡Äµråxßð† ɨs օռʟɨռɛ⚡**\n\n"

pm_caption += (
    f"               🅼🅰🆂🆃🅴🆁\n**『 [{DEFAULTUSER}](tg://user?id={AuraX}) 』**\n\n"
)

pm_caption += f"⚡TELETHON⚡ : `{version.__version__}` \n"

pm_caption += f"⚡Äµråxßð†⚡       : __**{AuraXversion}**__\n"

pm_caption += f"⚡Sudo⚡            : `{sudou}`\n"

pm_caption += "⚡CHANNEL⚡  : [ᴊᴏɪɴ](https://t.me/AuraXUserbot)\n"

pm_caption += "⚡CREATOR⚡    : [Nub Here](https://t.me/AuraX_Owner)\n\n"

pm_caption += "[✨REPO✨](https://github.com/AuraXNetwork/AuraXBot) 🔹 [📜License📜](https://github.com/AuraXNetwork/AuraXBot/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'aurax', None, 'Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg'
).add_info(
  'Zinda Hai Kya Bro?'
).add()
