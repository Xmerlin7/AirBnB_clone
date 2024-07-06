#!/usr/bin/python3
""" Intialize the package """

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()