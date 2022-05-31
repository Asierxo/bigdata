## Selección de imagen base
# Especificamos como imagen base una imagen Debian ligera con Java 8 JRE
FROM openjdk:8-jre-slim


## Descarga e instalación de dependencias
# Definimos las variables del Dockerfile
ARG hdfs_simulado=/opt/workspace
ARG spark_version=3.2.1
ARG hadoop_version=3.2
ARG spark_worker_web=8081 # Puerto para interfaz web del nodo worker

# Definimos la variable de entorno conteniendo el directorio de HDFS
ENV HDFS_SIMULADO=${hdfs_simulado}

# Realizamos la instalación de la última versión estable de Python3
RUN mkdir -p ${hdfs_simulado} && \
    apt-get update -y && \
    apt-get install -y python3 && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    rm -rf /var/lib/apt/lists/*
RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    pip3 install gdown numpy matplotlib scipy scikit-learn py4j pandas pyarrow

# Realizamos la instalación de Apache Spark
RUN apt-get update -y && \
    apt-get install -y curl && \
    curl https://archive.apache.org/dist/spark/spark-${spark_version}/spark-${spark_version}-bin-hadoop${hadoop_version}.tgz -o spark.tgz && \
    tar -xf spark.tgz && \
    mv spark-${spark_version}-bin-hadoop${hadoop_version} /usr/bin/ && \
    mkdir /usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}/logs && \
    rm spark.tgz

# Definimos las variables de entorno de Spark
ENV SPARK_HOME /usr/bin/spark-${spark_version}-bin-hadoop${hadoop_version}
ENV SPARK_MASTER_HOST spark-master
ENV SPARK_MASTER_PORT 7077
ENV PYSPARK_PYTHON python3

# Exponemos el puerto utilizado para acceder a la interfaz web del worker
EXPOSE ${spark_worker_web}


## Ejecución de comandos al arrancar el contenedor
# Montamos el HDFS simulado en una carpeta con datos persistentes
VOLUME ${hdfs_simulado}
CMD ["bash"]

# Especificamos la ruta de trabajo dentro del contenedor
WORKDIR ${SPARK_HOME}

# Ejecutamos Apache Spark como nodo worker
CMD bin/spark-class org.apache.spark.deploy.worker.Worker spark://${SPARK_MASTER_HOST}:${SPARK_MASTER_PORT} >> logs/spark-worker.out
