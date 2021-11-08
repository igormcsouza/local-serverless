"""
# Time according to Timezone

Capture the time according to the timezone
"""
import pytz
import datetime

import argh


def get_timezone(timezone='US/Pacific'):
    """Gets the time according to the timezone."""
    return datetime.datetime.now(tz=pytz.timezone(timezone))


# assembling:

parser = argh.ArghParser()
parser.add_commands([get_timezone])

# dispatching:

if __name__ == '__main__':
    parser.dispatch()
