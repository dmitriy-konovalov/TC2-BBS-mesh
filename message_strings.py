"""
This file contains all the string literals used in the BBS system.
"""

# General messages
HELP_COMMAND = "Type 'HELP' for a list of commands."
NO_FORTUNES = "No fortunes available."
ERROR_GENERATING_FORTUNE = "Error generating fortune: {}"

# Bulletin board messages
SELECT_BULLETIN_NUMBER = "Select a bulletin number to view from {}:"
BULLETIN_ITEM = "[{}] {}"
NO_BULLETINS = "No bulletins in {}."
NO_PERMISSION = "You don't have permission to post to this board."
BULLETIN_SUBJECT_PROMPT = "What is the subject of your bulletin? Keep it short."
BULLETIN_DISPLAY = "From: {}\nDate: {}\nSubject: {}\n- - - - - - -\n{}"
BULLETIN_CONTENT_PROMPT = "Send the contents of your bulletin. Send a message with END when finished."
NODE_INFO_ERROR = "Error: Unable to retrieve your node information."
BULLETIN_POSTED = "Your bulletin '{}' has been posted to {}.\n(╯°□°)╯📄📌[{}]"

# Mail messages
MAIL_MESSAGES_COUNT = "You have {} mail messages. Select a message number to read:"
MAIL_ITEM = "-{}-\nDate: {}\nFrom: {}\nSubject: {}"
NO_MAIL_MESSAGES = "There are no messages in your mailbox.📭"
RECIPIENT_SHORT_NAME_PROMPT = "What is the Short Name of the node you want to leave a message for?"
MAIL_DISPLAY = "Date: {}\nFrom: {}\nSubject: {}\n{}"
MAIL_ACTION_PROMPT = "What would you like to do with this message?\n[K]eep  [D]elete  [R]eply"
MAIL_NOT_FOUND = "Mail not found"
NODE_NOT_FOUND = "I'm unable to find that node in my database."
MAIL_SUBJECT_PROMPT = "What is the subject of your message to {}?\nKeep it short."
MULTIPLE_NODES = "There are multiple nodes with that short name. Which one would you like to leave a message for?"
NODE_OPTION = "[{}] {}"
MAIL_DELETED = "The message has been deleted 🗑️"
MAIL_REPLY_PROMPT = "Send your reply to {} now, followed by a message with END"
MAIL_KEPT = "The message has been kept in your inbox.✉️"
MAIL_CONTENT_PROMPT = "Send your message. You can send it in multiple messages if it's too long for one.\nSend a single message with END when you're done"
MAIL_SENT = "Mail has been posted to the mailbox of {}.\n(╯°□°)╯📨📬"
NEW_MAIL_NOTIFICATION = "You have a new mail message from {}. Check your mailbox by responding to this message with CM."
SEND_ANOTHER_COMMAND = "Okay, feel free to send another command."

# Menu items
MAIL_MENU = "✉️Mail Menu✉️\nWhat would you like to do with mail?\n[R]ead  [S]end E[X]IT"
BULLETIN_MENU = "📰Bulletin Menu📰\nWhich board would you like to enter?\n[G]eneral  [I]nfo  [N]ews  [U]rgent"
STATS_MENU = "📊Stats Menu📊\nWhat stats would you like to view?\n[N]odes  [H]ardware  [R]oles  E[X]IT"
CHANNEL_DIR_MENU = "📚CHANNEL DIRECTORY📚\nWhat would you like to do?\n[V]iew  [P]ost  E[X]IT"
BOARD_STATS = "{} has {} messages.\n[R]ead  [P]ost"
QUICK_COMMANDS_HELP = "✈️QUICK COMMANDS✈️\nSend command below for usage info:\nSM,, - Send Mail\nCM - Check Mail\nPB,, - Post Bulletin\nCB,, - Check Bulletins\n"

# Quick command help
SEND_MAIL_FORMAT = "Send Mail Quick Command format:\nSM,,{short_name},,{subject},,{message}"
CHECK_MAIL_NO_MESSAGES = "You have no new messages."
CHECK_MAIL_MESSAGES = "📬 You have the following messages:\n"
MAIL_NUMBER_PROMPT = "\nPlease reply with the number of the message you want to read."
INVALID_MESSAGE_NUMBER = "Invalid message number. Please try again."
ERROR_PROCESSING_COMMAND = "Error processing {} command."

# Channel directory
POST_BULLETIN_FORMAT = "Post Bulletin Quick Command format:\nPB,,{board_name},,{subject},,{content}"
CHECK_BULLETINS_FORMAT = "Check Bulletins Quick Command format:\nCB,,board_name"
NO_BULLETINS_AVAILABLE = "No bulletins available on {} board."
BULLETINS_ON_BOARD = "📰 Bulletins on {} board:\n"
BULLETIN_LIST_ITEM = "[{:02d}] Subject: {}, From: {}, Date: {}\n"
BULLETIN_NUMBER_PROMPT = "\nPlease reply with the number of the bulletin you want to read."
INVALID_BULLETIN_NUMBER = "Invalid bulletin number. Please try again."
CHANNEL_POST_FORMAT = "Post Channel Quick Command format:\nCHP,,{channel_name},,{channel_url}"
CHANNEL_ADDED = "Channel '{}' has been added to the directory."
NO_CHANNELS = "No channels available in the directory."
AVAILABLE_CHANNELS = "Available Channels:\n"
CHANNEL_LIST_ITEM = "{:02d}. Name: {}\n"
CHANNEL_NUMBER_PROMPT = "\nPlease reply with the number of the channel you want to view."
INVALID_CHANNEL_NUMBER = "Invalid channel number. Please try again."
CHANNEL_DISPLAY = "Channel Name: {}\nChannel URL: {}"
CHANNEL_NAME_PROMPT = "Name your channel for the directory:"
CHANNEL_URL_PROMPT = "Send a message with your channel URL or PSK:"

# Wall of shame
WALL_OF_SHAME_HEADER = "Devices with battery levels below 20%:\n"
WALL_OF_SHAME_ITEM = "{} - Battery {}%\n"
NO_LOW_BATTERY = "No devices with battery levels below 20% found."

# JS8Call integration
INVALID_OPTION = "Invalid option. Please choose again."
NO_GROUP_MESSAGES = "No group messages available."
NO_STATION_MESSAGES = "No station messages available."
NO_URGENT_MESSAGES = "No urgent messages available."
NO_MESSAGES_FOR_GROUP = "No messages for group {}."
INVALID_GROUP = "Invalid group selection. Please choose again."
