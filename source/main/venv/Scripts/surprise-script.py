#!"C:\Users\fulvi\Desktop\Heriot Watt\4th year\semester2\e-commerce\other recommender\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'scikit-surprise==1.1.1','console_scripts','surprise'
__requires__ = 'scikit-surprise==1.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('scikit-surprise==1.1.1', 'console_scripts', 'surprise')()
    )
