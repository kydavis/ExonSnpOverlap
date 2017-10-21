from lib.IntervalTree import IntervalTree
import sys

def addInterval(dic, key, s1, s2):
	interval = [int(s1), int(s2)]
	start = min(interval)
	end = max(interval)
	if key in dic:
		dic[key].append((start, end))
	else:
		dic[key] = [(start,end)]

def parseGFF(file_name):
	ret = {}
	with open(file_name, "rb") as gff:
		for entry in gff:
			split = entry.split()
			addInterval(ret, split[0], split[3], split[4])
	return (ret)

def parseBED(file_name):
	ret = {}
	with open(file_name, "rb") as bed:
		for entry in bed:
			split = entry.split()
			addInterval(ret, split[0], split[1], split[2])
	return (ret)

def parseFile(file_name):
	if (file_name[-4:] == ".gff"):
		return (parseGFF(file_name))
	elif(file_name[-4:] == ".bed"):
		return (parseBED(file_name))
	else:
		raise ValueError("Must take either GFF file or BED file")
		

def main(argc, argv):
	if (argc != 3):
		print("Takes two files of either GFF or BED format")
		return (-1)
	base = parseFile(argv[1])
	search = parseFile(argv[2])
	for chrom in base:
		base[chrom].sort()
		baseTree = IntervalTree(base[chrom])
		print("Chromosome:{}".format(chrom))
		if chrom in search:
			search[chrom].sort()
			for interval in search[chrom]:
				overlap = baseTree.querey(interval)
				print("\tQuerey:{}\n\tOverlaps {}\n".format(interval, overlap))

main(len(sys.argv), sys.argv)
