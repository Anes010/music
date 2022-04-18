
import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters
from .queues import QUEUE, add_to_queue, get_queue, clear_queue, pop_an_item
from .PyTgCalls import skip_current_song, skip_item

# will set it true for functioning of automatic leave

AUTO_LEAVING = getenv("AUTO_LEAVING_ASSISTANT", True)

# Time after which you're assistant account will leave chats automatically.

AUTO_LEAVE_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "1200")
