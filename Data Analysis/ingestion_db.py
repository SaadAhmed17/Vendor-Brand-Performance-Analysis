import os
import pandas as pd
from sqlalchemy import create_engine
import time
import logging
logging.basicConfig(
    filename = "logs/ingestion.db.log",
    level=logging.DEBUG,
    formate="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

engine = create_engine("mysql+pymysql://root:X%40%40d@localhost/Vender_Performance")

def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists='replace', index=False, method='multi', chunksize=10000)

def load_raw_data():
    start = time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df = pd.read_csv('data/'+file)
            logging.info(f'ingesting {file} in db')
            ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end - start)/60
    logging.info('------------Ingestion Complete------------')
    logging.info(f'\nTotal Time Taken: {total_time} minutes')

if __name__ == '__main__':
    load_raw_data()