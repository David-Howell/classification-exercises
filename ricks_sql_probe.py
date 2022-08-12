def sql_database_info_probe(schema_input):
    '''
    No return
    '''
    schema=schema_input
    query_1=f'''
    SELECT table_schema "Database Name",
    ROUND(SUM(data_length + index_length) / 1024 / 1024, 4) "DB Size in (MB)"
    FROM information_schema.tables
    WHERE table_schema= "{schema}"
    GROUP BY table_schema
    ;
    '''
    query_2=f'''
    SELECT table_name AS "Tables",
    ROUND(((data_length + index_length) / 1024 / 1024), 4) AS "Size (MB)"
    FROM information_schema.TABLES
    WHERE table_schema = "{schema}"
    ORDER BY (data_length + index_length) DESC;
    '''
    info1=pd.read_sql(query_1, get_db_url(schema))
    info2=pd.read_sql(query_2, get_db_url(schema))
    display(f'In {schema} your overlall size(MB) is:',info1)
    tablenames=[x[0] for x in [list(i) for i in info2.values] ]
    display(f'In {schema} you have the following table names and their sizes:',info2)
    x=[(pd.read_sql(f'describe {x}', get_db_url(schema)))for x in tablenames]
    [display(f'{(tablenames[i]).capitalize()}',k) for i,k in enumerate(x)]
    y=[(i.Field).str.split() for i in x]