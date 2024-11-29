from __future__ import annotations

from .data import DataError
from ..i18n import _  # (canada fork only): add i18n support


class FileError(DataError):
    type = "file-error"
    title = property(lambda self: _("File Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("There is a file error."))  # (canada fork only): i18n support
    template = property(lambda self: _("General file error: {note}"))  # (canada fork only): i18n support
    tags = ["#file"]


class HashCountError(FileError):
    type = "hash-count"
    title = property(lambda self: _("Hash Count Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("This error can happen if the data is corrupted."))  # (canada fork only): i18n support
    template = property(lambda self: _("The data source does not match the expected hash count: {note}"))  # (canada fork only): i18n support


class ByteCountError(FileError):
    type = "byte-count"
    title = property(lambda self: _("Byte Count Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("This error can happen if the data is corrupted."))  # (canada fork only): i18n support
    template = property(lambda self: _("The data source does not match the expected byte count: {note}"))  # (canada fork only): i18n support
