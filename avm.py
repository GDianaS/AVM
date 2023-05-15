import numpy as np
import pandas as pd

n_servidores = 3
filas = np.zeros(n_servidores)

v = np.array([16, 10, 5]) # número de visitas
s = np.array([0.125, 0.3 , 0.2]) # tempo de serviço
q = 0 # número médio de jobs
z = 4 # tempo de pensar
n = 1 #número da iteração

verificador = False # True quando o valor da utilização passa 80% em um dos servidores

results_utilizacao = [] #lista para armazenar as utilizações dos servidores
results_tamFilas = [] #lista para armazenar o tamanho das filas dos servidores
results_resposta = [] #lista para armazenar o tempo de resposta

def check(lista):
    for i in range(n_servidores):
        if(lista[i] >= 0.80): 
            return True 
    return False

while (verificador == False):
    
    n_jobs = np.zeros(n_servidores)
    utilizacao = np.zeros(n_servidores) 
    tempo_resposta = np.zeros(n_servidores)
    
    tempo_resposta_sistema = 0

    for i in range(n_servidores):
        tempo_resposta[i] = round((s[i]*(1 + filas[i])), 4) 
        
    for i in range(n_servidores):
        tempo_resposta_sistema = tempo_resposta_sistema + round(((tempo_resposta[i] * v[i])), 4) 

    for i in range(n_servidores):
        #vazão / throughput
        vazao = round((n / (tempo_resposta_sistema + z)),4)

    for i in range(n_servidores):
        # Utilização [i] = X*Di = X * (Si * Vi) 
        utilizacao[i] = round((vazao * s[i] * v[i]),4)

    for i in range(n_servidores):
        #tamanho da fila[i] = X * Ri * Vi
        filas[i] = round((vazao * tempo_resposta[i] * v[i]),4)

    print("ITERAÇÃO N." + str(n))
    print("Tempo de Resposta dos Servidores: " + str(tempo_resposta))
    print("Tempo de Resposta do Sistema: " + str(tempo_resposta_sistema))
    print("Utilização dos Servidores: " + str(utilizacao))
    print("Vazão do Sistema:" + str(vazao))
    print("Tamanho das filas:" + str(filas))
    print()

    verificador = check(utilizacao)

    if(verificador):
        print("SERVIDOR ATINGIU 80%!!!")
        print()
    
    results_utilizacao.append(utilizacao)
    results_tamFilas.append(filas)
    results_resposta.append(tempo_resposta)

    n = n+1

#Exibir tabela de utilização, tamanho das filas e tempo de resposta
df = pd.DataFrame()
df['Utilizacao'] = results_utilizacao
df['Filas'] = results_tamFilas
df['Tempo_Resposta'] = results_resposta
print(df)