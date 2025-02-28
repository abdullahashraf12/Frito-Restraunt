#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

class Setter_Getter:
    def __init__(self,error_password="",error_account=""):
        self.error_password=error_password
        self.error_account=error_account
    def set_error_account(self,value):
        self.error_account=value
    def set_error_password(self,value):
        self.error_password=value
    def get_error_password(self):
        return self.error_password
    def get_error_account(self):
        return self.error_account

data = Setter_Getter()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Frito_Restraunt.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
