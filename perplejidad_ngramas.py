import re
from nltk.util import pad_sequence
from nltk.util import ngrams
from nltk.lm.preprocessing import pad_both_ends
from nltk import word_tokenize, sent_tokenize 
from nltk import tokenize
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import Vocabulary

filename="canciones_generadas.txt"
with open(filename, encoding='utf-8-sig') as f:
  text = f.read()
text=text.lower()
text=re.sub('([!"#$%&()*+,-./:;<=>?@[\]^_`{|}~])', '', text)
text=re.sub('\s{2,}', ' ', text)
text=re.sub(',','',text)


#entrenamos al modelo
train_sentences = text.splitlines()

train_tokenized_text = [list(map(str.lower, tokenize.word_tokenize(sent))) 
                for sent in train_sentences]
#en este caso usamos trigramas
n = 3
train_data, padded_vocab = padded_everygram_pipeline(n, train_tokenized_text)
model = MLE(n)
model.fit(train_data, padded_vocab) 


filename="texto_generado.txt"
with open(filename, encoding='utf-8-sig') as f:
  prueba = f.read()
prueba=prueba.lower()
prueba=re.sub('([!"#$%&()*+,-/:;<=>?@[\]^_`{|}~])', '', prueba)
prueba=re.sub('\s{2,}', ' ', prueba)
prueba=re.sub(',','',prueba)


sentences = prueba.splitlines()

test_sentences = []
for oracion in sentences:
    if(len(oracion)>0):
        test_sentences.append(oracion)


test_tokenized_text = [list(map(str.lower, tokenize.word_tokenize(sent))) 
                for sent in test_sentences]
test_data, _ = padded_everygram_pipeline(n, test_tokenized_text)
average = []
number_verses = 0
no_validos = 0
aux = 1
#calculamos la perplejidad de cada verso, contamos el numero de trigramas no validos y sacamos un promedio del texto
for test in test_data:
    aux = float(model.perplexity(test))
    if(aux > 5000):
        aux = 2000
        no_validos +=1
    average.append( aux )
    number_verses += 1
print(no_validos,average/number_verses)
