#!/usr/bin/env python3
"""Module implementing an expiring web
cache and tracker"""

import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()


def data_counter(method: Callable) -> Callable:
    """Caches response of fetched data & if
    successful increments count key by 1"""

    @wraps(method)
    def wrapper(url):
        """The wrapper function"""
        response = r.get(f'response:{url}')
        if response:
            return response.decode('utf-8')
        res_content = method(url)
        r.incr(f'count:{url}')
        r.set(f'response:{url}', res_content, ex=10)
        r.expire(f'response:{url}', 10)
        return res_content

    return wrapper


@data_counter
def get_page(url: str) -> str:
    """returns the number of times
    a particular URL is accessed in the
    key count: {url}"""
    res = requests.get(url)
    return res.text


if __name__ == "__main__":
    get_page('http://google.co.uk/')
