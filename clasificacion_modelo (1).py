# -*- coding: utf-8 -*-
"""clasificacion_modelo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19Vw1zpNS6wceiUKTkh_Adm1XCCg2PYnb
"""

# Importación de las bibliotecas necesarias
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler

from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Cargar los datos desde un archivo CSV
df_filtered = pd.read_csv('/content/sample_data/dataset_muestra_representativa_para_cluster.csv')

# Verificar la estructura del DataFrame
print(df_filtered.head())
print(df_filtered.info())

#ORIGINAL
# Paso 3: Calcular inercia y coeficiente de silueta para diferentes valores de k
inertia = []
silhouette_scores = []
range_clusters = range(2, 10)  # Reducimos el rango para facilitar depuración
results = []

for k in range_clusters:
    try:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        inertia_value = kmeans.inertia_
        labels = kmeans.labels_
        silhouette_avg = silhouette_score(X_scaled, labels)

        # Guardar resultados
        inertia.append(inertia_value)
        silhouette_scores.append(silhouette_avg)
        results.append({
            'Número de Clústeres (k)': k,
            'Inercia': inertia_value,
            'Coeficiente de Silueta': silhouette_avg
        })

        print(f"k={k}: Inercia={inertia_value:.2f}, Silueta={silhouette_avg:.2f}")
    except Exception as e:
        print(f"Error en k={k}: {e}")

# Convertir resultados a DataFrame
results_df = pd.DataFrame(results)

# Verificar si silhouette_scores tiene valores
if silhouette_scores:
    optimal_k = silhouette_scores.index(max(silhouette_scores)) + 2  # +2 porque range_clusters comienza en 2
    print(f"Número óptimo de clústeres basado en Silhouette: {optimal_k}")
else:
    print("No se calcularon valores para el coeficiente de silueta.")

# Graficar resultados si existen datos
if not results_df.empty:
    plt.figure(figsize=(10, 6))
    plt.plot(results_df['Número de Clústeres (k)'], results_df['Inercia'], marker='o', linestyle='--', label='Inercia')
    plt.title('Método del Codo para Selección de Clústeres')
    plt.xlabel('Número de Clústeres (k)')
    plt.ylabel('Inercia')
    plt.legend()
    plt.grid()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(results_df['Número de Clústeres (k)'], results_df['Coeficiente de Silueta'], marker='o', linestyle='-', color='orange', label='Coeficiente de Silueta')
    plt.title('Coeficiente de Silueta para Selección de Clústeres')
    plt.xlabel('Número de Clústeres (k)')
    plt.ylabel('Coeficiente de Silueta')
    plt.legend()
    plt.grid()
    plt.show()

# Mostrar la tabla de resultados
print("Tabla de Resultados:")
print(results_df)


# Reentrenar K-Means con el número óptimo de clústeres
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
#kmeans = KMeans(n_clusters=3, random_state=42)

kmeans.fit(X_scaled)
labels = kmeans.labels_

# Calcular el coeficiente de silueta final
silhouette_avg = silhouette_score(X_scaled, labels)
print(f"Coeficiente de silueta para k={optimal_k}: {silhouette_avg:.2f}")

# Agregar los clústeres al DataFrame
df_filtered['CLUSTER'] = labels

# Analizar distribución de los clústeres
print("Distribución de pacientes en cada clúster:")
print(df_filtered['CLUSTER'].value_counts())

# Visualizar los centroides
centroids = kmeans.cluster_centers_
print("Centroides de los clústeres (estandarizados):")
print(centroids)

cluster_summary = df_filtered.groupby('CLUSTER').mean()
print("Resumen de características por clúster:")
print(cluster_summary)

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(10, 8))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', s=50, alpha=0.7)
plt.colorbar(label='Cluster')
plt.title('Visualización de Clústeres con K-Means')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.show()

#CON 3
# Paso 3: Calcular inercia y coeficiente de silueta para diferentes valores de k
inertia = []
silhouette_scores = []
range_clusters = range(2, 10)  # Reducimos el rango para facilitar depuración
results = []

