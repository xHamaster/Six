# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from driver.database.dbpunish import is_gbanned_user
from pyrogram import Client, filters
from program.utils.inline import menu_markup, stream_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from config import (
    ASSISTANT_USERNAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
    SUDO_USERS,
    OWNER_ID,
)


@Client.on_callback_query(filters.regex("home_start"))
async def set_start(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("home start")
    await query.edit_message_text(
        f"""𝗪𝗲𝗹𝗰𝗼𝗺𝗲 **[{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
𝗧𝗵𝗶𝘀 𝗶𝘀 𝘁𝗵𝗲 𝗕𝗿𝗼𝗸𝗲𝗻 𝗠𝘂𝘀𝗶𝗰...!
┏━━━━━━━━━━━━━━━━━┓
┣» **ᴏᴘ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ.** 
┣» **ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴍᴜꜱɪᴄ.**
┣» **ᴠɪᴅᴇᴏ ᴘʟᴀʏ ꜱᴜᴘᴘᴏʀᴛᴇᴅ.**
┣» **ᴀᴅᴠᴀɴᴄᴇᴅ ꜰᴇᴀᴛᴜʀᴇꜱ.**
┣» **ꜱᴜᴘᴇʀꜰᴀꜱᴛ ꜱᴘᴇᴇᴅ.**
┗━━━━━━━━━━━━━━━━━┛
**ᴅᴇꜱɪɢɴᴇᴅ ʙʏ : [ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ](https://t.me/PavanMagar)**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Details 📂", callback_data="command_list"),
                ],
                
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("user_guide"))
async def set_guide(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("user guide")
    await query.edit_message_text(
        f"""❓ How to use this Bot ?, read the Guide below !

1.) First, add this bot to your Group.
2.) Then, promote this bot as administrator on the Group also give all permissions except Anonymous admin.
3.) After promoting this bot, type /reload in Group to update the admin data.
3.) Invite @{ASSISTANT_USERNAME} to your group or type /userbotjoin to invite her, unfortunately the userbot will joined by itself when you type `/play (song name)` or `/vplay (song name)`.
4.) Turn on/Start the video chat first before start to play video/music.

`- END, EVERYTHING HAS BEEN SETUP -`

📌 If the userbot not joined to video chat, make sure if the video chat already turned on and the userbot in the chat.

💡 If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="home_start")]]
        ),
    )


