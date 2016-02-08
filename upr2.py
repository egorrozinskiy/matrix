import argparse
import sys
parser = argparse.ArgumentParser(
	description='calc'
)
parser.add_argument(
	'values',
	metavar='VALUES',
	nargs='+',
	type=float
)
parser.add_argument(
    '-a',
	'--action',
	type = list,
	nargs='+',
	help='opred znaka'
)
parser.add_argument(
	'-v',
	'--verbose',
	help='vivod virazh'
)

args = parser.parse_args()
if not args.action and not args.verbose:
	print(
		'invalid sign'
	)
	sys.exit(-1)


if args.action[0] == '*':
	print((int(args.values[0]))*(int(args.values[1])))
if args.action[0] == '+':
	print(int((args.values[0]))+int((args.values[1])))
if args.action[0] == '-':
	print(int((args.values[0]))-int((args.values[1])))
if args.action[0] == '/':
	print(float((args.values[0]))/float((args.values[1])))
print ('I am working!')
