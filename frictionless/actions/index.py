from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional

from ..exception import FrictionlessException
from ..platform import platform
from ..resource import Resource

if TYPE_CHECKING:
    from ..indexer import IOnProgress, IOnRow

from ..i18n import _  # (canada fork only): add i18n support


def index(
    source: Optional[Any] = None,
    *,
    name: Optional[str] = None,
    type: Optional[str] = None,
    # Index
    database_url: str,
    fast: bool = False,
    on_row: Optional[IOnRow] = None,
    on_progress: Optional[IOnProgress] = None,
    use_fallback: bool = False,
    qsv_path: Optional[str] = None,
    **options: Any,
) -> List[str]:
    """Index data into a database"""

    # Create resource
    resource = (
        source
        if isinstance(source, Resource)
        else Resource(source, datatype=type, **options)
    )

    # Index resource
    if not isinstance(resource, platform.frictionless_resources.Indexable):
        note = _('Resource with data type "{resource_datatype}" is not indexable').format(resource_datatype=resource.datatype)
        raise FrictionlessException(note)
    return resource.index(
        database_url,
        fast=fast,
        on_row=on_row,
        on_progress=on_progress,
        use_fallback=use_fallback,
        qsv_path=qsv_path,
    )
