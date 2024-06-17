import os
import json
import hashlib
from flask_caching import Cache
from flask import request


cache_config = {
    "DEBUG": True if os.environ.get("DEBUG", False) else False,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": int(os.environ.get("TIME_CACHE", 300))
}


def make_cache_key():
    data = request.get_json()
    return hashlib.md5(json.dumps(data, sort_keys=True).encode('utf-8')).hexdigest()


cache = Cache(config=cache_config)
