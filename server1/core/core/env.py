import os
import json
from pathlib import Path
###########################################################
# SET ENVIRONMENT VARIABLES
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def load_env():
    env_data = json.loads(open(BASE_DIR / '.env/', "r").read())
    for key, value in env_data.items():
        os.environ[key] = value
###########################################################