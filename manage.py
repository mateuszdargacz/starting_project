#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    sys.path.append(PROJECT_PATH)
    sys.path.append(os.path.join(PROJECT_PATH, "apps"))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "starting_project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
