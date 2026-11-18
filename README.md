# Audimed – Detección temprana de glosas en cuentas médicas

Sistema de machine learning que identifica las cuentas médicas con riesgo de glosa **antes del cobro**, para que el área de auditoría de una clínica concentre la revisión en las cuentas con más probabilidad de reclamo.

Trabajo fin de máster del **Máster Universitario en Análisis y Visualización de Datos Masivos (UNIR, 2024)**.

## Resultados

| Modelo | Recall glosas (clase 1) | Recall sin glosa (clase 0) | AUC ROC | Tiempo de entrenamiento |
|---|---|---|---|---|
| Random Forest | 31,25 % | 99,99 % | 0,66 | 1 h 35 min |
| Red neuronal (TensorFlow) | 93,75 % | 97,07 % | 0,95 | 35 min |
| **Gradient Boosting (modelo final)** | **93,75 %** | **99,99 %** | **0,97** | **3 min** |

Se eligió Gradient Boosting porque detecta la misma proporción de glosas que la red neuronal, con menos falsos positivos y un tiempo de entrenamiento mucho menor.

## El problema

En Colombia, las entidades responsables del pago revisan las cuentas médicas (facturas) que les envían las clínicas y, si encuentran inconsistencias, generan **glosas** (reclamos). Cada glosa retrasa el recaudo, afecta el flujo de caja y obliga a reprocesar la cuenta. El área de auditoría de la clínica no alcanza a revisar el 100 % de las cuentas antes de facturar, por el volumen que maneja.

Este proyecto propone un modelo que prioriza qué cuentas revisar, a partir del comportamiento histórico de las glosas.

## Datos

- **Fuente:** sistema de historia clínica y ERP de una clínica colombiana, extraídos con SQL desde Oracle, con el detalle de cada ítem facturado.
- **Volumen:** 6.104.443 registros y 53 variables, de septiembre de 2018 a abril de 2024.
- **Variables:** datos de la atención (tipo, estancia, régimen, responsable de pago), antecedentes médicos del paciente (en cantidades) y datos de facturación del ítem (concepto, cantidad, valor, centro de costo).
- **Variable objetivo:** `CLAIM` (1 = con glosa, 0 = sin glosa).
- **Anonimización:** los datos se anonimizaron desde la extracción y se codificaron a valores numéricos. No contienen información identificable de pacientes ni de la clínica.
- **Dataset publicado:** [Claims of medical billing (Kaggle)](https://www.kaggle.com/datasets/jacquelineguzman/claims-of-medical-billing/)

## Metodología

Se siguió **CRISP-DM**: comprensión del negocio, comprensión de los datos, preparación, modelado, evaluación e implantación.

1. **Transformación:** conversión de las variables a formato numérico y optimización de tipos de datos para reducir el uso de memoria RAM.
2. **Exploración:** valores nulos, distribución de la variable objetivo y matriz de correlación.
3. **Preparación:** normalización y división 85 % entrenamiento / 15 % validación.
4. **Desbalance de clases:** solo 120 registros con glosa (0,002 %). Se aplicó **SMOTE** únicamente sobre el conjunto de entrenamiento.
5. **Modelado:** tres clasificadores.
   - Random Forest: 100 estimadores, modo balanceado.
   - Red neuronal: 4 capas ocultas, con pesos por clase según su participación.
   - Gradient Boosting (`HistGradientBoostingClassifier`): tasa de aprendizaje 0,05, profundidad 3, 300 árboles.
6. **Evaluación:** sensibilidad (recall) por clase y área bajo la curva ROC, priorizando el recall de la clase con glosa.

## Estructura del repositorio

| Notebook | Contenido |
|---|---|
| `1_Transform_Data_Claims.ipynb` | Transformación de los datos a valores numéricos y anonimización |
| `2_EDA_Data_Claims.ipynb` | Análisis exploratorio sobre `claims.csv` |
| `3_Model_RFC_Claims.ipynb` | Modelo Random Forest y su evaluación |
| `4_Model_NN_Claims.ipynb` | Modelo de red neuronal y su evaluación |
| `5_Model_HGBC_Claims.ipynb` | Modelo Gradient Boosting y su evaluación |

## Cómo ejecutarlo

Requisitos: Python 3.11 y JupyterLab 4.

```bash
pip install numpy pandas scikit-learn imbalanced-learn tensorflow matplotlib seaborn jupyterlab
```

1. Descarga el dataset desde Kaggle y ubícalo en la carpeta del proyecto.
2. Ejecuta los notebooks en orden, empezando por `2_EDA_Data_Claims.ipynb` si usas el dataset ya transformado.

## Limitaciones

- **Pocos casos positivos para validar:** el conjunto de validación tiene 16 glosas, así que el 93,75 % de recall corresponde a 15 de 16 casos. El resultado es prometedor, pero necesita validarse con más datos (por ejemplo, con validación cruzada estratificada).
- **Subregistro de glosas:** parte de las glosas se registraba en hojas de cálculo paralelas y no en el sistema de información, lo que explica en parte el desbalance extremo. Integrar esas fuentes es el siguiente paso para mejorar el modelo.
- **Una sola clínica:** el modelo está ajustado a los datos de una institución y puede no generalizar a otras sin reentrenamiento.

## Trabajo futuro

- Integrar todas las fuentes de glosas en un único origen de datos.
- Construir un modelo estándar que se pueda adaptar a varias clínicas.
- Automatizar otros procesos administrativos y financieros del sector salud con técnicas de IA.

## Tecnologías

Python 3.11 · JupyterLab 4 · Pandas · NumPy · Scikit-Learn · imbalanced-learn · TensorFlow · Matplotlib · Seaborn · SQL (Oracle)

## Autora

**Jacqueline Guzmán Rodríguez** – DBA e Ingeniera de Datos
[LinkedIn](https://www.linkedin.com/in/jacqueline-guzman-rodriguez)
