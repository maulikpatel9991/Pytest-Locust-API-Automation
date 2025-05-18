# utils/monkey_patch.py

import os

def safe_monkey_patch():
    """
    Perform gevent monkey patching ONLY if using Locust.
    Prevents SSL recursion errors during pytest runs.
    """
    if os.getenv("USE_LOCUST") == "1":
        from gevent import monkey
        monkey.patch_all()
