from pydruid.client import *
import pandas as pd
from pydruid.db import connect


def exec_to_df(druid_query):
    conn = connect(host='localhost', port=8082, path='/druid/v2/sql/', scheme='http')
    curs = conn.cursor()

    # druid_query = """SELECT * FROM datastock LIMIT 100"""

    df = pd.DataFrame(curs.execute(druid_query))

    return df