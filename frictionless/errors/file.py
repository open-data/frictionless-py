from __future__ import annotations

from .data import DataError
from ..i18n import _  # (canada fork only): add i18n support


class FileError(DataError):
    type = "file-error"
    title = _("File Error")
    description = _("There is a file error.")
    template = _("General file error: {note}")
    tags = ["#file"]


class HashCountError(FileError):
    type = "hash-count"
    title = _("Hash Count Error")
    description = _("This error can happen if the data is corrupted.")
    template = _("The data source does not match the expected hash count: {note}")


class ByteCountError(FileError):
    type = "byte-count"
    title = _("Byte Count Error")
    description = _("This error can happen if the data is corrupted.")
    template = _("The data source does not match the expected byte count: {note}")
