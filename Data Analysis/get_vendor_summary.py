import mysql.connector
import pandas as pd
import numpy as np
import logging
from ingestion_db import ingest_db
from sqlalchemy import create_engine
import time

logging.basicConfig(
    filename = "logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filemode="a"
)
engine = create_engine("mysql+pymysql://root:X%40%40d@localhost/Vender_Performance")
    
def create_vendor_summary (engine):
    vendor_sales_summary = pd.read_sql_query("""WITH FreightSummary as(
        SELECT
            VendorNumber,
            SUM(Freight) as FreightCost
        FROM vendor_invoice
        GROUP BY VendorNumber
    ),
    PurchaseSummary AS(
        SELECT
            p.vendorNumber,
            p.VendorName,
            p.Brand,
            p.Description,
            p.PurchasePrice,
            pp.Price AS ActualPrice,
            pp.Volume,
            SUM(p.Dollars) AS TotalPurchaseDollars,
            SUM(p.Quantity) AS TotalPurchaseQuantity
        FROM purchases p
        JOIN purchase_prices pp
            ON p.Brand=pp.Brand
        WHERE p.PurchasePrice > 0
        GROUP BY p.VendorNumber, p.VendorName, p.Brand, p.Description, p.PurchasePrice, pp.Price, pp.Volume
    ),
    SalesSummary as(
        SELECT
            VendorNo,
            Brand,
            SUM(SalesDollars) as TotalSalesDollars,
            SUM(SalesPrice) as TotalSalesPrice,
            SUM(SalesQuantity) as TotalSalesQuantity,
            SUM(ExciseTax) as TotalExciseTax
        FROM sales
        GROUP BY VendorNo, Brand
    )

    SELECT
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.ActualPrice,
        ps.Volume,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalExciseTax,
        fs.FreightCost
    FROM PurchaseSummary ps
    LEFT JOIN SalesSummary ss
        ON ps.VendorNumber = ss.VendorNo
        AND ps.Brand = ss.Brand
    LEFT JOIN FreightSummary fs
        ON ps.VendorNumber = fs.VendorNumber
    ORDER BY TotalPurchaseDollars DESC""", engine)

    return vendor_sales_summary


def clean_data(df):
    '''this function will clean the data'''
    #changing datatpe to float
    df['Volume'] = df['Volume'].astype('float')

    #removing spaces from catagorical columns
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    #creating new columns for better analysis
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] = (df['GrossProfit'] / df['TotalSalesDollars'])*100
    df['StockTurnover'] = df['TotalSalesQuantity'] / df['TotalPurchaseQuantity']
    df['SalesToPurchaseRatio'] = df['TotalSalesDollars'] / df['TotalPurchaseDollars']

    #filling the missing values with zero(0)
    # handle inf/nan
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.fillna(0, inplace=True)

    return df

if __name__ == '__main__':
    # creating database connection
    conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "X@@d",
    database = "Vender_Performance"
    )
    logging.info('Creating Vendor Summary Table....')
    summary_df = create_vendor_summary(engine)
    logging.info(summary_df.head())
    
    logging.info('Cleaning Data....')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Ingesting Data....')
    ingest_db(clean_df, 'vendor_sales_summary', engine)
    logging.info('Completed')
    logging.shutdown()