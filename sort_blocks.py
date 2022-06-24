import argparse

from block_sorter.block_sorter import BlockSorter, check

parser = argparse.ArgumentParser()
parser.add_argument("token", help="token to be used to query the API")
parser.add_argument("-b", "--blocks", help="blocks to order in json format")
args = parser.parse_args()

if args.blocks:
    sorted_blocks = check(args.blocks, args.token)
else:
    sorted_blocks = []

sorter = BlockSorter(token=args.token, sorted_blocks=sorted_blocks)
success = sorter.validate()
sorted_str = "".join(sorted_blocks)
print(f"Sorted blocks: {sorted_str}")
if success:
    print(f"Validated response!")
else:
    print("Incorrect result :-(")


