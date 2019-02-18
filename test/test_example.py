# -*- coding: utf-8 -*-
import sys
import pytest

# Marked as integration test
# Could be launched isolated with 'pytest -v -m example'

@pytest.mark.example
@pytest.mark.skipif('example' not in sys.argv,
                    reason="no explicitly selected")
#@pytest.mark.skipif('example' not in pytest.config.getoption('markexpr').split(),
#                    reason="no explicitly selected")
def test_example():
    assert 1 == 1
