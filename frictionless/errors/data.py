from __future__ import annotations

from ..error import Error
from ..i18n import _  # (canada fork only): add i18n support


class DataError(Error):
    type = "data-error"
    title = property(lambda self: _("Data Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("There is a data error."))  # (canada fork only): i18n support
    template = property(lambda self: _("Data error: {note}"))  # (canada fork only): i18n support
