from __future__ import annotations

import attrs

from .header import HeaderError
from ..i18n import _  # (canada fork only): add i18n support


@attrs.define(kw_only=True, repr=False)
class LabelError(HeaderError):
    """Label error representation.

    A base class for all the errors related to the labels of the columns/fields.

    """

    type = "label-error"
    title = property(lambda self: _("Label Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Label Error"))  # (canada fork only): i18n support
    template = property(lambda self: _("Label Error"))  # (canada fork only): i18n support
    tags = ["#table", "#header", "#label"]

    label: str
    """
    Label of the field that has an error.
    """

    field_name: str
    """
    Name of the field that has an error.
    """

    field_number: int
    """
    Index of the field that has an error.
    """

    # Metadata

    metadata_profile_patch = {
        "properties": {
            "label": {"type": "string"},
            "fieldName": {"type": "string"},
            "fieldNumber": {"type": "integer"},
        },
    }


class ExtraLabelError(LabelError):
    type = "extra-label"
    title = property(lambda self: _("Extra Label"))  # (canada fork only): i18n support
    description = property(lambda self: _("The header of the data source contains label that does not exist in the provided schema."))  # (canada fork only): i18n support
    template = property(lambda self: _('There is an extra label "{label}" in header at position "{fieldNumber}"'))  # (canada fork only): i18n support


class MissingLabelError(LabelError):
    type = "missing-label"
    title = property(lambda self: _("Missing Label"))  # (canada fork only): i18n support
    description = property(lambda self: _("Based on the schema there should be a label that is missing in the data's header."))  # (canada fork only): i18n support
    template = property(lambda self: _('There is a missing label in the header\'s field "{fieldName}" at position "{fieldNumber}"'))  # (canada fork only): i18n support


class BlankLabelError(LabelError):
    type = "blank-label"
    title = property(lambda self: _("Blank Label"))  # (canada fork only): i18n support
    description = property(lambda self: _("A label in the header row is missing a value. Label should be provided and not be blank."))  # (canada fork only): i18n support
    template = property(lambda self: _('Label in the header in field at position "{fieldNumber}" is blank'))  # (canada fork only): i18n support


class DuplicateLabelError(LabelError):
    type = "duplicate-label"
    title = property(lambda self: _("Duplicate Label"))  # (canada fork only): i18n support
    description = property(lambda self: _("Two columns in the header row have the same value. Column names should be unique."))  # (canada fork only): i18n support
    template = property(lambda self: _('Label "{label}" in the header at position "{fieldNumber}" is duplicated to a label: {note}'))  # (canada fork only): i18n support


class IncorrectLabelError(LabelError):
    type = "incorrect-label"
    title = property(lambda self: _("Incorrect Label"))  # (canada fork only): i18n support
    description = property(lambda self: _("One of the data source header does not match the field name defined in the schema."))  # (canada fork only): i18n support
    template = property(lambda self: _('Label "{label}" in field {fieldName} at position "{fieldNumber}" does not match the field name in the schema'))  # (canada fork only): i18n support
