from __future__ import annotations

from .metadata import MetadataError
from .. import _  # (canada fork only): add i18n support


class ResourceError(MetadataError):
    type = "resource-error"
    title = _("Resource Error")
    description = _("A validation cannot be processed.")
    template = _("The data resource has an error: {note}")


class SourceError(ResourceError):
    type = "source-error"
    title = _("Source Error")
    description = _("Data reading error because of not supported or inconsistent contents.")
    template = _("The data source has not supported or has inconsistent contents: {note}")


class SchemeError(ResourceError):
    type = "scheme-error"
    title = _("Scheme Error")
    description = _("Data reading error because of incorrect scheme.")
    template = _("The data source could not be successfully loaded: {note}")


class FormatError(ResourceError):
    type = "format-error"
    title = _("Format Error")
    description = _("Data reading error because of incorrect format.")
    template = _("The data source could not be successfully parsed: {note}")


class EncodingError(ResourceError):
    type = "encoding-error"
    title = _("Encoding Error")
    description = _("Data reading error because of an encoding problem.")
    template = _("The data source could not be successfully decoded: {note}")


class CompressionError(ResourceError):
    type = "compression-error"
    title = _("Compression Error")
    description = _("Data reading error because of a decompression problem.")
    template = _("The data source could not be successfully decompressed: {note}")
