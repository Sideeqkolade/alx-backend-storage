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

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """ Retrieves a value from a Redis data storage
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """ Retrieves a string value from a Redis data storage
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """ Retrieves an integer value from a Redis data storage
        """
        return self.get(key, lambda x: int(x))
