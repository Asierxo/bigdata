# És el teu reducer modificat perquè retorni a més la paraula més llarga amb aquesta lletra
from operator import itemgetter
import sys

current_lletra = None
current_count = 0
max_len= 0
lletra = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line=line.lower()

    # parse the input we got from mapper.py
    lletra, count, max_lletra_len = line.split('\t')
    try:
      count = int(count)
      max_lletra_len= int(max_lletra_len)
    except ValueError:
      #count was not a number, so silently
      #ignore/discard this line
      continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: lletra) before it is passed to the reducer
    # Comprovam que la dimensió de la lletra és més gran que l'anterior per poder substituir la variable.
    if current_lletra == lletra:
        if max_lletra_len>max_len:
                max_len=max_lletra_len
        current_count += count
    else:
        if current_lletra:
            if max_lletra_len>max_len:
                max_len=max_lletra_len
            # write result to STDOUT
            print ('%s\t%s\t%s' % (current_lletra, current_count, max_len))
        current_count = count
        max_len=max_lletra_len
        current_lletra = lletra

# do not forget to output the last lletra if needed!
if current_lletra == lletra:
    if max_lletra_len>max_len:
        max_len=max_lletra_len
    print( '%s\t%s\t%s' % (current_lletra, current_count, max_len))
