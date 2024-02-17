# proyecto2-numpy
Parte 1: Introducción al análisis de datos

El proyecto de este curso consiste en analizar el conjunto de datos introducido en esta sección, procesarlo, limpiarlo y finalmente ajustar modelos de machine learning para realizar predicciones sobre estos datos.

Vamos a trabajar con un dataset sobre fallo cardíaco

El dataset contiene registros médicos de 299 pacientes que padecieron insuficiencia cardíaca durante un período de seguimiento.
Características Clínicas

    Edad: edad del paciente (años)
    Anemia: disminución de glóbulos rojos o hemoglobina (booleano)
    Presión arterial alta: si el paciente tiene hipertensión (booleano)
    Creatinina fosfoquinasa (CPK): nivel de la enzima CPK en la sangre (mcg/L)
    Diabetes: si el paciente tiene diabetes (booleano)
    Fracción de eyección: porcentaje de sangre que sale del corazón en cada contracción (porcentaje)
    Plaquetas: plaquetas en la sangre (kiloplaquetas/mL)
    Sexo: mujer u hombre (binario)
    Creatinina sérica: nivel de creatinina sérica en la sangre (mg/dL)
    Sodio sérico: nivel de sodio sérico en la sangre (mEq/L)
    Fumar: si el paciente fuma o no (booleano)
    Tiempo: período de seguimiento (días)
    [Objetivo] Evento de fallecimiento: si el paciente falleció durante el período de seguimiento (booleano)

Tu tarea para esta etapa del proyecto integrador es convertir la lista de edades a un arreglo de NumPy y calcular el promedio de edad de las personas participantes en el estudio.
# Parte 2: Carga de datos

Continuando con la anterior sección del proyecto integrador, ahora debes realizar lo siguiente:

    Convertir la estructura Dataset en un DataFrame de Pandas usando pd.DataFrame.
    Separar el dataframe en dos diferentes, uno conteniendo las filas con personas que perecieron (is_dead=1) y otro con el complemento.
    Calcular los promedios de las edades de cada dataset e imprimir.

# Parte 3: Calculando analíticas simples

Continuando con el DataFrame con todos los datos de la anterior subsección, ahora debes:

    Verificar que los tipos de datos son correctos en cada colúmna (por ejemplo que no existan colúmnas numéricas en formato de cadena).
    Calcular la cantidad de hombres fumadores vs mujeres fumadoras (usando agregaciones en Pandas).

# Parte 4: Procesando información en bruto

Imagina que no tuvieramos el acceso fácil de estos datos a través de la librería y tuvieramos que descargar los datos usando requests.

    Realiza un GET request para descargarlos y escribe la respuesta como un archivo de texto plano con extensión csv (no necesitas pandas para esto, sólo manipulación de archivos nativa de Python)
    Agrupa el código para esto en una función reutilizable que reciba como argumento la url.

# Parte 5: Limpieza y preparación de datos

Una vez cargado el csv mediante el request anterior, realiza lo siguiente:

    Verificar que no existan valores faltantes
    Verificar que no existan filas repetidas
    Verificar si existen valores atípicos y eliminarlos
    Crear una columna que categorice por edades
        0-12: Niño
        13-19: Adolescente
        20-39: Jóvenes adulto
        40-59: Adulto
        60-...: Adulto mayor
    Guardar el resultado como csv

Encapsula toda la lógica anterior en una función que reciba un dataframe como entrada.
# Parte 6: Automatizando el proceso

Imagina que los datos que procesaste en anteriores etapas del proyecto integrador se van actualizando cada cierto tiempo, (manteniendo el formato) y la url siempre va apuntando a la versión más actual, en este caso conviene tener automatizado el procesamiento en un script que pedas llamar y siempre te dé un csv limpio y listo para su análisis.

Tu tarea en esta etapa del proyecto consiste en crear un script (un archivo .py) que realice todas las operaciones vistas hasta ahora (desde el módulo de APIS) que al ejecutarse:

    Descargue los datos desde una url
    Convierta todo a un dataframe
    Categorice en grupos
    Exporte un csv resultante

La URL a usar y obtener los datos es: 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'

La url no debe estar definida como una constante en el código, en su lugar usa argumentos por terminal (revisar este enlace) para enviarle la url al programa al ejecutarlo.
# Parte 7: Analizando distribuciones 1

Una vez tenemos los datos exportados por nuestro script de ETL, podemos proceder a realizar gráficas de análisis. En esta etapa del proyecto usa matplotlib para:

    Graficar la distribución de edades con un histograma
    Graficar histogramas agrupado por hombre y mujer:
        cantidad de anémicos
        cantidad de diabéticos
        cantidad de fumadores
        cantidad de muertos

El segundo histograma debe verse así:

# Parte 8: Analizando distribuciones 2

Usando el mismo DataFrame, realiza una gráfica usando subplots, que contenga gráficas de torta que represente las distribuciones de:

    Cantidad de anémicos
    Cantidad de diabéticos
    Cantidad de fumadores
    Cantidad de muertos

La grafica debe verse similar a esta (no es necesario el mismo color)

