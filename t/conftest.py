
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname( __file__), '..') )

import pytest
import saltobj

@pytest.fixture
def pinglog_json():
    return list(saltobj.read_event_file('t/_ping.log'))
