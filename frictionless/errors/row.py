from __future__ import annotations

from typing import TYPE_CHECKING, Any, List

import attrs

from .table import TableError

if TYPE_CHECKING:
    from ..table import Row

from ..i18n import _  # (canada fork only): add i18n support


@attrs.define(kw_only=True, repr=False)
class RowError(TableError):
    """Row error representation.

    A base class for all the errors related to a row of the
    tabular data.

    """

    type = "row-error"
    title = property(lambda self: _("Row Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Row Error"))  # (canada fork only): i18n support
    template = property(lambda self: _("Row Error"))  # (canada fork only): i18n support
    tags = ["#table", "#row"]

    cells: List[str]
    """
    Values of all the cells in the row that has an error.
    """

    row_number: int
    """
    Index of the row that has an error.
    """

    # Convert

    @classmethod
    def from_row(cls, row: Row, *, note: str):
        """Create an error from a row"""
        to_str = lambda v: str(v) if v is not None else ""  # type: ignore
        return cls(
            note=note,
            cells=list(map(to_str, row.cells)),  # type: ignore
            row_number=row.row_number,
        )

    # Metadata

    metadata_profile_patch = {
        "properties": {
            "cells": {"type": "array", "items": {"type": "string"}},
            "rowNumber": {"type": "integer"},
        },
    }


class BlankRowError(RowError):
    type = "blank-row"
    title = property(lambda self: _("Blank Row"))  # (canada fork only): i18n support
    description = property(lambda self: _("This row is empty. A row should contain at least one value."))  # (canada fork only): i18n support
    template = property(lambda self: _('Row at position "{rowNumber}" is completely blank'))  # (canada fork only): i18n support


class PrimaryKeyError(RowError):
    type = "primary-key"
    title = property(lambda self: _("PrimaryKey Error"))  # (canada fork only): i18n support
    description = property(_("Values in the primary key fields should be unique for every row"))  # (canada fork only): i18n support
    template = property(_('Row at position "{rowNumber}" violates the primary key: {note}'))  # (canada fork only): i18n support


@attrs.define(kw_only=True)
class ForeignKeyError(RowError):
    type = "foreign-key"
    title = property(lambda self: ("ForeignKey Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Values in the foreign key fields should exist in the reference table"))  # (canada fork only): i18n support
    template = property(lambda self: _('Row at position "{rowNumber}" violates the foreign key: {note}'))  # (canada fork only): i18n support

    field_names: List[str]
    """
    Keys in the resource target column.
    """

    field_cells: List[str]
    """
    Cells not found in the lookup table.
    """

    reference_name: str
    """
    Name of the lookup table the keys were searched on
    """

    reference_field_names: List[str]
    """
    Key names in the lookup table defined as foreign keys in the resource.
    """

    @classmethod
    def from_row(  # type: ignore
        cls,
        row: Row,
        *,
        note: str,
        field_names: List[str],  # type: ignore
        field_values: List[Any],  # type: ignore
        reference_name: str,  # type: ignore
        reference_field_names: List[str],  # type: ignore
    ):
        """Create an foreign-key-error from a row"""
        to_str = lambda v: str(v) if v is not None else ""  # type: ignore
        return cls(
            note=note,
            cells=list(map(to_str, row.cells)),  # type: ignore
            row_number=row.row_number,
            field_names=field_names,
            field_cells=list(map(to_str, field_values)),  # type: ignore
            reference_name=reference_name,
            reference_field_names=reference_field_names,
        )

    # Metadata

    metadata_profile_patch = {
        "properties": {
            "fieldNames": {"type": "array", "items": {"type": "string"}},
            "fieldCells": {"type": "array", "items": {"type": "string"}},
            "referenceName": {"type": "string"},
            "referenceFieldNames": {"type": "array", "items": {"type": "string"}},
        },
    }


class DuplicateRowError(RowError):
    type = "duplicate-row"
    title = property(lambda self: _("Duplicate Row"))  # (canada fork only): i18n support
    description = property(lambda self: _("The row is duplicated."))  # (canada fork only): i18n support
    template = property(lambda self: _("Row at position {rowNumber} is duplicated: {note}"))  # (canada fork only): i18n support


class RowConstraintError(RowError):
    type = "row-constraint"
    title = property(lambda self: _("Row Constraint"))  # (canada fork only): i18n support
    description = property(lambda self: _("The value does not conform to the row constraint."))  # (canada fork only): i18n support
    template = property(lambda self: _("The row at position {rowNumber} has an error: {note}"))  # (canada fork only): i18n support
