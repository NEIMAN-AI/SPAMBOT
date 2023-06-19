from pyrogram.types import InlineKeyboardButton

class Data:

    HELP_MENU1 = [

        [

            InlineKeyboardButton(text="⚜️ banall ⚜️", callback_data="banall"),

            InlineKeyboardButton(text="📍birthday 📍", callback_data="birthday"),

        ],

        [

            InlineKeyboardButton(text="⚜️ Ping ⚜️", callback_data="core_help1"),

            InlineKeyboardButton(text="📍 Restart 📍", callback_data="core_help2"),

        ],

        [

            InlineKeyboardButton(text="⚜️ eval ⚜️", callback_data="evaluators_help1"),

            InlineKeyboardButton(text="📍 exec 📍", callback_data="evaluators_help2"),

        ],

        [

            InlineKeyboardButton(

                text="⚜️ Good Morning ⚜️", callback_data="gwish_help1"

            ),

            InlineKeyboardButton(text="📍Good Afternoon 📍", callback_data="gwish_help2"),

        ],

        [

            InlineKeyboardButton(text="⚜️ Good Night ⚜️", callback_data="gwish_help3"),

        ],

        [

            InlineKeyboardButton(text="⚜️ Raid ⚜️", callback_data="raid_help1"),

            InlineKeyboardButton(text="📍Reply Raid📍", callback_data="raid_help2"),

        ],

        [

            InlineKeyboardButton(text="⚜️ Dreply Raid ⚜️", callback_data="raid_help3"),

            InlineKeyboardButton(text="📍 List Raid 📍", callback_data="raid_help4"),

        ],

        [

            InlineKeyboardButton(text="⚜️ Shayri ⚜️", callback_data="shayri_help1"),

            InlineKeyboardButton(text="📍 Stop 📍", callback_data="shayri_help2"),

        ],

        [

            InlineKeyboardButton(text="⚜️ Spam ⚜️", callback_data="spam_help1"),

            InlineKeyboardButton(text="📍 Delay Spam 📍", callback_data="spam_help2"),

        ],

        [

            InlineKeyboardButton(text="⚜️ Porn Spam ⚜️", callback_data="spam_help3"),

            InlineKeyboardButton(text="📍 Hang Spam 📍", callback_data="spam_help4"),

        ],

        [

            InlineKeyboardButton(text="⚜️ U Spam ⚜️", callback_data="unlimited_help1"),

            InlineKeyboardButton(text="📍 U Raid 📍", callback_data="unlimited_help2"),

        ],

        [

            InlineKeyboardButton(text="⚜️ Abuse ⚜️", callback_data="unlimited_help3"),

            InlineKeyboardButton(text="📍 Stop 📍", callback_data="unlimited_help4"),

        ],

        [

            InlineKeyboardButton(text="⚜️ Echo ⚜️", callback_data="unlimited_help5"),

        ],

        [

            InlineKeyboardButton(text="🔒 Close", callback_data="close"),

        ],

    ]

    REVERT = [

        [

            InlineKeyboardButton("Reopen Help Menu", callback_data="helpmenu1"),

        ],

    ]

    HELP_MENU2 = [

        [

            InlineKeyboardButton(text="🔙 Previous", callback_data="helpmenu1"),

        ],

        [

            InlineKeyboardButton(text="Close ", callback_data="close"),

        ],

        [

            InlineKeyboardButton(text="Next ⏭️", callback_data="helpmenu3"),

        ],

    ]

    HELP_MENU3 = [

        [

            InlineKeyboardButton(text="🔙 Previous", callback_data="helpmenu2"),

        ],

        [

            InlineKeyboardButton(text="Close ", callback_data="close"),

        ],

        [

            InlineKeyboardButton(text="Next ⏭️", callback_data="helpmenu1"),

        ],

    ]
