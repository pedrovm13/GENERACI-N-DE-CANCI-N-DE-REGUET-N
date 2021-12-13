import re
filename="texto_generado.txt"
metrica = []

with open(filename, encoding='utf-8-sig') as f:
  text = f.read()
text=text.lower()
text = text.replace('..', '.')
text = text.replace('®','')
text = text.replace("'",'')
text = text.replace('?','')
text = text.replace('|','')
text = text.replace('-','')
text=re.sub('([!"#$%&()*+,.-/:;<=>?@[\]^_`{|}~])', '', text)
text = text.splitlines()
for i in range(0,len(text)):
  text[i] = text[i].strip()  
  
length = len(text)

numero_versos_estrofa =[]
estrofas = []
estrofa = []
for i in range(0,length):
    if(len(text[i]) == 0 and len(estrofa)>0 ):
        estrofas.append(estrofa)
        estrofa =[]
    elif( len(text[i].split()) >0 ):
        estrofa.append(text[i].split()[-1][-3:])
        
#estrofas guarda cada estrofa como una lista
#el primer indice nos da una estrofa
#el segundo indice nos da el verso de la estrofa
#el tercer indice nos da la letra en el verso

numero_rimas1 = []

vocales = ['a','e','i','o','u','á','é','í','ó','ú']
for estrofa in estrofas:
    numero_versos = len(estrofa)
    tablon =  [True for i in range(numero_versos)]
    tablon
    numero_rimas = 0
    for i in range(0,numero_versos-1):
        #Tomamos la última letra de la palabra 'i' 
        rima = estrofa[i][-1]
        if(tablon[i]):
            if( rima in vocales):
                for j in range(i+1,len(estrofa)):
                    if( estrofa[j][-1] == rima ):
                        numero_rimas += 1
                        tablon[j] = False
            else:
                rima = estrofa[i][-2:]
                for j in range(i+1,len(estrofa)):
                    if( estrofa[j][-2:] == rima ):
                        numero_rimas += 1
                        tablon[j] = False 
    numero_rimas1.append(numero_rimas)
 
data= open("numero_rimas_bidi1.dat","w+")
for numero in numero_rimas1:
    #print(numero)
    data.write(str(numero)+'\n')
    
data.close()
