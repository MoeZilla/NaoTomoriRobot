# Copyright (C) 2018 - 2020 MrYacha. All rights reserved. Source code available under the AGPL.
# Copyright (C) 2019 Aiogram
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

import sys

import redis as redis_lib

from naoimport log
from nao.config import get_str_key, get_int_key, get_bool_key

if get_bool_key("HEROKU") is True:
    redis = redis_lib.Redis(
        host=get_str_key("REDIS_URI"),
        port=get_str_key("REDIS_PORT"),
        password=get_str_key("REDIS_PASS"),
        decode_responses=True
    )

    bredis = redis_lib.Redis(
        host=get_str_key("REDIS_URI"),
        port=get_str_key("REDIS_PORT"),
        password=get_str_key("REDIS_PASS"),
    )

if get_bool_key("HEROKU") is False:
    redis = redis_lib.StrictRedis(
    host=get_str_key("REDIS_URI"),
    port=get_str_key("REDIS_PORT"),
    db=get_int_key("REDIS_DB_FSM"),
    decode_responses=True
)

    
    bredis = redis_lib.StrictRedis(
    host=get_str_key("REDIS_URI"),
    port=get_str_key("REDIS_PORT"),
    db=get_int_key("REDIS_DB_FSM")
)

try:
    redis.ping()
except redis_lib.ConnectionError:
    sys.exit(log.critical("Can't connect to RedisDB! Exiting..."))
