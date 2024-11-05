
from datetime import datetime

now = datetime.now()

ts = now.timestamp()

print(f"Second since january 1, 1970: {ts:,.4f} or {ts:.2e} in scientific notation")
print(f"{now.strftime("%b")} {now.day} {now.year}")
