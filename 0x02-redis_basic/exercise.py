#!/usr/bin/env python3
""" A script that contains cache class
"""
import uuid
import redis
from typing import Union


class Cache:
    """ A class cache """
    def __init__(self) -> None:
        # creating an instance of Redis client in _redis
        self._redis = redis.Redis()
        # flush the instance using flushdb
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ A store method that taskes data as arg and returns
            a string.
        """
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
