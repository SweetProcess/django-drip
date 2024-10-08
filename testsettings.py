SECRET_KEY = "dripdripdripdripdripdripdrip"

# MUST SPECIFY TO MAKE USE OF DJANGO DRIP
DRIP_FROM_EMAIL = ""
DEBUG = True

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

SECRET_KEY = "whatever/you/want-goes-here"

SECRET_KEY = "whatever"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "sqlite.db",
    },
}

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.sessions",
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.messages",
    "drip",
    # testing only
    "credits",
)

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)


USE_TZ = True
TIME_ZONE = "UTC"

AUTH_PROFILE_MODULE = "credits.Profile"

ROOT_URLCONF = "test_urls"

STATIC_URL = "/static/"
STATICFILES_DIRS = ()

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    },
]
