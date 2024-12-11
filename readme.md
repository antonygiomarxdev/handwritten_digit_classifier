# Handwritten Digit Classifier

## Descripción

Handwritten Digit Classifier es un proyecto de aprendizaje profundo que utiliza una Red Neuronal Convolucional (CNN) para reconocer y clasificar dígitos escritos a mano. El modelo está entrenado con el conjunto de datos MNIST, el cual contiene miles de imágenes de dígitos manuscritos, divididas en conjuntos de entrenamiento y prueba.

Este proyecto está pensado para principiantes en ciencia de datos y aprendizaje automático. Proporciona un ejemplo práctico de cómo:
- Cargar y preprocesar datos de imágenes.
- Construir y entrenar una CNN con TensorFlow y Keras.
- Evaluar el rendimiento del modelo.
- Realizar predicciones con el modelo entrenado.

## Estructura del Proyecto

El proyecto contiene diferentes directorios y archivos para mantener el código y los datos organizados:

- `data/`: Contiene los datos (crudos y preprocesados).
- `notebooks/`: Almacena el notebook con el análisis exploratorio de datos (EDA).
- `src/`: Incluye el código fuente del proyecto (preprocesamiento, definición del modelo, scripts de entrenamiento, evaluación y predicción).
- `outputs/`: Guarda los modelos entrenados y las gráficas generadas durante el entrenamiento y la evaluación.
- `requirements.txt`: Lista de dependencias necesarias para el proyecto.
- `setup.py`: Opcional, para empaquetar el proyecto si así se desea.

## Requisitos

- Python 3.x
- TensorFlow
- NumPy
- Matplotlib
- scikit-learn
- seaborn

Instala las dependencias con:
```
pip install -r requirements.txt
```

## Uso

1. Clona o descarga el repositorio.
2. Crea y activa un entorno virtual (opcional pero recomendado).
3. Instala las dependencias.
4. Ejecuta el notebook en `notebooks/` para el análisis exploratorio.
5. Ejecuta `train.py` desde `src/` para entrenar el modelo.
6. Ejecuta `evaluate.py` para evaluar el modelo.
7. Ejecuta `predict.py` para hacer predicciones sobre nuevas imágenes.

## Recursos Adicionales

- Documentación de TensorFlow: https://www.tensorflow.org/
- Ejemplos de Keras: https://keras.io/examples/
- Tutoriales de aprendizaje profundo: https://www.coursera.org/specializations/deep-learning

Este proyecto es un punto de partida. Siéntete libre de modificar el código, la arquitectura del modelo o el proceso de entrenamiento para adaptarlo a tus necesidades.