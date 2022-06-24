import pytest
import requests

from block_sorter.block_sorter import BlockSorter

collect_ignore = ["./test.py"]

@pytest.fixture
def block_sorter():
    return BlockSorter(token="abcd", blocks=["abcd"])


@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())
