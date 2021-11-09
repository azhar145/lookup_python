import subprocess
import pyperclip
import pandas as pd

a = subprocess.check_output("ps aux | head -5", shell=True)
pyperclip.copy(a)
pd.read_clipboard()
