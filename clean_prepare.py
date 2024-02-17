import pandas as pd

def get_age_category(age) -> str:
    age_categories = {
        (0, 12): 'Niño',
        (13, 19): 'Adolescente',
        (20, 39): 'Joven adulto',
        (40, 59): 'Adulto',
        (60, float('inf')): 'Adulto mayor'
    }
    
    for age_range, category in age_categories.items():
        if age_range[0] <= age <= age_range[1]:
            return category

def remove_outliers(df: pd.DataFrame, column: str, threshold: float = 1.5) -> pd.DataFrame:

    # Calculate quartiles and IQR
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    # Filter out rows with outliers
    df = df[~((df[column] < (Q1 - threshold * IQR)) | (df[column] > (Q3 + threshold * IQR)))]

    return df


def clean_and_prepare(df) -> pd.DataFrame:

    # 1. Verificar valores faltantes
    print(f"Valores faltantes por columna: \n{df.isnull().sum()}")

    # 2. Verificar filas duplicadas
    print(f"Valores duplicados: {df.duplicated().sum()}")

    # 3. Verificar y eliminar valores atípicos
    df = remove_outliers(df, 'age')
    df = remove_outliers(df, 'creatinine_phosphokinase')
    
    #ordenar por orden ascendente con la columna 'age'
    df = df.sort_values('age', ascending=True)


    # 4. Crear columna de categoría por edad
    df['age_category'] = df['age'].apply(get_age_category)

    # 5. Guardar resultado como CSV
    df.to_csv('cleaned_data.csv', index=True)

    return df


df = pd.read_csv('data4.csv')
df_cleaned = clean_and_prepare(df )
print(df_cleaned)