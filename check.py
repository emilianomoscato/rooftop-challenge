from block_sorter.block_sorter import BlockSorter


def check(blocks: list[str], token: str) -> list[str]:
    sorter = BlockSorter(blocks=blocks, token=token)
    sorter.sort()
    return sorter.sorted
