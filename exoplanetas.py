import pandas as pd
import matplotlib.pyplot as plt
import math as m
import numpy as np

plt.rcParams.update({'font.size': 12})

def cargar_datos(nombre_archivo:str)->pd.DataFrame:
    """ Carga los datos de un archivo csv y retorna el DataFrame con la informacion.
    Parametros:
        nombre_archivo (str): El nombre del archivo CSV que se debe cargar
    Retorno:
        (DataFrame) : El DataFrame con todos los datos contenidos en el archivo
    """
    data = pd.read_csv(nombre_archivo)
    
    return data


def histograma_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un histograma con 30 grupos (bins) en el que debe
        aparecer la cantidad de planetas descubiertos por anho.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    plt.hist(datos['DESCUBRIMIENTO'], bins=30, color=['Cyan'], edgecolor='black', linewidth=0.4) 
    plt.title('Cantidad de Planetas Descubiertos entre 1988 y 2018')
    plt.ylabel('Cantidad Planetas')
    plt.xlabel('Años')
    plt.show()
    

def estado_publicacion_por_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por anho, agrupados de acuerdo con el tipo de publicacion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    # agrupar los datos según la columna 'ESTADO_PUBLICACION'
    grouped_data = datos.groupby('ESTADO_PUBLICACION')['DESCUBRIMIENTO'].apply(list)

    # crear una lista de nombres de grupos para usar como etiquetas en el gráfico
    group_labels = list(grouped_data.index)


    # crear el gráfico de boxplot
    fig, ax = plt.subplots()
    meanpointprops = {'marker': 'D',
                      'markeredgecolor': 'black',
                      'markerfacecolor': 'firebrick'}
    ax.boxplot(grouped_data.tolist(), labels=group_labels, showmeans=True, meanline=True, 
    meanprops=meanpointprops)
    ax.set_xlabel('TIPO PUBLICACION')
    ax.set_ylabel('AÑO DESCUBRIMIENTO')
    ax.set_title("DESCUBRIMIENTO POR TIPO DE PUBLICACION")
    ax.set_xticklabels(group_labels, rotation=90)
    plt.show()
    
   
   

