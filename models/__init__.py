#!/usr/bin/python3
from models.engine.file_storage import FileStorage


if __name__ != "__main__":
    storage = FileStorage()
    storage.reload()
