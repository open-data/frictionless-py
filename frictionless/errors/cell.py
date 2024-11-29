from __future__ import annotations

from typing import TYPE_CHECKING, Any

import attrs

from ..exception import FrictionlessException
from .row import RowError
from ..i18n import _  # (canada fork only): add i18n support

if TYPE_CHECKING:
    from ..table import Row


@attrs.define(kw_only=True, repr=False)
class CellError(RowError):
    """Cell error representation.

    A base class for all the errors related to the cell value.
    """

    type = "cell-error"
    title = property(lambda self: _("Cell Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Cell Error"))  # (canada fork only): i18n support
    template = property(lambda self: _("Cell Error"))  # (canada fork only): i18n support
    tags = ["#table", "#row", "#cell"]

    cell: str
    """
    Cell where the error occurred.
    """

    field_name: str
    """
    Name of the field that has an error.
    """

    field_number: int
    """
    Index of the field that has an error.
    """

    # Convert

    @classmethod
    def from_row(cls, row: Row, *, note: str, field_name: str):  # type: ignore
        """Create and error from a cell

        Parameters:
            row (Row): row
            note (str): note
            field_name (str): field name

        Returns:
            CellError: error
        """
        # This algorithm can be optimized by storing more information in a row
        # At the same time, this function should not be called very often
        for field_number, name in enumerate(row.field_names, start=1):
            if field_name == name:
                cell: Any = row[field_name]
                to_str = lambda v: str(v) if v is not None else ""  # type: ignore
                return cls(
                    note=note,
                    cells=list(map(to_str, row.cells)),  # type: ignore
                    row_number=row.row_number,
                    cell=str(cell),
                    field_name=field_name,
                    field_number=field_number,
                )
        raise FrictionlessException(_("Field {field_name} is not in the row").format(field_name=field_name))

    # Metadata

    metadata_profile_patch = {
        "properties": {
            "cell": {"type": "string"},
            "fieldName": {"type": "string"},
            "fieldNumber": {"type": "integer"},
        },
    }


class ExtraCellError(CellError):
    type = "extra-cell"
    title = property(lambda self: _("Extra Cell"))  # (canada fork only): i18n support
    description = property(lambda self: _("This row has more values compared to the header row (the first row in the data source). A key concept is that all the rows in tabular data must have the same number of columns."))  # (canada fork only): i18n support
    template = property(lambda self: _('Row at position "{rowNumber}" has an extra value in field at position "{fieldNumber}"'))  # (canada fork only): i18n support


class MissingCellError(CellError):
    type = "missing-cell"
    title = property(lambda self: _("Missing Cell"))  # (canada fork only): i18n support
    description = property(lambda self: _("This row has less values compared to the header row (the first row in the data source). A key concept is that all the rows in tabular data must have the same number of columns."))  # (canada fork only): i18n support
    template = property(lambda self: _('Row at position "{rowNumber}" has a missing cell in field "{fieldName}" at position "{fieldNumber}"'))  # (canada fork only): i18n support


class TypeError(CellError):
    type = "type-error"
    title = property(lambda self: _("Type Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("The value does not match the schema type and format for this field."))  # (canada fork only): i18n support
    template = property(lambda self: _('Type error in the cell "{cell}" in row "{rowNumber}" and field "{fieldName}" at position "{fieldNumber}": {note}'))  # (canada fork only): i18n support


class ConstraintError(CellError):
    type = "constraint-error"
    title = property(lambda self: _("Constraint Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("A field value does not conform to a constraint."))  # (canada fork only): i18n support
    template = property(lambda self: _('The cell "{cell}" in row at position "{rowNumber}" and field "{fieldName}" at position "{fieldNumber}" does not conform to a constraint: {note}'))  # (canada fork only): i18n support


class UniqueError(CellError):
    type = "unique-error"
    title = property(lambda self: _("Unique Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("This field is a unique field but it contains a value that has been used in another row."))  # (canada fork only): i18n support
    template = property(lambda self: _('Row at position "{rowNumber}" has unique constraint violation in field "{fieldName}" at position "{fieldNumber}": {note}'))  # (canada fork only): i18n support


class TruncatedValueError(CellError):
    type = "truncated-value"
    title = property(lambda self: _("Truncated Value"))  # (canada fork only): i18n support
    description = property(lambda self: _("The value is possible truncated."))  # (canada fork only): i18n support
    template = property(lambda self: _("The cell {cell} in row at position {rowNumber} and field {fieldName} at position {fieldNumber} has an error: {note}"))  # (canada fork only): i18n support


class ForbiddenValueError(CellError):
    type = "forbidden-value"
    title = property(lambda self: _("Forbidden Value"))  # (canada fork only): i18n support
    description = property(lambda self: _("The value is forbidden."))  # (canada fork only): i18n support
    template = property(lambda self: _("The cell {cell} in row at position {rowNumber} and field {fieldName} at position {fieldNumber} has an error: {note}"))  # (canada fork only): i18n support


class SequentialValueError(CellError):
    type = "sequential-value"
    title = property(lambda self: _("Sequential Value"))  # (canada fork only): i18n support
    description = property(lambda self: _("The value is not sequential."))  # (canada fork only): i18n support
    template = property(lambda self: _("The cell {cell} in row at position {rowNumber} and field {fieldName} at position {fieldNumber} has an error: {note}"))  # (canada fork only): i18n support


class AsciiValueError(CellError):
    type = "ascii-value"
    title = property(lambda self: _("Ascii Value"))  # (canada fork only): i18n support
    description = property(lambda self: _("The cell contains non-ascii characters."))  # (canada fork only): i18n support
    template = property(lambda self: _("The cell {cell} in row at position {rowNumber} and field {fieldName} at position {fieldNumber} has an error: {note}"))  # (canada fork only): i18n support
