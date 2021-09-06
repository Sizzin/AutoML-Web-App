import warnings
from streamlit import write

def customwarn(message, category, filename, lineno, file=None, line=None):
    """A simple customization of warning messages"""
    write(message)

warnings.showwarning = customwarn