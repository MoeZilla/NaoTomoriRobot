# Copyright (C) 2018 - 2020 MrYacha. All rights reserved. Source code available under the AGPL.
# Copyright (C) 2019 Aiogram
# Copyright (C) 2017 - 2020 Telethon
#
# This file is part of nao(Telegram Bot)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from telethon import TelegramClient

from nao.config import get_str_key, get_int_key

TOKEN = get_str_key("TOKEN", required=True)
NAME = TOKEN.split(':')[0]

tbot = TelegramClient(
    NAME,
    get_int_key("APP_ID", required=True),
    get_str_key("APP_HASH", required=True)
)

# Telethon
tbot.start(bot_token=TOKEN)