def deteccion_por_descubrimiento(datos:pd.DataFrame)->None:
    """ Calcula y despliega un BoxPlot donde aparecen la cantidad de planetas
        descubiertos por anho, agrupados de acuerdo con el tipo de deteccion
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    # agrupar los datos según la columna 'TIPO_DETECCION'
    grouped_data = datos.groupby('TIPO_DETECCION')['DESCUBRIMIENTO'].apply(list)

    # crear una lista de nombres de grupos para usar como etiquetas en el gráfico
    group_labels = list(grouped_data.index)


    # crear el gráfico de boxplot
    fig, ax = plt.subplots()
    meanpointprops = {'marker': 'D',
                      'markeredgecolor': 'black',
                      'markerfacecolor': 'firebrick'}
    ax.boxplot(grouped_data.tolist(), labels=group_labels, showmeans=True, meanline=True, 
    meanprops=meanpointprops)
    ax.set_xlabel('TIPO DETECCION')
    ax.set_ylabel('AÑO DESCUBRIMIENTO')
    ax.set_title("DESCUBRIMIENTO POR TIPO DE DETECCION")
    ax.set_xticklabels(group_labels, rotation=90)
    plt.show()

def deteccion_y_descubrimiento(datos:pd.DataFrame,anho:int)->None:
    """ Calcula y despliega un diagrama de pie donde aparecen la cantidad de
        planetas descubiertos en un anho particular, clasificados de acuerdo
        con el tipo de publicacion.
        Si el anho es 0, se muestra la información para todos los planetas.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
        anho (int): el anho para el que se quieren analizar los planetas descubiertos
                    o 0 para indicar que deben ser todos los planetas.
    """
   
    # Calcular el número de ocurrencias de cada tipo de detección
    grouped_data = datos.groupby('TIPO_DETECCION')['DESCUBRIMIENTO'].count() 
    grouped_year = datos[datos['DESCUBRIMIENTO']==anho]['TIPO_DETECCION'].value_counts()
    
    # Crear un gráfico de torta general
    plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%', wedgeprops=
       {'edgecolor':'white'}, textprops = {"fontsize":9}, labeldistance=1.34)
    plt.title('Tipos de Deteccion por Año de Descubrimiento',fontweight="bold")
    plt.figure(figsize=(6,8))
    plt.show()
    
    # Crear un grafico por anio
    plt.pie(grouped_year, labels=grouped_year.index,autopct='%1.1f%%',  wedgeprops=
       {'edgecolor':'white'}, textprops = {"fontsize":11}, labeldistance=1.25, counterclock=False)
    plt.title(f'Tipo de Deteccion para el Año {anho}',fontweight="bold")
    plt.figure(figsize=(6,8))
    plt.show()


def cantidad_y_tipo_deteccion(datos:pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de lineas donde aparece una linea por
        cada tipo de deteccion y se muestra la cantidad de planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    # Agrupar los datos por tipo de detección
    grouped_data = datos.groupby('TIPO_DETECCION')
    
    # Crear el diccionario vacío
    detection_dict = {}
    
    # Recorrer cada grupo
    for name, group in grouped_data:
        # Agrupar los datos por año y contar la cantidad
        year_group = group.groupby('DESCUBRIMIENTO').size()
        detection_dict[name] = year_group
        
    # Crear un nuevo DataFrame a partir del diccionario
    df_detection = pd.DataFrame.from_dict(detection_dict)
    df_detection = df_detection.fillna(0)
    
    # Crear Grafica
    fig, ax = plt.subplots()
    
    # Recorrer cada columna del DataFrame
    colors = ['#ff0000','#00ff00','#0000ff','#008080','#ffa500','#800080','#808080','#000000','#00ffff']

    for i, column in enumerate(df_detection.columns):
         ax.plot(df_detection.index, df_detection[column], label=column, color=colors[i], )
         
    # Establecer el título del gráfico
    ax.set_title("Cantidad de planetas descubiertos por tipo de detección", weight='bold')
    
    # Establecer etiquetas para los ejes
    ax.set_xlabel("Año Descubrimiento")
    ax.set_ylabel("Cantidad de planetas")
    
    # Mostrar la leyenda
    ax.legend()
    
    # Mostrar el gráfico
    plt.show()
    


def masa_promedio_y_tipo_deteccion(datos:pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de lineas donde aparece una linea por
        cada tipo de detección y se muestra la masa promedio de los planetas descubiertos
        en cada anho, para ese tipo de deteccion.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    
    # Agrupar los datos por tipo de detección
    grouped_data = datos.groupby('TIPO_DETECCION')
    
    # Crear el diccionario vacío
    detection_dict = {}
    
    # Recorrer cada grupo
    for name, group in grouped_data:
        # Agrupar los datos por año y contar la cantidad
        year_group = group.groupby('DESCUBRIMIENTO')['MASA'].mean()
        detection_dict[name] = year_group
        
    # Crear un nuevo DataFrame a partir del diccionario
    df_detection = pd.DataFrame.from_dict(detection_dict)
    df_detection = df_detection.fillna(0)
    
    # Crear Grafica
    fig, ax = plt.subplots()
    
    # Recorrer cada columna del DataFrame
    colors = ['#ff0000','#00ff00','#0000ff','#008080','#ffa500','#800080','#808080','#000000','#00ffff']

    for i, column in enumerate(df_detection.columns):
          ax.plot(df_detection.index, df_detection[column], label=column, color=colors[i], )
         
    # Establecer el título del gráfico
    ax.set_title("Masa Promedio por Año y Tipo de Detección", weight='bold')
    
    # Establecer etiquetas para los ejes
    ax.set_xlabel("Año Descubrimiento")
    ax.set_ylabel("Masa promedio")
    
    # Mostrar la leyenda
    ax.legend()
    
    # Mostrar el gráfico
    plt.show()


def masa_planetas_vs_masa_estrellas(datos: pd.DataFrame)->None:
    """ Calcula y despliega un diagrama de dispersión donde en el eje x se
        encuentra la masa de los planetas y en el eje y se encuentra el logaritmo
        de la masa de las estrellas. Cada punto en el diagrama correspondera
        a un planeta y estara ubicado de acuerdo con su masa y la masa de la
        estrella más cercana.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    """
    # Crear el gráfico de dispersión
    plt.scatter(datos['MASA'], datos['MASA_ESTRELLA'])
    
    # Escala logaritmica
    plt.yscale('log')
    
    # Añadir título y etiquetas de ejes
    plt.title('Masa Planetas VS Masa Estrella mas Cercana', weight='bold')
    plt.xlabel('Masa Planeta')
    plt.ylabel('Masa Estrella')
    
    # Mostrar el gráfico
    plt.show()


def graficar_cielo(datos:pd.DataFrame)->list:
    """ Calcula y despliega una imagen donde aparece un pixel por cada planeta,
        usando colores diferentes que dependen del tipo de detección utilizado
        para descubirlo.
    Parametros:
        datos (DataFrame): el DataFrame con la informacion de los exoplanetas
    Retorno:
        Una matriz de pixeles con la representacion del cielo
    """
    pixels_dict = {'Microlensing':(0.94, 0.10, 0.10),
                   'Radial Velocity':(0.1, 0.5, 0.94),
                   'Imaging':(0.34, 0.94, 0.10),
                   'Primary Transit':(0.10, 0.94, 0.85),
                   'Other':(0.94, 0.10, 0.85),
                   'Astrometry':(0.94, 0.65, 0.10),
                   'TTV':(1, 1, 1) 
                   }
    
    # Crear un array de 100x200 con todos los elementos en 0 (negro)
    imagen = np.zeros((100,200,3), dtype=np.uint8)
    
    # Calcular fila
    def calcular_fila(datos:pd.DataFrame)->pd.DataFrame:
        datos = datos.copy()
        datos['seno'] = datos['RA'].apply(lambda x: m.sin(m.radians(x)))
        datos['coseno'] = datos['DEC'].apply(lambda x: m.cos(m.radians(x)))
        datos['fila'] = datos.apply(lambda x: 99 - abs(x['seno'] * x['coseno'] * 100), axis=1)
        return datos['fila'] 
    
    # Calcular Columna
    def calcular_columna(datos:pd.DataFrame)->pd.DataFrame:
        datos = datos.copy()
        datos['coseno_2'] = datos['RA'].apply(lambda x: m.cos(m.radians(x)))
        datos['coseno_3'] = datos['DEC'].apply(lambda x: m.cos(m.radians(x)))
        datos['columna'] = datos.apply(lambda x: (x['coseno_2'] * x['coseno_3'] * 100)+100, axis=1)
        return datos['columna']
   
    #df fila
    row_df = calcular_fila(datos)
    
    #df columna
    column_df = calcular_columna(datos)
    
    #df pixels
    pixels_df = datos['TIPO_DETECCION'].map(lambda x : pixels_dict.get(x,(0,0,0)))
    
    #df total
    result_df = pd.concat([row_df, column_df,pixels_df], axis=1)
    
    # Recorrer cada fila del dataframe
    for i in range(result_df.shape[0]):
        # Obtener la fila, columna y color de la fila actual
        fila = int(result_df.iloc[i]["fila"])
        columna = int(result_df.iloc[i]["columna"])
        color = tuple(np.array(result_df.iloc[i]["TIPO_DETECCION"])*255)
    
        if fila <100 and columna <200:
             # Modificar el valor del píxel en la posición especifica con el color especifico
             imagen[fila,columna]=color
                 
    # Mostrar Imagen
    plt.imshow(imagen)
    plt.show()
                
    return imagen


def filtrar_imagen_cielo(imagen:list)->None:
    """ Le aplica a la imagen un filtro de convolucion basado en la matriz
        [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
    Parametros:
        imagen (list): una matriz con la imagen del cielo
    """
    # mascara
    mascara = [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
    
    # Obtener dimensiones de la imagen
    filas, columnas = imagen.shape[:2]
   
    # Crear una imagen resultado con las mismas dimensiones
    result = np.zeros_like(imagen) # matriz de ceros con las mismas dimensiones imagen 100X200
    # Recorrer cada píxel de la imagen
    for i in range(1, filas-1): #99
        for j in range(1, columnas-1): #199
            # Aplicar la máscara de convolución
            pixel_result = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    pixel_result += imagen[i+k, j+l] * mascara[k+1][l+1]
            result[i,j] = pixel_result
    
    # Mostrar Imagen
    plt.imshow(imagen)
    plt.show()
               

# df = cargar_datos('exoplanetas.csv')
# histogram = histograma_descubrimiento(df)
# boxplot_1 = estado_publicacion_por_descubrimiento(df)
# boxplot_2 = deteccion_por_descubrimiento(df)
# pie = deteccion_y_descubrimiento(df, 2000)
# line = cantidad_y_tipo_deteccion(df)
# line_2 = masa_promedio_y_tipo_deteccion(df)
# scatter = masa_planetas_vs_masa_estrellas(df)
# imagen = graficar_cielo(df)
# convolution = filtrar_imagen_cielo(imagen, [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])










