from __future__ import annotations

from typing import List

import attrs

from .table import TableError
from .. import _  # (canada fork only): add i18n support


@attrs.define(kw_only=True, repr=False)
class HeaderError(TableError):
    """Header error representation.

    A base class for all the errors related to the resource header.
    """

    type = "header-error"
    title = _("Header Error")
    description = _("Cell Error")
    template = _("Cell Error")
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
    title = _("Blank Header")
    description = _("This header is empty. A header should contain at least one value.")
    template = _("Header is completely blank")
