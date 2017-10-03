#!/usr/bin/env python
import sys
sys.path.append('../../lib/fileParsers')

import GeneData

data = GeneData.GenomicRanges()

data.addRange("1", 10, 30)
data.addRange("1", 10, 15)
data.addRange("chr1", 1, 15)
data.addRange("X", 10, 30)
data.addRange("X", 100, 15)
data.addRange("2", 1, 15)

print(data.ranges)
