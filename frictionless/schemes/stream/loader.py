from __future__ import annotations

import os

from ... import errors, types
from ...exception import FrictionlessException
from ...system import Loader

from ...i18n import _  # (canada fork only): add i18n support


class StreamLoader(Loader):
    """Stream loader implementation."""

    # Read

    def read_byte_stream_create(self):  # type: ignore
        byte_stream = self.resource.data
        if not os.path.isfile(byte_stream.name):  # type: ignore
            note = _("only local streams are supported: {byte_stream}").format(byte_stream=byte_stream)
            raise FrictionlessException(errors.SchemeError(note=note))
        if hasattr(byte_stream, "encoding"):
            try:
                byte_stream = open(byte_stream.name, "rb")  # type: ignore
            except Exception:
                note = _("cannot open a stream in the byte mode: {byte_stream}").format(byte_stream=byte_stream)
                raise FrictionlessException(errors.SchemeError(note=note))
        byte_stream = ReusableByteStream(byte_stream)  # type: ignore
        return byte_stream

    # Write

    def write_byte_stream_save(self, byte_stream: types.IByteStream):
        self.resource.data = byte_stream


# Internal


class ReusableByteStream:
    def __init__(self, byte_stream: types.IByteStream):
        self.__byte_stream = byte_stream

    def __getattr__(self, name: str):
        return getattr(self.__byte_stream, name)

    def read(self, size: int = -1):
        if self.__byte_stream.closed:
            try:
                self.__byte_stream = open(self.__byte_stream.name, "rb")
            except Exception:
                note = _("cannot re-open a byte stream: {byte_stream}").format(byte_stream=self.__byte_stream)
                raise FrictionlessException(errors.SchemeError(note=note))
        return self.__byte_stream.read(size)
