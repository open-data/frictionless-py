from __future__ import annotations

from ..error import Error
from ..i18n import _  # (canada fork only): add i18n support


class MetadataError(Error):
    type = "metadata-error"
    title = _("Metadata Error")
    description = _("There is a metadata error.")
    template = _("Metadata error: {note}")


class CatalogError(MetadataError):
    type = "catalog-error"
    title = _("Catalog Error")
    description = _("A validation cannot be processed.")
    template = _("The data catalog has an error: {note}")


class DatasetError(CatalogError):
    type = "dataset-error"
    title = _("Dataset Error")
    description = _("A validation cannot be processed.")
    template = _("The dataset has an error: {note}")


class ChecklistError(MetadataError):
    type = "checklist-error"
    title = _("Checklist Error")
    description = _("Provided checklist is not valid.")
    template = _("Checklist is not valid: {note}")


class CheckError(ChecklistError):
    type = "check-error"
    title = _("Check Error")
    description = _("Provided check is not valid")
    template = _("Check is not valid: {note}")


class DetectorError(MetadataError):
    type = "detector-error"
    title = _("Detector Error")
    description = _("Provided detector is not valid.")
    template = _("Detector is not valid: {note}")


class DialectError(MetadataError):
    type = "dialect-error"
    title = _("Dialect Error")
    description = _("Provided dialect is not valid.")
    template = _("Dialect is not valid: {note}")


class ControlError(DialectError):
    type = "control-error"
    title = _("Control Error")
    description = _("Provided control is not valid.")
    template = _("Control is not valid: {note}")


class InquiryError(MetadataError):
    type = "inquiry-error"
    title = _("Inquiry Error")
    description = _("Provided inquiry is not valid.")
    template = _("Inquiry is not valid: {note}")


class InquiryTaskError(MetadataError):
    type = "inquiry-task-error"
    title = _("Inquiry Task Error")
    description = _("Provided inquiry task is not valid.")
    template = _("Inquiry task is not valid: {note}")


class PackageError(MetadataError):
    type = "package-error"
    title = _("Package Error")
    description = _("A validation cannot be processed.")
    template = _("The data package has an error: {note}")


class PipelineError(MetadataError):
    type = "pipeline-error"
    title = _("Pipeline Error")
    description = _("Provided pipeline is not valid.")
    template = _("Pipeline is not valid: {note}")


class StepError(PipelineError):
    type = "step-error"
    title = _("Step Error")
    description = _("Provided step is not valid")
    template = _("Step is not valid: {note}")


class ReportError(MetadataError):
    type = "report-error"
    title = _("Report Error")
    description = _("Provided report is not valid.")
    template = _("Report is not valid: {note}")


class ReportTaskError(ReportError):
    type = "report-task-error"
    title = _("Report Task Error")
    description = _("Provided report task is not valid.")
    template = _("Report task is not valid: {note}")


class SchemaError(MetadataError):
    type = "schema-error"
    title = _("Schema Error")
    description = _("Provided schema is not valid.")
    template = _("Schema is not valid: {note}")


class FieldError(SchemaError):
    type = "field-error"
    title = _("Field Error")
    description = _("Provided field is not valid.")
    template = _("Field is not valid: {note}")


class StatsError(MetadataError):
    type = "stats-error"
    title = _("Stats Error")
    description = _("Stats object has an error.")
    template = _("Stats object has an error: {note}")
