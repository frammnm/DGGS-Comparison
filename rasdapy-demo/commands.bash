
#Check types
rasql -q "select r from RAS_SET_TYPES as r" \
      --out string


#Working insert commands


#Basic insert 
rasql -q 'insert into test_basic values decode($1, "csv", "{ \"formatParameters\": {\"domain\": \"[0:1,0:2]\",\"basetype\": \"long\" } }")' --out string --file "/home/rasdaman/Documents/TFM/include/DGGS-Comparison/rasdapy-demo/dggs_sample_6.csv" --user rasadmin --passwd rasadmin


#Slightly more complex insert
rasql -q 'insert into test_json_dict values decode($1, "csv", "{ \"formatParameters\": {\"domain\": \"[0:0,1:254]\",\"basetype\": \"struct{char key, long value}\" } }")' --out string --file "/home/rasdaman/Documents/TFM/include/DGGS-Comparison/rasdapy-demo/dggs_sample_4.csv" --user rasadmin --passwd rasadmin

#Expected output:

# rasdaman@rasdaman:~/Documents/TFM/include/DGGS-Comparison/rasdapy-demo$ rasql -q 'insert into test_json_dict values decode($1, "csv", "{ \"formatParameters\": {\"domain\": \"[0:0,1:254]\",\"basetype\": \"struct{char key, long value}\" } }")' --out string --file "/home/rasdaman/Documents/TFM/include/DGGS-Comparison/rasdapy-demo/dggs_sample_4.csv" --user rasadmin --passwd rasadmin
# rasql: rasdaman query tool v1.0, rasdaman 9.8.0.
# Opening database RASBASE at localhost:7001... ok.
# fetching type information for GreyString from database... ok.
# reading file /home/rasdaman/Documents/TFM/include/DGGS-Comparison/rasdapy-demo/dggs_sample_4.csv... ok.
# constants are:
#   constant 1: GMarray
#   Oid...................: 
#   Type Structure........: <nn>
#   Type Schema...........: marray< char >
#   Domain................: [0:1902]
#   Base Type Schema......: char
#   Base Type Length......: 1
#   Data format.......... : Array
#   Data size (bytes).... : 1903
# Executing insert query... ok.
# Query result collection has 1 element(s):
#   Result element 1: 6657
# rasql done.
