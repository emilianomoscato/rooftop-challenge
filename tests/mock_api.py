from urllib.parse import urlsplit, parse_qs

from tests.testcases import get_test_cases


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def mocked_get_requests(*args):
    url = urlsplit(args[0])
    params = parse_qs(url.query)

    if url.path == "/token":
        email = params["email"][0]
        return MockResponse(*token_endpoint(email))
    elif url.path == "/blocks":
        token = params["token"][0]
        return MockResponse(*blocks_endpoint(token))
    return MockResponse(None, 404)


def mocked_post_requests(**kwargs):
    url = urlsplit(kwargs['url'])
    params = parse_qs(url.query)

    if url.path == "/check":
        token = params["token"][0]
        post_args = kwargs["data"]
        if "blocks" in post_args:
            blocks = post_args["blocks"]
            return MockResponse(*check_endpoint(token, blocks=blocks))
        elif "encoded" in post_args:
            encoded = post_args["encoded"]
            return MockResponse(*check_endpoint(token, encoded=encoded))
    return MockResponse(None, 404)


def token_endpoint(email: str):
    test_element = [item["token"] for item in get_test_cases() if item["email"] == email]
    if test_element:
        return {"token": test_element[0]}, 200
    else:
        return {}, 404


def blocks_endpoint(token: str):
    test_element = [item["blocks"] for item in get_test_cases() if item["token"] == token]
    if test_element:
        blocks = test_element[0]
        chunksize = len(blocks[0])
        return {"data": blocks, "chunkSize": chunksize, "length": chunksize * len(blocks)}, 200
    else:
        return {}, 404


def check_endpoint(token: str, blocks: list[str] = None, encoded: str = None):
    test_element = [item["sorted"] for item in get_test_cases() if item["token"] == token]
    if test_element:
        sorted_blocks = test_element[0]
        result = False
        if blocks:
            result = sorted_blocks.index(blocks[1]) - sorted_blocks.index(blocks[0]) == 1
        elif encoded:
            result = "".join(sorted_blocks) == encoded
        return {"message": result}, 200
    else:
        return {}, 404
