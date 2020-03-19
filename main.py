import bokeh

from scripts import extract
from scripts.extract import DataContainer as dc 

if __name__ == "__main__":
    test = dc(
        datapath=extract.DATAPATH,
        prefix_data_filename=extract.PREFFIX_NAME,
        suffix_data_filename=extract.SUFFIX_NAME,
        data_sheetname=extract.DATA_SHEETNAME,
        date_inquiry=None
    )

    print(test)
    print(test.extract_by_country('FI'))
    print(test.extract_by_date('2020-03-18'))