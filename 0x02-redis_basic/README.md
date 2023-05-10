# 0x02 - Redis Basic

## Resources:books:
Read or watch:
* [Redis Commands](https://redis.io/commands/)
* [Redis Python Client](https://redis-py.readthedocs.io/en/stable/)
* [How to Use Redis with Python](https://realpython.com/python-redis/)
* [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

---

## Learning Objectives:bulb:
What you should learn from this project:

* Learn how to use redis for basic operations
* Learn how to use redis as a simple cache

---

## Install Redis on Ubuntu 20.04
```shell
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

---

## Author
* **Raymond Lukwago A.R** - [lukwagoraymond](https://github.com/lukwagoraymond)