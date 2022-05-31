## Selección de imagen base
# Especificamos como imagen base una imagen Debian ligera con Java 8 JRE
FROM openjdk:8-jre-slim


## Descarga e instalación de dependencias
# Definimos las variables del Dockerfile
ARG hdfs_simulado=/opt/workspace
ARG spark_version=3.2.1
ARG jupyterlab_version=3.2.0
ARG jupyterlab_web=8888 # Puerto para interfaz web de JupyterLab

# Definimos la variable de entorno conteniendo el puerto de JupyterLab
ENV HDFS_SIMULADO=${hdfs_simulado}

# Definimos las variables de entorno conteniendo el directorio de HDFS
ENV JUPYTERLAB_PORT=${jupyterlab_web}

# Realizamos la instalación de la última versión estable de Python3
RUN mkdir -p ${hdfs_simulado} && \
    apt-get update -y && \
    apt-get install -y python3 && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/*
RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    pip3 install gdown matplotlib scipy scikit-learn 
# Dependències pyspark
RUN pip3 install pandas numpy pyarrow py4j pyarrow

# Realizamos la instalación de la versión especificada de Pyspark y JupyterLab
RUN pip3 install wget pyspark==${spark_version} jupyterlab==${jupyterlab_version}


## Ejecución de comandos al arrancar el contenedor
# Montamos el HDFS simulado en una carpeta con datos persistentes
VOLUME ${hdfs_simulado}
CMD ["bash"]

# Exponemos el puerto utilizado por JupyterLab
EXPOSE ${jupyterlab_web}

# Especificamos la ruta de trabajo dentro del contenedor
WORKDIR ${HDFS_SIMULADO}

# Ejecutamos JupyterLab utilizando el puerto especificado
CMD jupyter lab --ip=0.0.0.0 --port=${JUPYTERLAB_PORT} --no-browser --allow-root --NotebookApp.token=
