#!/usr/bin/env python3
"""A practice module on various workings of
Redis DB"""

import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Returns count of methods called in Cache"""
    method_key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapped function implementing counts"""
        self._redis.incr(method_key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Stores history of inputs & outputs to
    lists <:input> & <:output>"""
    method_key = method.__qualname__
    input_data = method_key + ":inputs"
    output_data = method_key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function implementing storage"""
        self._redis.rpush(input_data, str(args))
        output_value = method(self, *args, **kwargs)
        self._redis.rpush(output_data, str(output_value))
        return output_value

    return wrapper


def replay(method: Callable):
    """Displays the history of calls of a particular
    function"""
    method_key = method.__qualname__
    r = redis.Redis()
    input_data = method_key + ":inputs"
    output_data = method_key + ":outputs"
    method_count = r.get(method_key).decode('utf-8')
    print(f'{method_key} was called {method_count} times:')
    input_list = r.lrange(input_data, 0, -1)
    output_list = r.lrange(output_data, 0, -1)
    for key, val in list(zip(input_list, output_list)):
        attr, val = key.decode('utf-8'), val.decode('utf-8')
        print(f'{method_key}(*{attr}) -> {val}')


class Cache:
    """Writing strings to Redis"""

    def __init__(self):
        """Instantiates redis connection"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores value & returns random key"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Gets value & returns original data type from byte"""
        data_value = self._redis.get(key)
        if fn is not None:
            return fn(data_value)
        return data_value

    def get_str(self, data_value: str) -> str:
        """returns string equivalent from byte"""
        return data_value.decode('utf-8')

    def get_int(self, data_value: str) -> int:
        """returns int equivalent from byte"""
        return int(data_value)
