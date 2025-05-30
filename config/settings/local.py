"""Settings for config project (Local)."""

import os

from .base import *


STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "assets", "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "assets", "media")
