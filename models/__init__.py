#!/usr/bin/python3

"""Imports a modeule."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
classes = {"BaseModel": BaseModel}

storage.reload()
