import re
from unicodedata import normalize
import sys
import io
import re
import nltk
import string
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

stop_words = stopwords.words('spanish') + stopwords.words('french')
stop_words = set(stop_words)
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='latin1')
for line in input_stream:
  line = line.strip()
  line = re.sub(r'[^\w\s]', '',line)
  line = line.lower()
  for x in line:
    if x in punctuations:
      line=line.replace(x, " ") 

  words=line.split()
  for word in words: 
    if word not in stop_words:
        
        word = re.sub(
                r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
                normalize( "NFD", word), 0, re.I
            )

        # -> NFC
        word = normalize( 'NFC', word)
        letra = word[0:1]
        if letra in list('abcdefghijklmnñopqrstuvwxyzç'):
          print('%s\t%s' % (letra, 1))
