## Mandatory Imports
```python3
None
```
There is None Mandatory Imports. Because Var, bot and command are already automatically imported.

## Explanation
The Mandatory Imports are now automatically imported.

### Formation
Now I will show a short script to show the formation of the desired script.
```python3
from AuraXBot.utils import admin_cmd, sudo_cmd, edit_or_reply as eor
from AuraXBot import CmdHelp

@bot.on(admin_cmd(pattern="Hello$", outgoing=True))
@bot.on(sudo_cmd(pattern="Hello$", allow_sudo=True))
async def Hello_world(event):
    if event.fwd_from:
        return
    await eor(event, "**Hello WORLD**")

CmdHelp("Hello").add_command(
  "Hello", None, "Hello World Edit."
).add
```
