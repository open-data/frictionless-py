# (canada fork only): custom checks i18n

_ = lambda x:x

_("Invalid Header for DataStore")
_("Column name is invalid for a DataStore header.\n\n How it could be resolved:\n - Remove any leading underscores('_') from the column name.\n - Remove any leading or trailing white space from the column name.\n - Remove any double quotes('\"') from the column name.\n - Make sure the column name is not blank.")
_("Column name {value} in column {column_number} is not valid for a DataStore header")

_("Header Too Long for DataStore")
_("Column name is too long for a DataStore header.\n\n How it could be resolved:\n - Make the column name at most 63 characters long.")
_("Column name {value} in column {column_number} is too long for a DataStore header")
