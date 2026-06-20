import duckdb
import pandas as pd

conn=duckdb.connect("data.db")

class StockRepository:

    def find_by_theme(self,theme):

        sql="""

        SELECT *
        FROM Stock
        WHERE theme_id=?

        """

        return conn.execute(
            sql,
            [theme]
        ).df()

class JoinRepository:

    def theme_report(self,theme):

        sql="""

        SELECT
        T.theme_name,
        S.stock_name,
        F.revenue,
        F.operating_profit

        FROM Theme T

        JOIN Stock S
        ON T.theme_id=S.theme_id

        JOIN Financials F
        ON S.stock_code=F.stock_code

        WHERE T.theme_id=?

        """

        return conn.execute(
            sql,
            [theme]
        ).df()