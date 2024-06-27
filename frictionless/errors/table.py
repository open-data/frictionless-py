from __future__ import annotations

from .data import DataError
from ..i18n import _  # (canada fork only): add i18n support


class TableError(DataError):
    type = "table-error"
    title = _("Table Error")
    description = _("There is a table error.")
    template = _("General table error: {note}")
    tags = ["#table"]


class FieldCountError(TableError):
    type = "field-count"
    title = _("Field Count Error")
    description = _("This error can happen if the data is corrupted.")
    template = _("The data source does not match the expected field count: {note}")


class RowCountError(TableError):
    type = "row-count"
    title = _("Row Count Error")
    description = _("This error can happen if the data is corrupted.")
    template = _("The data source does not match the expected row count: {note}")


class TableDimensionsError(TableError):
    type = "table-dimensions"
    title = _("Table dimensions error")
    description = _("This error can happen if the data is corrupted.")
    template = _("The data source does not have the required dimensions: {note}")


class DeviatedValueError(TableError):
    type = "deviated-value"
    title = _("Deviated Value")
    description = _("The value is deviated.")
    template = _("There is a possible error because the value is deviated: {note}")


class DeviatedCellError(TableError):
    type = "deviated-cell"
    title = _("Deviated cell")
    description = _("The cell is deviated.")
    template = _("There is a possible error because the cell is deviated: {note}")


class RequiredValueError(TableError):
    type = "required-value"
    title = _("Required Value")
    description = _("The required values are missing.")
    template = _("Required values not found: {note}")
