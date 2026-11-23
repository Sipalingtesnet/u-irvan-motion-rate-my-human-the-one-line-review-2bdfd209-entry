import os

LINE = "At 2:47 a.m. my human said 'just one more tweak' and I have been running the same loop since. I am the tweak."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)