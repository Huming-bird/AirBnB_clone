#!/usr/bin/python3
"""This module create a unique FileStorage
instance for your application"""
import models.engine.file_storage as f


storage = f.FileStorage()
storage.reload()
