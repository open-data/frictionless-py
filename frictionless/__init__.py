from .actions import convert as convert
from .actions import describe as describe
from .actions import extract as extract
from .actions import list as list
from .actions import transform as transform
from .actions import validate as validate
from .analyzer import Analyzer as Analyzer
from .catalog import Catalog as Catalog
from .catalog import Dataset as Dataset
from .checklist import Check as Check
from .checklist import Checklist as Checklist
from .detector import Detector as Detector
from .dialect import Control as Control
from .dialect import Dialect as Dialect
from .error import Error as Error
from .exception import FrictionlessException as FrictionlessException
from .indexer import Indexer as Indexer
from .inquiry import Inquiry as Inquiry
from .inquiry import InquiryTask as InquiryTask
from .metadata import Metadata as Metadata
from .package import Package as Package
from .pipeline import Pipeline as Pipeline
from .pipeline import Step as Step
from .platform import Platform as Platform
from .platform import platform as platform
from .report import Report as Report
from .report import ReportTask as ReportTask
from .resource import Resource as Resource
from .schema import Field as Field
from .schema import Schema as Schema
from .settings import VERSION as __version__
from .system import Adapter as Adapter
from .system import Loader as Loader
from .system import Mapper as Mapper
from .system import Parser as Parser
from .system import Plugin as Plugin
from .system import System as System
from .system import system as system
from .table import Header as Header
from .table import Lookup as Lookup
from .table import Row as Row
from .transformer import Transformer as Transformer
from .validator import Validator as Validator

# (canada fork only): add i18n support
import gettext
import os
i18n_dir = os.path.join(os.path.dirname(__file__), '../i18n')
try:
    _ = gettext.translation('frictionless', i18n_dir).ugettext
except AttributeError:
    _ = gettext.translation('frictionless', i18n_dir).gettext
except IOError:
    _ = lambda x:x
