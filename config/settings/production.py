"""Settings for config project (Production)."""

import os

from .base import *


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "assets", "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "assets", "static_root")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "assets", "media")

SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 31536000  # 1 year

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_BROWSER_XSS_FILTER = True

CORS_ALLOW_CREDENTIALS = True
