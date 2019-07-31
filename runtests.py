#!/usr/bin/env python
import django
import logging
import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings
from os.path import abspath, dirname


app_name = 'edc_adverse_event'
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    ETC_DIR=os.path.join(base_dir, app_name, "tests", "etc"),
    SUBJECT_VISIT_MODEL="edc_reference.subjectvisit",
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django_crypto_fields.apps.AppConfig',
        'edc_action_item.apps.AppConfig',
        'edc_adverse_event.apps.AppConfig',
        'edc_facility.apps.AppConfig',
        'edc_notification.apps.AppConfig',
        'edc_registration.apps.AppConfig',
        'adverse_event_app.apps.AppConfig',
    ],
    add_dashboard_middleware=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    failures = DiscoverRunner(failfast=True).run_tests(
        [f'{app_name}.tests'])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()
