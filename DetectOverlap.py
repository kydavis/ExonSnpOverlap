from lib.IntervalTree import IntervalTree
from lib.GeneData import GenomicIntervals
import sys

def parseGFF(file_name):
	ret = GenomicIntervals()
	with open(file_name, "rb") as gff:
		for entry in gff:
			split = entry.split()
			ret.addInterval(split[0], int(split[3]), int(split[4]))
	return (ret)

def parseBED(file_name):
	ret = GenomicIntervals()
	with open(file_name, "rb") as bed:
		for entry in bed:
			split = entry.split()
			ret.addInterval(split[0], int(split[1]), int(split[2]))
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
	for chrom in base.intervals:
		baseTree = IntervalTree(base.intervals[chrom])
		#print("Chromosome:{}".format(chrom))
		if chrom in search.intervals:
			for interval in search.intervals[chrom]:
				overlap = baseTree.querey(interval)
		#		print("Querey:{}\nOverlaps {}".format(interval, overlap))

main(len(sys.argv), sys.argv)
