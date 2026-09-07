import duckdb

con = duckdb.connect(config = {'storage_compatibility_version': 'latest'})

print(con)