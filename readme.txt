mkdir WorkspacePigAnalisisOpinions
cd WorkspacePigAnalisisOpinions
hdfs dfs -mkdir pig_analisis_opinions

wget https://gitlab.com/jmmadronal/bigdata_aplicat/-/raw/main/pig/critiquescinematografiques.csv
wget https://gitlab.com/jmmadronal/bigdata_aplicat/-/raw/main/pig/AFINN.txt
wget https://raw.githubusercontent.com/Asierxo/bigdata/main/pig_script.pig
wget https://raw.githubusercontent.com/Asierxo/bigdata/main/pelis.csv
wget https://raw.githubusercontent.com/Asierxo/bigdata/main/pig_script1.pig

hdfs dfs -put critiquescinematografiques.csv /user/cloudera/pig_analisis_opinions
hdfs dfs -put AFINN.txt /user/cloudera/pig_analisis_opinions
hdfs dfs -put pelis.csv /user/cloudera/pig_analisis_opinions/

hdfs dfs -ls pig_analisis_opinions

cat pig_script.pig
pig pig_script.pig

cat pig_script1.pig
pig pig_script1.pig
