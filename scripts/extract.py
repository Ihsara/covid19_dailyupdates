import pandas as pd
import os
from datetime import datetime as dt

from xlrd.biffh import XLRDError

PREFFIX_NAME = 'COVID-19-geographic-disbtribution-worldwide'
SUFFIX_NAME = '.xls'
DATAPATH = 'data'
DATA_SHEETNAME = 'COVID-19-geographic-disbtributi'


def __name_constructor(prefix=PREFFIX_NAME, suffix=SUFFIX_NAME, today=None):
    if not today:
        today = dt.now().strftime('%Y-%m-%d')

    return f'{prefix}-{today}{suffix}'


def extract_latest_df(datapath=None, sheetname=''):
    excelfile = pd.ExcelFile(datapath)
    try:
        df = pd.read_excel(excelfile, sheetname)
    except XLRDError:
        df = ''
        print('Error reading file')

    return df


def extract_df_per_contry(df=None, country_id=None):
    return df[df['GeoId'] == country_id]


def extract_df_per_date(date=None):
    return df[df.DateRep == date]


class DataContainer(object):
    def __init__(
        self,
        datapath=DATAPATH,
        prefix_data_filename=PREFFIX_NAME,
        suffix_data_filename=SUFFIX_NAME,
        data_sheetname=None,
        date_inquiry=None):

        self.name = self.__name_constructor(
            preffix=prefix_data_filename,
            suffix= suffix_data_filename,
            date=date_inquiry
        )
        self.df = self.extract_df(
            datapath=os.path.join(
                datapath,
                self.name
            ),
            sheetname=data_sheetname
        )

    def __repr__(self):
        return str(self.name)

    def __name_constructor(self, preffix=None, suffix=None, date=None):
        if not date:
            date = dt.now().strftime('%Y-%m-%d')

        return f'{preffix}-{date}{suffix}'

    def extract_df(self, datapath=None, sheetname=None): 
        excelfile = pd.ExcelFile(datapath)
        try:
            df = pd.read_excel(excelfile, sheetname)
        except XLRDError:
            df = ''
            print('Error reading file')

        return df

    def extract_by_country(self, country_geoid=None):
        if country_geoid:
            ans_df = self.df[self.df['GeoId']==country_geoid]

        return ans_df

    def extract_by_date(self, date=None):
        if date:
            ans_df = self.df[self.df['DateRep'] == date]
        return ans_df


if __name__ == "__main__":
    # https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide
 
    __datapath = os.path.join('.', 'data', __name_constructor())

    print(__datapath)

    tst1_df = extract_latest_df(
        datapath=__datapath,
        sheetname='COVID-19-geographic-disbtributi'
    )

    vn_df = extract_df_per_contry(country_id='VN', df=tst1_df)

    print(tst1_df)
    print(vn_df)

    test2 = DataContainer(
        datapath=DATAPATH,
        prefix_data_filename=PREFFIX_NAME,
        suffix_data_filename=SUFFIX_NAME, 
        data_sheetname=DATA_SHEETNAME,
        date_inquiry=None
    )

    print(test2)
    print(test2.extract_by_country('FI'))
    print(test2.extract_by_date('2020-03-18'))