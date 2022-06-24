from unittest.mock import patch

import pytest

from block_sorter.block_sorter import _get_token, BlockSorter, NoTokenException, check

from tests.mock_api import mocked_get_requests, mocked_post_requests
from tests.testcases import get_test_cases


@pytest.mark.parametrize(
    'email, token',
    [(case['email'], case['token']) for case in get_test_cases()]
)
@patch("block_sorter.block_sorter.requests.get", side_effect=mocked_get_requests)
def test__get_token(mock_get, email, token):
    assert _get_token("", email=email) == token
    assert _get_token("", token=token) == token
    with pytest.raises(NoTokenException):
        _get_token("")
    assert mock_get.called


@pytest.mark.parametrize(
    'email, token',
    [(case["email"], case["token"]) for case in get_test_cases()]
)
@patch("block_sorter.block_sorter.requests.get", side_effect=mocked_get_requests)
def test_block_sorter(mock_get, email, token):
    bs = BlockSorter(token=token)
    bs2 = BlockSorter(email=email)
    assert bs.token == token
    assert bs2.token == token
    assert bs.sorted == []


@pytest.mark.parametrize(
    'token, blocks',
    [(case["token"], case["blocks"]) for case in get_test_cases()]
)
@patch("block_sorter.block_sorter.requests.get", side_effect=mocked_get_requests)
def test__get_blocks(mock_get, token, blocks, block_sorter):
    sorter = BlockSorter(token=token)
    assert sorter._get_blocks() == blocks


@pytest.mark.parametrize('validation', [True, False])
@patch("block_sorter.block_sorter.requests.post")
def test__check_blocks(mock_post, validation, block_sorter):
    mock_post.return_value.ok = True
    mock_post.return_value.json.return_value = {"message": validation}
    assert block_sorter._check_blocks("", "") is validation


@pytest.mark.parametrize('blocks', [["abcd", "bcde"], ["abcd"], ])
def test_sort_without_api(blocks, block_sorter):
    """
    Test sort method without patching API to test that it doesn't consult the API if not necessary 
    """
    block_sorter.blocks = blocks.copy()
    block_sorter.sort()
    assert block_sorter.sorted == blocks


@pytest.mark.parametrize(
    'token, blocks, sorted_blocks',
    [(case["token"], case["blocks"], case["sorted"]) for case in get_test_cases()]
)
@patch("block_sorter.block_sorter.requests.post", side_effect=mocked_post_requests)
def test_sort_with_api_call(mock_post, token, blocks, sorted_blocks):
    sorter = BlockSorter(token=token, blocks=blocks)
    sorter.sort()
    assert sorter.sorted == sorted_blocks


@pytest.mark.parametrize(
    'token, sorted',
    [(case["token"], case["sorted"]) for case in get_test_cases()]
)
@patch("block_sorter.block_sorter.requests.post", side_effect=mocked_post_requests)
def test_validate(mock_post, token, sorted):
    sorter = BlockSorter(token=token, blocks=sorted)
    sorter.sorted = sorted
    assert sorter.validate()


@pytest.mark.parametrize(
    'token, blocks, sorted_blocks',
    [(case["token"], case["blocks"], case["sorted"]) for case in get_test_cases()]
)
@patch("block_sorter.block_sorter.requests.post", side_effect=mocked_post_requests)
def test_check(mock_post, token, blocks, sorted_blocks):
    assert check(blocks, token) == sorted_blocks
