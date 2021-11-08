from rasdapy.db_connector import DBConnector
from rasdapy.query_executor import QueryExecutor

db_connector = DBConnector("localhost", 7001, "rasadmin", "rasadmin")
db_connector.open()



query_executor = QueryExecutor(db_connector)


collection_list = query_executor.execute_read("select c from RAS_COLLECTIONNAMES as c")
print(collection_list)


# Example
# query_executor.execute_write("create collection test_mr GreySet")
# query_executor.execute_update_from_file("insert into test_mr values decode($1)", "/home/rasdaman/Documents/TFM/include/rasdapy-demo/mr_1.png")

# sdom = query_executor.execute_read("select sdom(c) from test_mr as c")
# print(sdom)


# Create my own cell type
# create type typeName
# as (
#   attrName_1 atomicType_1,
#   ...
#   attrName_n atomicType_n
# )

query_executor.execute_write("create type jsonDict as ( key char, value long)")


# Create my own MD Array type based on my cell type
# create type typeName
# as baseTypeName mdarray domainSpec
# Alternate declaration: 
# create type typeName
# as (
#   attrName_1 atomicType_1,
#   ...
#   attrName_n atomicType_n
# ) mdarray domainSpec

query_executor.execute_write("create type jsonDictArray as jsonDict mdarray [x, y]")



# Create my own set based on my MDArray type
# create type typeName
# as set ( marrayTypeName [ nullValues ] )

query_executor.execute_write("create type jsonDictSet as set (jsonDictArray)")


# Create test collection
query_executor.execute_write("create collection test_json_dict jsonDictSet") 

# Inser data into collection

# query_executor.execute_update_from_file("insert into test_json_dict values decode($1, 'json', '{\"formatParameters\": {\"domain\": \"[0:1000]\",\"basetype\": struct { char k, long v } } })'", "/home/rasdaman/Documents/TFM/include/rasdapy-demo/dggs_sample.json")
query_executor.execute_update_from_file("insert into test_json_dict values decode($1, 'csv', '{\"formatParameters\": {\"domain\": \"[0:0,1:254]\",\"basetype\": struct { char key, long value } } })'", "/home/rasdaman/Documents/TFM/include/rasdapy-demo/dggs_sample_4.csv")