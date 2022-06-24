from block_sorter.block_sorter import BlockSorter


def run_check(blocks: list[str], token: str) -> list[str]:
    sorter = BlockSorter(blocks=blocks, token=token)
    sorter.sort()
    print(f"Solved using {sorter.api_check_calls} block check api calls.")
    return sorter.sorted
