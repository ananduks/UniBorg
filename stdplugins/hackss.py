"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0,42)

    input_str = event.pattern_match.group(1)

    if input_str == "hackss":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Phone...`",
	    "`Gaining root Access`",
            "`root Access obtained succesfully`",
	    "`accessing kernal`",
	    "`uploading kernal files`",
	    "`Uploading... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Uploading... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Uploading... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Uploading... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Uploading... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Uploading... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Uploading... 84%\n█████████████████████▒▒▒▒ `",
            "`Uploading... 100%\n█████████UPLOADED████████ `",
            "`Kernal modifying...`",
            "`Kernal modifying....`",
	    "`Kernal modifying.....`",
	    "`Kernal modifying......`",
 	    "`Kernal modifying...`",
            "`Kernal modifying....`",
	    "`Kernal modifying.....`",
	    "`Kernal modifying......`",
	    "`Downloading modified kernals..`",
            "`Downloading... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Downloading... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Downloading... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Downloading... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Downloading... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Downloading... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Downloading... 84%\n█████████████████████▒▒▒▒ `",
            "`Downloading... 100%\n████████DOWNLOADED███████ `",
            "`Copying Kernal...`",
            "`Copying Kernal....`",
	    "`Copying Kernal.....`",
	    "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 84%\n█████████████████████▒▒▒▒ `",
            "`Hacking... 100%\n█████████HACKED██████████ `",
            "`Your Phone Storage Have Been Hacked...\n\nPay RS 5000 as Bitcoin: 1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX `"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 42])