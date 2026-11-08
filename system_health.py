#!/usr/bin/env python3
"""
System Diagnostics & Health Checker
Author: Rami Izzeddin
"""

import os
import platform

def get_system_info():
    """Display core platform and diagnostic attributes."""
    print("=== System Health Diagnostics ===")
    print(f"OS Platform : {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Hostname    : {platform.node()}")
    print(f"Python Ver. : {platform.python_version()}")

if __name__ == "__main__":
    get_system_info()