for k in range_clusters:
    try:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        inertia_value = kmeans.inertia_
        labels = kmeans.labels_
        silhouette_avg = silhouette_score(X_scaled, labels)

        # Guardar resultados
        inertia.append(inertia_value)
        silhouette_scores.append(silhouette_avg)
        results.append({
            'Número de Clústeres (k)': k,
            'Inercia': inertia_value,
            'Coeficiente de Silueta': silhouette_avg
        })
    except Exception as e:
        print(f"Error en k={k}: {e}")

# Convertir resultados a DataFrame
results_df = pd.DataFrame(results)

# Verificar si silhouette_scores tiene valores
if silhouette_scores:
    #optimal_k = silhouette_scores.index(max(silhouette_scores)) + 2  # +2 porque range_clusters comienza en 2
    optimal_k = 3
    print(f"Número óptimo de clústeres basado en Silhouette: {optimal_k}")
else:
    print("No se calcularon valores para el coeficiente de silueta.")

# Graficar resultados si existen datos
if not results_df.empty:
    plt.figure(figsize=(10, 6))
    plt.plot(results_df['Número de Clústeres (k)'], results_df['Inercia'], marker='o', linestyle='--', label='Inercia')
    plt.title('Método del Codo para Selección de Clústeres')
    plt.xlabel('Número de Clústeres (k)')
    plt.ylabel('Inercia')
    plt.legend()
    plt.grid()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(results_df['Número de Clústeres (k)'], results_df['Coeficiente de Silueta'], marker='o', linestyle='-', color='orange', label='Coeficiente de Silueta')
    plt.title('Coeficiente de Silueta para Selección de Clústeres')
    plt.xlabel('Número de Clústeres (k)')
    plt.ylabel('Coeficiente de Silueta')
    plt.legend()
    plt.grid()
    plt.show()


# Reentrenar K-Means con el número óptimo de clústeres
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
#kmeans = KMeans(n_clusters=3, random_state=42)

kmeans.fit(X_scaled)
labels = kmeans.labels_

# Calcular el coeficiente de silueta final
silhouette_avg = silhouette_score(X_scaled, labels)
print(f"Coeficiente de silueta para k={optimal_k}: {silhouette_avg:.2f}")

# Agregar los clústeres al DataFrame
df_filtered['CLUSTER'] = labels

# Analizar distribución de los clústeres
print("Distribución de pacientes en cada clúster:")
print(df_filtered['CLUSTER'].value_counts())

# Visualizar los centroides
centroids = kmeans.cluster_centers_
print("Centroides de los clústeres (estandarizados):")
print(centroids)

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(10, 8))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', s=50, alpha=0.7)
plt.colorbar(label='Cluster')
plt.title('Visualización de Clústeres con K-Means')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.show()

cluster_summary = df_filtered.groupby('CLUSTER').mean()
print("Resumen de características por clúster:")
print(cluster_summary)

df_filtered.to_csv('resultados_clustering.csv', index=False)
print("Resultados guardados en 'resultados_clustering.csv'.")

import seaborn as sns
import matplotlib.pyplot as plt

# Visualización: Distribución de edades por clúster
plt.figure(figsize=(10, 6))
sns.boxplot(x='CLUSTER', y='NIVEL_ENFERMEDAD', data=df_filtered)
plt.title('Distribución de Nivel de la enfermedad por Clúster')
plt.xlabel('Clúster')
plt.ylabel('Nivel de la enfermedad')
plt.show()


# Visualización: Distribución de edades por clúster
plt.figure(figsize=(10, 6))
sns.boxplot(x='CLUSTER', y='ESTADIO_TFG', data=df_filtered)
plt.title('Distribución de ESTADIO_TFG por Clúster')
plt.xlabel('Clúster')
plt.ylabel('ESTADIO_TFG')
plt.show()

# Visualización: Promedio de otras variables por clúster
cluster_means = df_filtered.groupby('CLUSTER').mean().reset_index()
cluster_means.plot(kind='bar', x='CLUSTER', figsize=(12, 8))
plt.title('Promedio de Variables Clave por Clúster')
plt.xlabel('Clúster')
plt.ylabel('Promedio')
plt.legend(loc='upper right')
plt.show()

from sklearn.metrics import pairwise_distances_argmin_min
import numpy as np

# Calcular la distancia mínima de cada punto a su centroide
_, distances = pairwise_distances_argmin_min(kmeans.cluster_centers_, X_scaled)
intra_cluster_distance = distances.sum()
print(f"Intra-cluster distance: {intra_cluster_distance}")

