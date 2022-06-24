from unittest.mock import patch

import pytest

from block_sorter.check import check
from tests.mock_api import mocked_post_requests
from tests.testcases import get_test_cases


@pytest.mark.parametrize(
    'token, blocks, sorted_blocks',
    [(case["token"], case["blocks"], case["sorted"]) for case in get_test_cases()]
)
@patch("block_sorter.block_sorter.requests.post", side_effect=mocked_post_requests)
def test_check(mock_post, token, blocks, sorted_blocks):
    assert check(blocks, token) == sorted_blocks
