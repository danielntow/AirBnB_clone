#!/usr/bin/python3
"""
city.py - City class definition
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class - inherits from BaseModel
    """
    state_id = ""
    name = ""
