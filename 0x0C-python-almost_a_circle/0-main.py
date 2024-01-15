#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    instance1 = Base()
    print(instance1.id)

    instance2 = Base()
    print(instance2.id)

    instance3 = Base()
    print(instance3.id)

    instance4 = Base(12)
    print(instance4.id)

    instance5 = Base()
    print(instance5.id)

