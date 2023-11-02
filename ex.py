import pandas as pd
import matplotlib.pyplot as plt

# Carregue o conjunto de dados
url = "https://raw.githubusercontent.com/alfaneo-ai/brazilian-legal-text-dataset/main/resources/raw/pesquisas_prontas_stj.csv"
df = pd.read_csv(url)

# Conte o número de amostras em cada classe
class_counts = df['classe'].value_counts()

# Crie um gráfico de barras para visualizar o desbalanceamento
plt.figure(figsize=(10, 6))
class_counts.plot(kind='bar', color='skyblue')
plt.title('Distribuição das Classes')
plt.xlabel('Classes')
plt.ylabel('Número de Amostras')
plt.xticks(rotation=45)
plt.show()