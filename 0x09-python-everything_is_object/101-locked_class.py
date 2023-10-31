#!/usr/bin/python3
"""blocked class"""


class LockedClass:
    """prevents from creating new attributes"""

    __slots__ = ['first_name']
