from typing import TypedDict


class DefaultIcons(TypedDict):
    """These are the icons that appear on the top right in the extension area."""
    x16: str
    x24: str
    x32: str


class Icons(TypedDict):
    """These are the icons that appear in the chrome web store and in the extension settings on Chrome."""
    x16: str
    x32: str
    x48: str
    x128: str
