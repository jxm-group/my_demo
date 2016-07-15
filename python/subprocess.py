#!/usr/bin/env python
#coding=utf-8

import os
import sys
if os.name == 'posix' and sys.version_info[0] < 3:
    import subprocess32 as subprocess
else:
    import subprocess

args=["/mcos/dvclient/sbin/usbip/usbip-mgr"]
args.append("-c")
args.append("192.168.102.201")

sub=subprocess.Popen(args,close_fds=True)
print sub.wait()
print sub.poll()
