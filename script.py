# Download pip and use it to install LingPy
import pip
print(f'Installing LingPy')
pip.main(['install', 'lingpy'])

# Import all LingPy classes
from lingpy import *

# Initialize a LexStat object from wordlist
lex = LexStat('wordlist.tsv')

# Initialize a scoring function based on sound correspondences between Coptic and Egyptian Arabic,
# forcing a recalculation of the existing distribution on each run
# and printing verbose output.
# This is needed to use the LexStat-Infomap clustering method in the next step
lex.get_scorer(verbose=True, force=True)

# Cluster words into cognate sets using LexStat-Infomap method, with a threshold of 0.5
lex.cluster(method='lexstat', threshold=0.5)

# Print output to file
lex.output('tsv',filename='clustering_output', ignore=['scorer'])

# Represent cognate sets as an etymological dictionary,
# where keys represent cognate sets representing keys
# and values are nested lists of words/word IDs for that concept
# across both languages
etd = lex.get_etymdict(ref='lexstatid', entry='concept')

# Define a function to pretty print the etymological dictionary
pretty_print = lambda element: '{0:10}'.format(element[0]) if element != 0 else '{0:10}'.format('-')

# Pretty print language names
print('\t'.join([pretty_print([language]) for language in lex.taxa]))

# Pretty print words in each cognate set
for cognate_set_id, words in etd.items():
  print('\t'.join([pretty_print(word) for word in words]))
