#!/usr/bin/env python3
"""
System Health & Network Audit Logger
Author: Rami Izzeddin
"""

import os
import platform
import shutil
import subprocess

def check_disk_usage(path: str = "/"):
    """Check disk partition usage percentage."""
    total, used, free = shutil.disk_usage(path)
    percent_used = (used / total) * 100
    print(f"[DISK] Partition '{path}': {percent_used:.1f}% used ({free // (2**30)} GB free)")

def ping_host(host: str = "8.8.8.8"):
    """Ping a remote host to check network connectivity."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    
    res = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if res.returncode == 0:
        print(f"[NET] Host '{host}' is reachable.")
    else:
        print(f"[NET] Host '{host}' is UNREACHABLE.")

if __name__ == "__main__":
    print(f"=== System Health Audit [{platform.node()}] ===")
    check_disk_usage()
    ping_host()
