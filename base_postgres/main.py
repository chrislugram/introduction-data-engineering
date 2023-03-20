"""
This file contains the process for upload a dataframe
into a postgress database
"""

import psycopg2
import os
import pandas as pd


def read_postgres_params():
    return {
        "db": os.getenv("POSTGRES_DB"),
        "user": os.getenv("POSTGRES_USER"),
        "pw": os.getenv("POSTGRES_PASSWORD"),
        "host": os.getenv("POSTGRES_HOST"),
        "port": os.getenv("POSTGRES_PORT"),
    }


def save_df_in_db(db_conn, df: pd.DataFrame):
    """
    This function insert in db a dataframe.
    - The table must exist

    Args:
        db_conn (psycopg2.connection): DB connection
        df (pd.DataFrame): Dataframe with data
    """
    cursor = db_conn.cursor()

    dict_data = df.to_dict()
    columns_name = list(dict_data.keys())
    len_dataframe = len(df)

    for i in range(0, len_dataframe):
        values = (
            dict_data[columns_name[0]][i],
            dict_data[columns_name[1]][i],
            dict_data[columns_name[2]][i],
            dict_data[columns_name[3]][i],
            dict_data[columns_name[4]][i],
        )
        cursor.execute(
            "INSERT INTO CARSALESTABLE (price, mileage, engType, year, model) VALUES (%s, %s, %s, %s, %s)",
            values,
        )

    db_conn.commit()


def flow():
    # Create conection
    con_params = read_postgres_params()
    db_conn = psycopg2.connect(
        database=con_params["db"],
        user=con_params["user"],
        password=con_params["pw"],
        host=con_params["host"],
        port=con_params["port"],
    )

    # # Read dataframe
    df = pd.read_csv("data/exercise03_car_sales_data.csv")

    # # Write dataframe in postgress
    save_df_in_db(db_conn=db_conn, df=df)

    # Close connection
    db_conn.close()


if __name__ == "__main__":
    flow()
