#!/usr/bin/env bash
# Linux System Diagnostic Audit Script
# Author: Rami Izzeddin

echo "========== SYSTEM DIAGNOSTIC REPORT =========="
echo "Date & Time : $(date)"
echo "Kernel Ver. : $(uname -r)"
echo "Uptime      : $(uptime -p)"
echo "=============================================="

echo -e "\n[1] CPU Load Average:"
cat /proc/loadavg

echo -e "\n[2] Memory Utilization:"
free -h

echo -e "\n[3] Disk Space Usage:"
df -h --total | grep -E 'Filesystem|total|/'

echo -e "\n[4] Failed Systemd Services:"
systemctl list-units --state=failed --no-legend 2>/dev/null || echo "No failed systemd services detected."

echo "=============================================="