from scipy.spatial.distance import cdist

# Calcular distancias entre los centroides
inter_cluster_distance = np.mean(cdist(kmeans.cluster_centers_, kmeans.cluster_centers_))
print(f"Inter-cluster distance: {inter_cluster_distance}")

import seaborn as sns

# Calcular distancias entre centroides
dist_matrix = cdist(kmeans.cluster_centers_, kmeans.cluster_centers_)

# Crear el heatmap
sns.heatmap(dist_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Distancia entre centroides (Inter-cluster)")
plt.xlabel("Clúster")
plt.ylabel("Clúster")
plt.show()

from mpl_toolkits.mplot3d import Axes3D

# PCA para 3 componentes
pca_3d = PCA(n_components=3)
X_pca_3d = pca_3d.fit_transform(X_scaled)

# Gráfica en 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(X_pca_3d[:, 0], X_pca_3d[:, 1], X_pca_3d[:, 2], c=labels, cmap='viridis', s=50, alpha=0.7)
plt.colorbar(sc, label='Cluster')
ax.set_title('Visualización 3D de Clústeres')
ax.set_xlabel('Componente Principal 1')
ax.set_ylabel('Componente Principal 2')
ax.set_zlabel('Componente Principal 3')
plt.show()

import pickle

# Guardar el escalador en un archivo .pkl
with open('scaler.pkl', 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

# Guardar el modelo K-Means en un archivo .pkl
with open('kmeans.pkl', 'wb') as kmeans_file:
    pickle.dump(kmeans, kmeans_file)

print("El escalador y el modelo K-Means han sido guardados exitosamente:")
print("Archivos generados: 'scaler.pkl' y 'kmeans.pkl'")

import pandas as pd
import pickle

# Paso 1: Cargar el scaler y el modelo K-Means
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('kmeans.pkl', 'rb') as kmeans_file:
    kmeans = pickle.load(kmeans_file)

# Verificar las columnas originales del scaler
print("Columnas originales del scaler:")
print(scaler.feature_names_in_)

def calcular_tfg(creatinina, edad, es_mujer=True):
    """
    Calcula la Tasa de Filtración Glomerular (TFG) usando la fórmula CKD-EPI.

    Args:
        creatinina (float): Nivel de creatinina sérica en mg/dL.
        edad (int): Edad del paciente en años.
        es_mujer (bool): Indica si el paciente es mujer (True) o no (False).

    Returns:
        float: Tasa de Filtración Glomerular (TFG) estimada en mL/min/1.73m².
    """
    # Constantes de la fórmula CKD-EPI
    k = 0.7 if es_mujer else 0.9
    alfa = -0.329 if es_mujer else -0.411
    f = 1.018 if es_mujer else 1.0
    g = 1.159  # Factor común para todas las personas

    # Fórmula CKD-EPI
    tfg = 141 * min(creatinina / k, 1) ** alfa * max(creatinina / k, 1) ** -1.209 * 0.993 ** edad * f * g
    return round(tfg, 2)

# Ejemplo de uso
tfg_ejemplo = calcular_tfg(creatinina=1.2, edad=50, es_mujer=False)
print(f"TFG Calculada: {tfg_ejemplo} mL/min/1.73m²")

# Paso 3: Función para clasificar pacientes
def clasificar_paciente(age, creatinina, glucosa, presion, sod=140, pot=4.5, hemo=13, bu=20):
    """
    Clasifica a un paciente en un clúster basado en sus datos y genera un informe.
    """
    # Calcular TFG
    tfg = calcular_tfg(creatinina, age, es_mujer=False)

    # Escalar los datos del paciente con las características utilizadas en el modelo
    patient_data = pd.DataFrame([[age, presion, glucosa, bu, creatinina, sod, pot, hemo]],
                                 columns=['EDAD_PACIENTE', 'bp', 'bgr', 'bu', 'CREATININA', 'sod', 'pot', 'HEMOGLOBINA'])

    # Ajustar nombres para que coincidan con el modelo entrenado
    patient_data = patient_data.rename(columns={
        'bp': 'PRESION_ARTERIAL',
        'bgr': 'GLUCOSA',
        'bu': 'UREA',
        'sod': 'SODIO',
        'pot': 'POTASIO',
        'CREATININA': 'CREATININA',
        'HEMOGLOBINA': 'HEMOGLOBINA',
        'EDAD_PACIENTE': 'EDAD_PACIENTE'
    })

    # Verificar que todas las columnas esperadas estén presentes
    columnas_faltantes = [col for col in scaler.feature_names_in_ if col not in patient_data.columns]
    for col in columnas_faltantes:
        patient_data[col] = 0  # Valor predeterminado

    # Reordenar las columnas para que coincidan exactamente con las esperadas por el escalador
    patient_data = patient_data[list(scaler.feature_names_in_)]

    # Escalar los datos del paciente
    patient_scaled = scaler.transform(patient_data)

    # Predecir el clúster usando el modelo entrenado
    cluster = kmeans.predict(patient_scaled)[0]

    # Generar un informe clínico
    recomendaciones = {
        0: "Paciente saludable con función renal normal. Se recomienda mantener hábitos saludables.",
        1: "Paciente con función renal moderadamente reducida. Es necesario realizar monitoreo frecuente.",
        2: "Paciente con daño renal severo. Se recomienda atención médica inmediata y tratamiento especializado."
    }

    informe = {
        "TFG (mL/min/1.73m²)": tfg,
        "Clúster asignado": cluster,
        "Estado clínico": recomendaciones.get(cluster, "Estado desconocido. Requiere evaluación adicional."),
        "Datos del paciente": {
            "Edad": age,
            "Creatinina (mg/dL)": creatinina,
            "Glucosa (mg/dL)": glucosa,
            "Presión Arterial (mmHg)": presion,
            "Sodio (mEq/L)": sod,
            "Potasio (mEq/L)": pot,
            "Hemoglobina (g/dL)": hemo,
            "Urea (mg/dL)": bu
        }
    }
    return informe

# Ejemplo: Clasificar un paciente
paciente_ejemplo = clasificar_paciente(age=60, creatinina=6.0, glucosa=200, presion=85)

# Mostrar el informe generado
print(paciente_ejemplo)

import seaborn as sns
import matplotlib.pyplot as plt

# Asegurarte de que la columna CLUSTER es categórica para las visualizaciones
df_filtered['CLUSTER'] = df_filtered['CLUSTER'].astype(str)

# Pairplot para analizar relaciones entre variables clave
sns.pairplot(
    df_filtered,
    vars=['EDAD_PACIENTE', 'CREATININA', 'NIVEL_ENFERMEDAD', 'ESTADIO_TFG'],
    hue='CLUSTER',
    palette='Set2'
)
plt.suptitle('Relación de Variables por Clúster', y=1.02)
plt.show()

# Gráfico de caja (boxplot) para analizar la distribución de creatinina por clúster
plt.figure(figsize=(10, 6))
sns.boxplot(x='CLUSTER', y='CREATININA', data=df_filtered, palette='viridis')
plt.title('Distribución de Creatinina por Clúster')
plt.xlabel('Clúster')
plt.ylabel('Creatinina sérica (mg/dL)')
plt.show()

# Gráfico de caja (boxplot) para analizar la distribución de nivel de enfermedad por clúster
plt.figure(figsize=(10, 6))
sns.boxplot(x='CLUSTER', y='NIVEL_ENFERMEDAD', data=df_filtered, palette='viridis')
plt.title('Distribución de Nivel de Enfermedad por Clúster')
plt.xlabel('Clúster')
plt.ylabel('Nivel de Enfermedad')
plt.show()

# Gráfico de barras para promedio de las variables por clúster
cluster_means = df_filtered.groupby('CLUSTER').mean().reset_index()

# Melt para graficar en forma larga (long-form data)
cluster_means_melted = cluster_means.melt(id_vars=['CLUSTER'], var_name='Variable', value_name='Promedio')

plt.figure(figsize=(12, 8))
sns.barplot(data=cluster_means_melted, x='CLUSTER', y='Promedio', hue='Variable', palette='viridis')
plt.title('Promedio de Variables por Clúster')
plt.xlabel('Clúster')
plt.ylabel('Promedio')
plt.legend(loc='upper right')
plt.show()