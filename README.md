# Sistema inteligente para ayudar a detectar posibles reclamos (glosas) en las cuentas médicas previo al cobro, de una clínica en Colombia - Audimed.
***
El desarrollo del proyecto se siguió usando la metodología de proyectos de minería de datos Cross-Industry Standard Process (CRISP-DM) (Corona Organiche & Jiménez Alfaro, 2020). En el proceso de exploración del conjunto de datos, se identificó una variable objetivo con dos clases registros con reclamaciones marcados como uno (1) y sin reclamaciones marcados como cero (0), también se identificó un desbalanceo en las clases (Bagnato, 2019), por lo cual fue necesario usar la técnica de sobre muestreo (over-sampling) SMOTE (Chaudhary, 2023), para facilitar la aplicación de los modelos de predicción. Posteriormente se experimentó con tres algoritmos de clasificación basados en las técnicas: Ramdon Forest (Erb, 2020), redes neuronales (Tensorflow, 2022) y Grandient Boosting (Amat Rodrigo, 2023). En el proceso de evaluación de los modelos se usaron las métricas de sensibilidad (recall) y el área bajo la curva ROC (Rutecki, 2022). Al finalizar la evaluación se escogió el modelo de clasificación basado en Grandient Boosting, porque fue el de mejor resultado obteniendo un valor de 0.97 en el área bajo la curva (ROC), una sensibilidad (recall) de la clase 0 con reclamación del 99.99% y una sensibilidad (recall) de la clase 1 sin reclamación del 93,75%.
## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)

### General Info
***
Write down the general informations of your project. It is worth to always put a project status in the Readme file. This is where you can add it. 
### Screenshot
![Image text](https://www.united-internet.de/fileadmin/user_upload/Brands/Downloads/Logo_IONOS_by.jpg)
## Technologies
***
A list of technologies used within the project:
* [Technologie name](https://example.com): Version 12.3 
* [Technologie name](https://example.com): Version 2.34
* [Library name](https://example.com): Version 1234
