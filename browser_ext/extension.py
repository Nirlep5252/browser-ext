import os
import json
import sys
import shutil
from typing import Optional
from .types import DefaultIcons, Icons


class ChromeExtension:
    def __init__(
        self, name: str, version: str, description: str, author: Optional[str] = None,
        default_title: Optional[str] = None,
        action_icons: Optional[DefaultIcons] = None,
        icons: Optional[Icons] = None,
    ):
        self._name = name
        self._version = version
        self._description = description
        self._author = author
        self._default_title = default_title

        self._action_icons = action_icons
        self._icons = icons
        self._popup: Optional[str] = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> str:
        return self._version

    @property
    def description(self) -> str:
        return self._description

    def add_popup(self, filename: str) -> None:
        if self._popup is not None:
            raise ValueError("Popup already set.")
        if not os.path.isfile(filename):
            raise RuntimeError(f"The file `{filename}` does not exist.")
        if not filename.endswith(".html"):
            raise RuntimeError(f"The file `{filename}` is not a html file.")

        self._popup = filename

    def build(self, folderName: Optional[str] = "chrome-build", overwrite: bool = False) -> None:
        """This method builds the extension and no more code below this will be executed."""
        manifest_dict = {
            "manifest_version": 3,
            "name": self._name,
            "version": self._version,
            "description": self._description,
            "icons": self._icons or {},
            "author": self._author,

            "action": {
                "default_icon": self._action_icons or {},
                "default_title": self._default_title,
                "default_popup": self._popup or "",
            },

            "background": {"service_worker": "background.js"}
        }

        if os.path.exists(folderName) and not overwrite:
            raise RuntimeError(f"The folder `{folderName}` already exists. Please remove/rename it first.")
        if os.path.exists(folderName) and overwrite:
            shutil.rmtree(folderName)

        os.mkdir(folderName)
        if self._popup is not None:
            shutil.copy2(self._popup, f"{folderName}/{self._popup}")
        with open("chrome-build/manifest.json", "w") as f:
            json.dump(manifest_dict, f, indent=4)
        with open("chrome-build/background.js", "w") as f:
            pass
        print("Your Chrome extension is ready!")
        sys.exit(0)
