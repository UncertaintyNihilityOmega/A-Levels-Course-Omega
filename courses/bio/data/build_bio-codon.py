# data/build_bio-codon.py: writes widgets/bio-codon.js from data/bio-codon.src.js, replacing the /*@@CODE@@*/ marker by the
# genetic code generated (and asserted: 64 codons, 61 sense, 3 stop) by data/codon_table.py. Run: py data/build_bio-codon.py
import os, sys
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import codon_table
src = open(os.path.join(here, "bio-codon.src.js"), encoding="utf-8").read()
assert "/*@@CODE@@*/" in src
out = src.replace("/*@@CODE@@*/", codon_table.js_block())
open(os.path.join(os.path.dirname(here), "widgets", "bio-codon.js"), "w", encoding="utf-8", newline="\n").write(out)
print("wrote widgets/bio-codon.js:", len(out), "bytes")
