from __future__ import annotations

from ..error import Error
from ..i18n import _  # (canada fork only): add i18n support


class MetadataError(Error):
    type = "metadata-error"
    title = property(lambda self: _("Metadata Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("There is a metadata error."))  # (canada fork only): i18n support
    template = property(lambda self: _("Metadata error: {note}"))  # (canada fork only): i18n support


class CatalogError(MetadataError):
    type = "catalog-error"
    title = property(lambda self: _("Catalog Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("A validation cannot be processed."))  # (canada fork only): i18n support
    template = property(lambda self: _("The data catalog has an error: {note}"))  # (canada fork only): i18n support


class DatasetError(CatalogError):
    type = "dataset-error"
    title = property(lambda self: _("Dataset Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("A validation cannot be processed."))  # (canada fork only): i18n support
    template = property(lambda self: _("The dataset has an error: {note}"))  # (canada fork only): i18n support


class ChecklistError(MetadataError):
    type = "checklist-error"
    title = property(lambda self: _("Checklist Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Provided checklist is not valid."))  # (canada fork only): i18n support
    template = property(lambda self: _("Checklist is not valid: {note}"))  # (canada fork only): i18n support


class CheckError(ChecklistError):
    type = "check-error"
    title = property(lambda self: _("Check Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Provided check is not valid"))  # (canada fork only): i18n support
    template = property(lambda self: _("Check is not valid: {note}"))  # (canada fork only): i18n support


class DetectorError(MetadataError):
    type = "detector-error"
    title = property(lambda self: _("Detector Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Provided detector is not valid."))  # (canada fork only): i18n support
    template = property(lambda self: _("Detector is not valid: {note}"))  # (canada fork only): i18n support


class DialectError(MetadataError):
    type = "dialect-error"
    title = property(lambda self: _("Dialect Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Provided dialect is not valid."))  # (canada fork only): i18n support
    template = property(lambda self: _("Dialect is not valid: {note}"))  # (canada fork only): i18n support


class ControlError(DialectError):
    type = "control-error"
    title = property(lambda self: _("Control Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Provided control is not valid."))  # (canada fork only): i18n support
    template = property(lambda self: _("Control is not valid: {note}"))  # (canada fork only): i18n support


class InquiryError(MetadataError):
    type = "inquiry-error"
    title = property(lambda self: _("Inquiry Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Provided inquiry is not valid."))  # (canada fork only): i18n support
    template = property(lambda self: _("Inquiry is not valid: {note}"))  # (canada fork only): i18n support


class InquiryTaskError(MetadataError):
    type = "inquiry-task-error"
    title = property(lambda self: _("Inquiry Task Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Provided inquiry task is not valid."))  # (canada fork only): i18n support
    template = property(lambda self: _("Inquiry task is not valid: {note}"))  # (canada fork only): i18n support


class PackageError(MetadataError):
    type = "package-error"
    title = property(lambda self: _("Package Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("A validation cannot be processed."))  # (canada fork only): i18n support
    template = property(lambda self: _("The data package has an error: {note}"))  # (canada fork only): i18n support


class PipelineError(MetadataError):
    type = "pipeline-error"
    title = property(lambda self: _("Pipeline Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Provided pipeline is not valid."))  # (canada fork only): i18n support
    template = property(lambda self: _("Pipeline is not valid: {note}"))  # (canada fork only): i18n support


class StepError(PipelineError):
    type = "step-error"
    title = property(lambda self: _("Step Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Provided step is not valid"))  # (canada fork only): i18n support
    template = property(lambda self: _("Step is not valid: {note}"))  # (canada fork only): i18n support


class ReportError(MetadataError):
    type = "report-error"
    title = property(lambda self: _("Report Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Provided report is not valid."))  # (canada fork only): i18n support
    template = property(lambda self: _("Report is not valid: {note}"))  # (canada fork only): i18n support


class ReportTaskError(ReportError):
    type = "report-task-error"
    title = property(lambda self: _("Report Task Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Provided report task is not valid."))  # (canada fork only): i18n support
    template = property(lambda self: _("Report task is not valid: {note}"))  # (canada fork only): i18n support


class SchemaError(MetadataError):
    type = "schema-error"
    title = property(lambda self: _("Schema Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Provided schema is not valid."))  # (canada fork only): i18n support
    template = property(lambda self: _("Schema is not valid: {note}"))  # (canada fork only): i18n support


class FieldError(SchemaError):
    type = "field-error"
    title = property(lambda self: _("Field Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Provided field is not valid."))  # (canada fork only): i18n support
    template = property(lambda self: _("Field is not valid: {note}"))  # (canada fork only): i18n support


class StatsError(MetadataError):
    type = "stats-error"
    title = property(lambda self: _("Stats Error"))  # (canada fork only): i18n support
    description = property(lambda self: _("Stats object has an error."))  # (canada fork only): i18n support
    template = property(lambda self: _("Stats object has an error: {note}"))  # (canada fork only): i18n support
