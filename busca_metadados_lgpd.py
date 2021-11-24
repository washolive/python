# Busca metadados das tabelas em busca de colunas que armazenem dados pessoais segundo a LGPD
# usando o inspector do SqlAlchemy

import sqlalchemy as sa
import pandas as pd
import pyodbc
import re

databases = [
    (r"mssql+pyodbc://user:password@host_ip:port/dbname1?driver=SQL+Server+Native+Client+11.0", 'dbo'),
    (r"mssql+pyodbc://user:password@host_ip:port/dbname2?driver=SQL+Server+Native+Client+11.0", 'dbo'),
]

pattern = r"""(.*cpf.*)|(.*nome.*)|(.*e_*mail.*)|(.*passaporte.*)|(.*sexo.*)|(.*cargo.*)|(.*funcao.*)|
              (.*lotacao.*)|(.*ident.*)|(.*siape.*)|(.*patente.*)|(.*conta.*)|(.*agencia.*)|(.*banco.*)|
              (.*tel.*)|(.*aux.*)|(.*nasc.*)|(.*mae.*)|(.*login.*)|(.*doenca.*)|(.*cnh.*)|(.*nis.*)|
              (.*nit.*)|(.*social.*)|(.*civil.*)|(rg)|(.*_rg)|(rg_.*)|(.*city.*)
            """

achados = pd.DataFrame({}, columns=['database', 'schema', 'tabela', 'coluna'])

for urldb, schema in databases:

    engine = sa.create_engine(urldb)
    inspector = sa.inspect(engine)

    dbname = urldb.split('?')[0].split('/')[-1]
    tabs = inspector.get_table_names(schema=schema)

    for tab in tabs:
        cols = inspector.get_columns(tab, schema=schema)

        for col in cols:
            # print(dbname, schema, tab, col['name'])
            if re.match(pattern, col['name'], re.IGNORECASE):
                item = {'database': dbname, 'schema': schema, 'tabela': tab, 'coluna': col['name']}
                achados = achados.append(item, ignore_index=True)

# print(achados)
achados.to_csv(r"metadados_lgpd.csv")

