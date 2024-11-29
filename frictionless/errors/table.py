from __future__ import annotations

from .data import DataError
from ..i18n import _  # (canada fork only): add i18n support


class TableError(DataError):
    type = "table-error"
    title = property(lambda self: _("Table Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("There is a table error."))  # (canada fork only): i18n support
    template = property(lambda self: _("General table error: {note}"))  # (canada fork only): i18n support
    tags = ["#table"]


class FieldCountError(TableError):
    type = "field-count"
    title = property(lambda self: _("Field Count Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("This error can happen if the data is corrupted."))  # (canada fork only): i18n support
    template = property(lambda self: _("The data source does not match the expected field count: {note}"))  # (canada fork only): i18n support


class RowCountError(TableError):
    type = "row-count"
    title = property(lambda self: _("Row Count Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("This error can happen if the data is corrupted."))  # (canada fork only): i18n support
    template = property(lambda self: _("The data source does not match the expected row count: {note}"))  # (canada fork only): i18n support


class TableDimensionsError(TableError):
    type = "table-dimensions"
    title = property(lambda self: _("Table dimensions error"))  # (canada fork only): i18n support
    description = property(lambda self: _("This error can happen if the data is corrupted."))  # (canada fork only): i18n support
    template = property(lambda self: _("The data source does not have the required dimensions: {note}"))  # (canada fork only): i18n support


class DeviatedValueError(TableError):
    type = "deviated-value"
    title = property(lambda self: _("Deviated Value"))  # (canada fork only): i18n support
    description = property(lambda self: _("The value is deviated."))  # (canada fork only): i18n support
    template = property(lambda self: _("There is a possible error because the value is deviated: {note}"))  # (canada fork only): i18n support


class DeviatedCellError(TableError):
    type = "deviated-cell"
    title = property(lambda self: _("Deviated cell"))  # (canada fork only): i18n support
    description = property(lambda self: _("The cell is deviated."))  # (canada fork only): i18n support
    template = property(lambda self: _("There is a possible error because the cell is deviated: {note}"))  # (canada fork only): i18n support


class RequiredValueError(TableError):
    type = "required-value"
    title = property(lambda self: _("Required Value"))  # (canada fork only): i18n support
    description = property(lambda self: _("The required values are missing."))  # (canada fork only): i18n support
    template = property(lambda self: _("Required values not found: {note}"))  # (canada fork only): i18n support
