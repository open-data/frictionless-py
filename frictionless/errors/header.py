from __future__ import annotations

from typing import List

import attrs

from .table import TableError
from ..i18n import _  # (canada fork only): add i18n support


@attrs.define(kw_only=True, repr=False)
class HeaderError(TableError):
    """Header error representation.

    A base class for all the errors related to the resource header.
    """

    type = "header-error"
    title = property(lambda self: _("Header Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Cell Error"))  # (canada fork only): i18n support
    template = property(lambda self: _("Cell Error"))  # (canada fork only): i18n support
    tags = ["#table", "#header"]

    labels: List[str]
    """
    List of labels that has errors.
    """

    row_numbers: List[int]
    """
    Row number where the error occurred.
    """

    # Metadata

    metadata_profile_patch = {
        "properties": {
            "labels": {"type": "array", "items": {"type": "string"}},
            "rowNumbers": {"type": "array", "items": {"type": "integer"}},
        },
    }


class BlankHeaderError(HeaderError):
    type = "blank-header"
    title = property(lambda self: _("Blank Header"))  # (canada fork only): i18n support
    description = property(lambda self: _("This header is empty. A header should contain at least one value."))  # (canada fork only): i18n support
    template = property(lambda self: _("Header is completely blank"))  # (canada fork only): i18n support
