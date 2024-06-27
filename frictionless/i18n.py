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


def set_language(lang):
    """Use a different language for errors than the default

    # Raises
        IOError: translation for lang is not found.
    """
    global _
    try:
        _ = gettext.translation('frictionless', i18n_dir, [lang]).ugettext
    except AttributeError:
        _ = gettext.translation('frictionless', i18n_dir, [lang]).gettext
    except IOError:
        _ = lambda x:x
