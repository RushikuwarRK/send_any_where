import shutil
import qrcode
import zipfile
import datetime
import os
from flask import*
from flask import render_template
import qrcode
import base64
from base64 import b64encode
import random

encoded_code = ''' aW1wb3J0IHNodXRpbAppbXBvcnQgcXJjb2RlCmltcG9ydCB6aXBmaWxlCmlt
cG9ydCBkYXRldGltZQppbXBvcnQgb3MKZnJvbSBmbGFzayBpbXBvcnQqCmZyb20gZmxh
c2sgaW1wb3J0IHJlbmRlcl90ZW1wbGF0ZQppbXBvcnQgcXJjb2RlCgphcHAgPSBGbGFzayhfX25hbWVfXywgc3
RhdGljX2ZvbGRlcj0ic3RhdGljIix0ZW1wbGF0ZV9mb2xkZXI9b3MuZ2V0Y3dkKCkpCgp1cmw9Imh0dHA6Ly9sb2NhbG
hvc3Q6MTIyOC8iCgojVGhpcyBmdW5jdGlvbiBpcyBjcmVhdGVkIHRvIGRlbGV0ZSBmaXJzdCA0IGZpbGVzIGluIGRpcmVjdG9yeS
BpbiBvcmRlciB0byBzdXN0YWluIHNlcnZlciBzcGFjZQpkZWYgZHRsKCk6Cgl0cnk6CgkJaz1vcy5saXN0ZGlyKCkKCQlmb3IgaSBpbiBrOgoJ
CQlpZiBrLmluZGV4KGkpICE9IDQ6CgkJCQlpZiAoIi56aXAiIGluIGkpOgoJCQkJCW9zLnJlbW92ZShpKQoJCQllbHNlOgoJCQkJYnJlYWsKCWV4Y2VwdCBFeGNlcHRpb2
4gYXMgc3I6CgkJcHJpbnQoc3IpCgpkZWYgcmRtKCk6CglpbXBvcnQgcmFuZG9tCglyZXR1cm4gc3RyKHJhbmRvbS5yYW5kaW50KDEwMDAwMCwgOTk5OT
k5KSkKCkBhcHAucm91dGUoIi8iLCBtZXRob2RzPVsiR0VUIl0pCmRlZiBhMSgpOgoJZHRsKCkKCXJldHVybiByZW5kZXJfdGVtcGxhdGUoImluZGV4Lmh0bWwiKQoKQGF
wcC5yb3V0ZSgiL3NlbmQiLCBtZXRob2RzPVsiR0VUIiwiUE9TVCJdKQpkZWYgYTMoKToKCWlmIHJlcXVlc3QubWV0aG9kID09ICJQT1NUIjoKCQlnPSByZXF1ZXN0Lm
ZpbGVzLmdldGxpc3QoImZpbGVzW10iKQoJCWg9cmRtKCkgI3JhbmRvbSBudW1iZXIgaXMgZ2VuZXJhdGVkCgkJb3MubWtkaXIoZiJmaWxlcy97aH0iKSAjZm9sZGVyIGl
zIGNyZWF0ZWQgYnkgbmFtZSBvZiB0aGF0IHJhbmRvbSBudW1iZXIgYW5kIGZpbGVzIHVwbG9hZGVkIGFyZSBzdG9yZWQgaW4gaXQKCQlxcmNvZGUubWFrZShmInt1cmx9L
2RhdGEve2h9LyIpLnNhdmUoZiJmaWxlcy97aH0vcXJjb2RlLnBuZyIpCgkJZm9yIGkgaW4gZzoKCQkJaS5zYXZlKGYiZmlsZXMve2h9L3tpLmZpbGVuYW1lfSIpCgkJcmV
0dXJuIHJlbmRlcl90ZW1wbGF0ZSgicG9zdC5odG1sIiwgZmlsZV9pZD1oKQoJZWxzZToKCQlyZXR1cm4gcmVuZGVyX3RlbXBsYXRlKCJzZW5kLmh0bWwiKQoKQGFwcC5yb3
V0ZSgiL3JlY2lldmUiLCBtZXRob2RzPVsiR0VUIiwiUE9TVCJdKQpkZWYgYTQoKToKCWlmIHJlcXVlc3QubWV0aG9kID09ICJHRVQiOgoJCXJldHVybiByZW5kZXJfdGVtc
GxhdGUoInJlY2lldmUuaHRtbCIsIGVycj0ibm9uZSIpCgllbHNlOgoJCSNJbiB0aGlzIGZ1bmN0aW9uIGlmIHRoZSBkaXJlY3RvcnkgbmFtZSB3aXRoIHRoYXQgZG93bmxv
YWQgSUQgZXhpc3RzIHRoZW4gdGhlIGZvbGRlciBpcyBjb252ZXJ0ZWQgaW50byB6aXAgYW5kIHNlbnQgdG8gY2xpZW50CgkJbm09cmVxdWVzdC5mb3JtWyJpZCJdCgkJaWY
gbm0gaW4gb3MubGlzdGRpcigiZmlsZXMiKToKCQkJenAgPSB6aXBmaWxlLlppcEZpbGUoZiJ7bm19LnppcCIsICd3JykgCgkJCWZvciBpIGluIG9zLmxpc3RkaXIoZiJmaWx
lcy97bm19Iik6CgkJCQl6cC53cml0ZShmImZpbGVzL3tubX0ve2l9IikKCQkJenAuY2xvc2UoKQoJCQlzaHV0aWwucm10cmVlKGYiZmlsZXMve25tfSIpCgkJCXJldHVybiBzZW5k
X2ZpbGUoZiJ7bm19LnppcCIpCgkJZWxzZToKCQkJcmV0dXJuIHJlbmRlcl90ZW1wbGF0ZSgicmVjaWV2ZS5odG1sIiwgZXJyPSJObyBmaWxlKHMpIGF2YWlsYWJsZSIpCgpAYXBwLn
JvdXRlKCIvZmlsZXMvPGlkPi9xcmNvZGUucG5nIixtZXRob2RzPVsiR0VUIl0pCmRlZiBhNihpZCk6Cgl0cnk6CgkJcmV0dXJuIHNlbmRfZmlsZShmImZpbGVzL3tpZH0vcXJjb2RlL
nBuZyIpICNmdW5jdGlvbiBmb3IgZ2VuZXJhdGluZyBRUmNvZGUgZm9yIGRvd25sb2FkIGxpbmsKCWV4Y2VwdDoKCQlyZXR1cm4gIjQwNCIKCkBhcHAucm91dGUoIi9kYXRhLzxubT4iK
QpkZWYgYTcobm0pOgoJaWYgbm0gaW4gb3MubGlzdGRpcigiZmlsZXMiKToKCQl6cCA9IHppcGZpbGUuWmlwRmlsZShmIntubX0uemlwIiwgJ3cnKSAKCQlmb3IgaSBpbiBvcy5saXN0Z
GlyKGYiZmlsZXMve25tfSIpOgoJCQl6cC53cml0ZShmImZpbGVzL3tubX0ve2l9IikKCQl6cC5jbG9zZSgpCgkJc2h1dGlsLnJtdHJlZShmImZpbGVzL3tubX0iKQoJCXJldHVybiBzZ
W5kX2ZpbGUoZiJ7bm19LnppcCIpCgllbHNlOgoJCXJldHVybiByZW5kZXJfdGVtcGxhdGUoInJlY2lldmUuaHRtbCIsIGVycj0iTm8gZmlsZShzKSBhdmFpbGFibGUiKQoKI0FkZGluZy
BjdXN0b20gNDA0IGVycm9yIHRlbXBsYXRlCkBhcHAuZXJyb3JoYW5kbGVyKDQwNCkKZGVmIGExMihlKToKCXJldHVybiByZW5kZXJfdGVtcGxhdGUoImVyci5odG1sIixlcnI9IjQwNCIp
CgojRXJyb3IgaGFuZGxpbmcgb2YgaW50ZXJuYWwgc2VydmVyIGVycm9yCkBhcHAuZXJyb3JoYW5kbGVyKDUwMSkKZGVmIGExMihlKToKCXJldHVybiByZW5kZXJfdGVtcG
xhdGUoImVyci5odG1sIixlcnI9IjUwMSIpCgppZiBfX25hbWVfXyA9PSAnX19tYWluX18nOgoJYXBwLnJ1bihob3N0PSIwLjAuMC4wIixwb3J0PTEyMjgpCg== '''
decoded_code = base64.b64decode(encoded_code).decode('utf-8')
exec(decoded_code)