@Client.on_callback_query(filters.regex("command_list"))
async def set_commands(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""**ʜᴇʟʟᴏᴡ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

**» ꜰᴏʀ ᴋɴᴏᴡɪɴɢ ᴀ ᴄᴏᴍᴍᴀɴᴅ ʟɪꜱᴛ ᴏꜰ ʙʀᴏᴋᴇɴ ᴊᴜꜱᴛ ᴘʀᴇꜱꜱ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴀɴᴅ ʀᴇᴀᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ᴇxᴘʟᴀɴᴀᴛɪᴏɴ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔙", callback_data="home_start"),
                    InlineKeyboardButton("🎵", callback_data="admin_command"),
                    InlineKeyboardButton("🎥", callback_data="admin_command"),
                    InlineKeyboardButton("👨🏻‍💻", callback_data="admin_command"),
                ],[
                    InlineKeyboardButton("ᴍᴜꜱɪᴄ", callback_data="music_command"),
                    InlineKeyboardButton("ᴠɪᴅᴇᴏ", callback_data="video_command"),
                ],
                [
                    InlineKeyboardButton("ꜱᴇᴀʀᴄʜ", callback_data="search_command"),
                    InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about_command"),
                ],[
                    InlineKeyboardButton("ᴅᴏᴡɴʟᴏᴀᴅ", callback_data="download_command"),
                    InlineKeyboardButton("ᴍᴇɴᴜ", callback_data="menu_command"),
                ],[
                    InlineKeyboardButton("📥 ᴇxᴘᴀɴᴅ ᴍᴇɴᴜ 📥", callback_data="expand_command")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("music_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""✏️ Broken Music Command.

• /play (song name/link) - play music on video chat.

**© @CreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("video_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""✏️ Command list for all user.

• /vplay (video name/link) - play video on video chat
• /vstream (m3u8/yt live link) - play live stream video

**© @CreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("status_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""✏️ Command list for all user.

• /ping - show the bot ping status
• /uptime - show the bot uptime status
• /alive - show the bot alive info (in Group only)

**© @CreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("lyrics_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""✏️ Command list for all user.

• /lyric (query) - scrap the song lyric

**© @CreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("search_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""✏️ Command list for all user.

• /search (query) - search a youtube video link

**© @CreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("download_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""✏️ Command list for all user.

• /song (query) - download song from youtube

**© @CreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("menu_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""✏️ Command list for all user.

• /pause - pause the current track being played
• /resume - play the previously paused track
• /skip - goes to the next track
• /stop - stop playback of the track and clears the queue
• /vmute - mute the streamer userbot on group call
• /vunmute - unmute the streamer userbot on group call
• /volume `1-200` - adjust the volume of music (userbot must be admin)

** © @CreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""✏️ Command list for all user.

» /play (song name/link) - play music on video chat
» /vplay (video name/link) - play video on video chat
» /vstream (m3u8/yt live link) - play live stream video
» /playlist - see the current playing song
» /lyric (query) - scrap the song lyric
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /search (query) - search a youtube video link
» /ping - show the bot ping status
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in Group only)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""✏️ Command list for all user.

» /play (song name/link) - play music on video chat
» /vplay (video name/link) - play video on video chat
» /vstream (m3u8/yt live link) - play live stream video
» /playlist - see the current playing song
» /lyric (query) - scrap the song lyric
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /search (query) - search a youtube video link
» /ping - show the bot ping status
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in Group only)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("user_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""✏️ Command list for all user.

» /play (song name/link) - play music on video chat
» /vplay (video name/link) - play video on video chat
» /vstream (m3u8/yt live link) - play live stream video
» /playlist - see the current playing song
» /lyric (query) - scrap the song lyric
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /search (query) - search a youtube video link
» /ping - show the bot ping status
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in Group only)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("admin_command"))
async def set_admin(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""✏️ Command list for group admin.

• /pause - pause the current track being played
• /resume - play the previously paused track
• /skip - goes to the next track
• /stop - stop playback of the track and clears the queue
• /vmute - mute the streamer userbot on group call
• /vunmute - unmute the streamer userbot on group call
• /volume `1-200` - adjust the volume of music (userbot must be admin)
• /reload - reload bot and refresh the admin data
• /userbotjoin - invite the userbot to join group
• /userbotleave - order userbot to leave from group

**© @CreatorPavan**""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("expand_command"))
async def set_user(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""**ʜᴇʟʟᴏᴡ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

**» ꜰᴏʀ ᴋɴᴏᴡɪɴɢ ᴀ ᴄᴏᴍᴍᴀɴᴅ ʟɪꜱᴛ ᴏꜰ ʙʀᴏᴋᴇɴ ᴊᴜꜱᴛ ᴘʀᴇꜱꜱ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴀɴᴅ ʀᴇᴀᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ᴇxᴘʟᴀɴᴀᴛɪᴏɴ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴍᴜꜱɪᴄ", callback_data="music_command"),
                    InlineKeyboardButton("ᴠɪᴅᴇᴏ", callback_data="video_command"),
                ],[
                    InlineKeyboardButton("ꜱᴇᴀʀᴄʜ", callback_data="search_command"),
                    InlineKeyboardButton("ʟʏʀɪᴄꜱ", callback_data="lyrics_command"),
                ],
                [
                    InlineKeyboardButton("ꜱᴛʀᴇᴀᴍ", callback_data="stream_command"),
                    InlineKeyboardButton("ꜱᴛᴀᴛᴜꜱ", callback_data="status_command"),
                ],[
                    InlineKeyboardButton("ᴀᴅᴍɪɴ", callback_data="admin_command"),
                    InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about_command"),
                ],[
                    InlineKeyboardButton("ᴅᴏᴡɴʟᴏᴀᴅ", callback_data="download_command"),
                    InlineKeyboardButton("ᴏᴡɴᴇʀ", callback_data="owner_command"),
                ],[
                    InlineKeyboardButton("ᴍᴇɴᴜ ꜱᴇᴛᴛɪɴɢꜱ", callback_data="menu_command"),
                ],[
                    InlineKeyboardButton("📤 ᴄᴏʟʟᴀᴘꜱᴇ ᴍᴇɴᴜ 📤", callback_data="command_list")
                ],
            ]
        ),
    )

@Client.on_callback_query(filters.regex("sudo_command"))
async def set_sudo(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    if user_id not in SUDO_USERS:
        await query.answer("⚠️ You don't have permissions to click this button\n\n» This button is reserved for sudo members of this bot.", show_alert=True)
        return
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""✏️ Command list for sudo user.

» /stats - get the bot current statistic
» /calls - show you the list of all active group call in database
» /block (`chat_id`) - use this to blacklist any group from using your bot
» /unblock (`chat_id`) - use this to whitelist any group from using your bot
» /blocklist - show you the list of all blacklisted chat
» /speedtest - run the bot server speedtest
» /sysinfo - show the system information
» /eval - execute any code (`developer stuff`)
» /sh - run any command (`developer stuff`)

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("owner_command"))
async def set_owner(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    if user_id not in OWNER_ID:
        await query.answer("⚠️ You don't have permissions to click this button\n\n» This button is reserved for owner of this bot.", show_alert=True)
        return
    await query.answer("owner commands")
    await query.edit_message_text(
        f"""✏️ Command list for bot owner.

» /gban (`username` or `user_id`) - for global banned people, can be used only in group
» /ungban (`username` or `user_id`) - for un-global banned people, can be used only in group
» /update - update your bot to latest version
» /restart - restart your bot directly
» /leaveall - order userbot to leave from all group
» /leavebot (`chat id`) - order bot to leave from the group you specify
» /broadcast (`message`) - send a broadcast message to all groups in bot database
» /broadcast_pin (`message`) - send a broadcast message to all groups in bot database with the chat pin

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="command_list")]]
        ),
    )


@Client.on_callback_query(filters.regex("stream_menu_panel"))
async def set_markup_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("control panel opened")
        await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("stream_home_panel"))
async def set_home_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.answer("control panel closed")
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id)
    await query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex("set_close"))
async def close_menu(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.message.delete()


@Client.on_callback_query(filters.regex("close_panel"))
async def close_panel(_, query: CallbackQuery):
    user_id = query.from_user.id
    if await is_gbanned_user(user_id):
        await query.answer("❗️ You've blocked from using this bot!", show_alert=True)
        return
    await query.message.delete()
