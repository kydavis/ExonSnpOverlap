import sys
from random import random

def main(argc, argv):
	if (argc != 5):
		print("Usage: <number> <unique chrom> <length> <range>")
	for i in range(0, int(argv[1])):
		chrom = int(random() * int(argv[2]))
		start = int(random() * int(argv[3]))
		end = start + int(random() * int(argv[4]))
		print("{} {} {}".format(chrom, start, end))

main(len(sys.argv), sys.argv)
