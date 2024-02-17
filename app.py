from datasets import load_dataset
from clean_prepare import clean_and_prepare
from down_csv import download_csv
import numpy as np
import pandas as pd

#? Implementacion parte 1
#* Se carga el conjunto de datos
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

#* Acceder a la característica 'age' y convertirla a un arreglo de NumPy
ages = np.array(data['age'])
has_anemia = np.array(data['has_anaemia'])

#* Calcular el promedio de edad
average_age = np.mean(ages)
#* Calcular las personas con anemia
sum_has_anemia = np.sum(has_anemia)

# TODO: print(has_anemia) 
# TODO: print(data)
# TODO: print(ages)
print(f"\n{sum_has_anemia} personas tienen anemia.")
print(f"El promedio de edad de las personas participantes en el estudio es: {average_age:.2f}\n" )


#?Implementacion parte 2
#* Convertir el Dataset a un DataFrame de Pandas
df = pd.DataFrame(data)

dead_df = df[df['is_dead'] == 1]
survived_df = df[df['is_dead'] == 0]

av_age_dead = dead_df['age'].mean()
av_age_survived = survived_df['age'].mean()

print(f"Promedio de edad de personas que perecieron: {av_age_dead:.2f}")
print(f"Promedio de edad de personas que sobrevivieron: {av_age_survived:.2f}")

#? Implementacion Parte 3
#Primera forma de verlo
smoker_counts = df.groupby(['is_male', 'is_smoker']).size().unstack()

# Cambiar nombres de las columnas
smoker_counts.columns = ['No Fumador', 'Fumador']
# Cambiar nombres de los índices(Filas)
smoker_counts.index = ['Mujer', 'Hombre']

print("\nCantidad de hombres fumadores vs mujeres fumadoras:")
print(f"{smoker_counts}\n")

#Segunda forma de verlo
df_men = df[df['is_male'] == 1]
df_women = df[df['is_male'] == 0]
num_smoking_men = df_men[df_men['is_smoker'] == 1]['is_smoker'].count()
num_smoking_women = df_women[df_women['is_smoker'] == 1]['is_smoker'].count()

print(f"Hombres fumadores: {num_smoking_men}") 
print(f"Mujeres fumadoras: {num_smoking_women}\n")


#? Implementacion API, parte 4
url = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'


download_csv(url, 'data5.csv')

df = pd.read_csv('data4.csv')
df_cleaned = clean_and_prepare(df)