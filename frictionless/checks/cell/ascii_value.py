from __future__ import annotations

from typing import TYPE_CHECKING, Iterable

import attrs

from ... import errors
from ...checklist import Check

if TYPE_CHECKING:
    from ...error import Error
    from ...table import Row

from ...i18n import _  # (canada fork only): add i18n support


@attrs.define(kw_only=True, repr=False)
class ascii_value(Check):
    """Check whether all the string characters in the data are ASCII

    This check can be enabled using the `checks` parameter
    for the `validate` function.

    """

    type = "ascii-value"
    Errors = [errors.AsciiValueError]

    # Validate

    def validate_row(self, row: Row) -> Iterable[Error]:
        for field in row.fields:  # type: ignore
            if field.type == "string":
                cell = row[field.name]
                if cell and not cell.isascii():
                    note = _("the cell contains non-ascii characters")
                    yield errors.AsciiValueError.from_row(
                        row, note=note, field_name=field.name
                    )
