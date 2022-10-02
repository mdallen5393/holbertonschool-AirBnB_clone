#!/usr/bin/python3
""" creates a FileStorage instance"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
