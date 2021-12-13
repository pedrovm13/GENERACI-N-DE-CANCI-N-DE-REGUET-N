from syltippy import syllabize

import re
filename="texto_generado.txt"
metrica = []

with open(filename, encoding='utf-8-sig') as f:
  text = f.read()
text=text.lower()
text=re.sub('([!"#$%&()*+,-/:;<=>?@[\]^_`{|}~])', '', text)
text=text.replace('..', '.')
text=text.replace('®','')
text = text.replace('|','')
text = text.splitlines()
versos = []
#tomamos los versos de cada cancion
for linea in text:
  if len(linea)>0:
    versos.append(linea.strip())
    
import random
#utilizamos 'syllabize' para medir las silbas de cada oración
i=0
metrica =[]
for verso in versos:
   syllables, stress = syllabize(verso)
   metrica.append(len(syllables))   
  
data= open("numero_silabas.dat","w+")
for silabas in metrica:
    data.write(str(silabas)+'\n')
    
data.close()
