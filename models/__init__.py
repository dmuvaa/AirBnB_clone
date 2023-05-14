#!/usr/bin/python3

"""Imports a modeule."""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
classes = {"BaseModel": BaseModel}

storage.reload()
