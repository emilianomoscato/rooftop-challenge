import argparse
import sys

from block_sorter.block_sorter import BlockSorter

parser = argparse.ArgumentParser()
parser.add_argument(
    "email",
    nargs="?",
    help="email to be used to query the API. If token is provided email is not used",
)
parser.add_argument("-t", "--token", help="token to be used to query the API instead of email")
args = parser.parse_args()

if args.token:
    sorter = BlockSorter(token=args.token)
elif args.email:
    sorter = BlockSorter(email=args.email)
else:
    parser.print_help(sys.stderr)
    sys.exit(1)

sorter.sort()
success = sorter.validate()
sorted_str = "".join(sorter.sorted)
print(f"Sorter made {sorter.api_check_calls} calls to check blocks")
print(f"Sorted blocks: {sorted_str}")
if success:
    print("Validated response!")
else:
    print("Incorrect result :-(")
