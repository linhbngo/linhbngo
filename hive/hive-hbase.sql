CREATE EXTERNAL TABLE testHBase(rowkey STRING, jsonColumn STRING)
STORED BY 'org.apache.hadoop.hive.hbase.HBaseStorageHandler'
WITH SERDEPROPERTIES('hbase.columns.mapping'=':key,Raw_Tweets:json')
TBLPROPERTIES('hbase.table.name'='test');
