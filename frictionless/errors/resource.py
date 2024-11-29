from __future__ import annotations

from .metadata import MetadataError
from ..i18n import _  # (canada fork only): add i18n support


class ResourceError(MetadataError):
    type = "resource-error"
    title = property(lambda self: _("Resource Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("A validation cannot be processed."))  # (canada fork only): i18n support
    template = property(lambda self: _("The data resource has an error: {note}"))  # (canada fork only): i18n support


class SourceError(ResourceError):
    type = "source-error"
    title = property(lambda self: _("Source Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Data reading error because of not supported or inconsistent contents."))  # (canada fork only): i18n support
    template = property(lambda self: _("The data source has not supported or has inconsistent contents: {note}"))  # (canada fork only): i18n support


class SchemeError(ResourceError):
    type = "scheme-error"
    title = property(lambda self: _("Scheme Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Data reading error because of incorrect scheme."))  # (canada fork only): i18n support
    template = property(lambda self: _("The data source could not be successfully loaded: {note}"))  # (canada fork only): i18n support


class FormatError(ResourceError):
    type = "format-error"
    title = property(lambda self: _("Format Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Data reading error because of incorrect format."))  # (canada fork only): i18n support
    template = property(lambda self: _("The data source could not be successfully parsed: {note}"))  # (canada fork only): i18n support


class EncodingError(ResourceError):
    type = "encoding-error"
    title = property(lambda self: _("Encoding Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Data reading error because of an encoding problem."))  # (canada fork only): i18n support
    template = property(lambda self: _("The data source could not be successfully decoded: {note}"))  # (canada fork only): i18n support


class CompressionError(ResourceError):
    type = "compression-error"
    title = property(lambda self: _("Compression Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Data reading error because of a decompression problem."))  # (canada fork only): i18n support
    template = property(lambda self: _("The data source could not be successfully decompressed: {note}"))  # (canada fork only): i18n support
