#!/usr/bin/env python3
"""Module implementing an expiring web
cache and tracker"""

import redis
import requests
from typing import Callable
from functools import wraps


def data_counter(method: Callable) -> Callable:
    """Caches response of fetched data & if
    successful increments count key by 1"""

    @wraps(method)
    def wrapper(url) -> str:
        """The wrapper function"""
        r = redis.Redis()
        response = r.get(f'response:{url}')
        if response:
            return response.decode('utf-8')
        res_content = method(url)
        r.incr(f'count:{url}')
        r.setex(f'response:{url}', 10, res_content)
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
    get_page('http://slowwly.robertomurray.co.uk/'
             'delay/2500/url/http://google.co.uk')
