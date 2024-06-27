from __future__ import annotations

from ..error import Error
from .. import _  # (canada fork only): add i18n support


class DataError(Error):
    type = "data-error"
    title = _("Data Error")
    description = _("There is a data error.")
    template = _("Data error: {note}")
