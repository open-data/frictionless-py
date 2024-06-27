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
