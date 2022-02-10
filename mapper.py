# Es el teu arxiu modificat amb l'ajuda d'un post d'stackoverflow de https://es.stackoverflow.com/questions/135707/c%C3%B3mo-puedo-reemplazar-las-letras-con-tildes-por-las-mismas-sin-tilde-pero-no-l

import re
from unicodedata import normalize
import sys
import io
import re
import nltk
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Juntar totes les stopwords de tots els idiomes utilizats: català, castellà, anglès i francès
stop_words = stopwords.words('english') + stopwords.words('spanish') + stopwords.words('french')
stop_words = set(stop_words)
# Llegim cada línia dels arxius i els netejam, utilizam l'encoding 
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
for line in input_stream:
  line = line.strip()
  line = re.sub(r'[^\w\s]', '',line)
  line = line.lower()
  for x in line:
    if x in punctuations:
      line=line.replace(x, " ") 

  words=line.split()
# Llevam accents amb un codi d'internet que te lleva els accents menys la Ñ, abans l'he posat un if perquè tampoc llevi la ç
  for word in words: 
    if word not in stop_words:
      if word[0:1]!='ç':
        word = re.sub(
                r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
                normalize( "NFD", word), 0, re.I
            )
        # -> NFC
        word = normalize( 'NFC', word)
        
      letra = word[0:1]
      if letra in list('abcçdefghijklmnñopqrstuvwxyz'):
        print('%s\t%s\t%s' % (letra, 1, len(word)))
