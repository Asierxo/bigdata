from operator import itemgetter
import sys

current_word = None
current_count = 0
max_len= 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line=line.lower()

    # parse the input we got from mapper.py
    word, count, max_word_len = line.split('\t')
    try:
      count = int(count)
      max_word_len= int(max_word_len)
    except ValueError:
      #count was not a number, so silently
      #ignore/discard this line
      continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        if max_word_len>max_len:
                max_len=max_word_len
        current_count += count
    else:
        if current_word:
            if max_word_len>max_len:
                max_len=max_word_len
            # write result to STDOUT
            print ('%s\t%s\t%s' % (current_word, current_count, max_len))
        current_count = count
        max_len=max_word_len
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    if max_word_len>max_len:
        max_len=max_word_len
    print( '%s\t%s\t%s' % (current_word, current_count, max_len))
