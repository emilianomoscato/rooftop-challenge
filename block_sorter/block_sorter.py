import requests

from block_sorter.block_sorter_exeptions import NoTokenException
from settings import API_URL


def check(blocks: list[str], token: str) -> list[str]:
    sorter = BlockSorter(blocks=blocks, token=token)
    sorter.sort()
    return sorter.sorted


def _get_token(api_url, token=None, email=None) -> str:
    if token:
        return token
    elif email:
        request = f"{api_url}/token?email={email}"
        resp = requests.get(request).json()
        return resp["token"]
    else:
        raise NoTokenException()


class BlockSorter:

    def __init__(self, token: str = None, base_url: str = API_URL, email: str = None, blocks=None,
                 sorted_blocks=None):
        self.url = base_url
        self.token = _get_token(self.url, token, email)
        self.blocks_endpoint = f"{self.url}/blocks?token={self.token}"
        self.check_endpoint = f'{self.url}/check?token={self.token}'
        self.blocks = blocks if blocks else self._get_blocks()
        self.sorted = sorted_blocks if sorted_blocks is not None else []

    def _check_blocks(self, b1: str, b2: str) -> bool:
        post_data = {"blocks": [b1, b2]}
        resp = requests.post(url=self.check_endpoint, data=post_data).json()
        return resp["message"]

    def _get_blocks(self) -> list[str]:
        resp = requests.get(self.blocks_endpoint).json()
        return resp["data"]

    def sort(self):
        # Move first element to ordered list
        last_ordered = self.blocks.pop(0)
        self.sorted = [last_ordered]

        while len(self.blocks) > 1:
            for index, block in enumerate(self.blocks):
                if self._check_blocks(last_ordered, block):
                    last_ordered = self.blocks.pop(index)
                    self.sorted.append(last_ordered)
                    break

        if len(self.blocks) == 1:
            # Move last unordered block without check against API
            self.sorted.append(self.blocks.pop())

    def validate(self) -> bool:
        post_data = {"encoded": "".join(self.sorted)}
        resp = requests.post(url=self.check_endpoint, data=post_data).json()
        return resp["message"]
