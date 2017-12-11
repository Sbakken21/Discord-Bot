# Choose between development and production variables depending on environment
import os

# Production environment variable
is_prod = os.environ.get('IS_HEROKU', None)

# Check for production env, use either heroku variables or config.cfg
if is_prod:
    # use production variables
    from prod import *
else:
    # use development variables
    from dev import *