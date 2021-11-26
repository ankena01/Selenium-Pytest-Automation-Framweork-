# Common utilities
import logging
from ddt import data
import pandas as pd


class Utils:

    def custom_logger(loglevel = logging.DEBUG):


        # Create logger - set logging level
        logger = logging.getLogger(__name__)
        logger.setLevel(loglevel)


        # Create handler - console handler / file handler
        
        fh = logging.FileHandler('.\Logs\demo_file.log', mode='a')

        # Create formatter (how you want logs to be formatted)
        
        formatter_fh = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s :%(filename)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p' )


        # Adding the formatter to console handler / file handler
        
        fh.setFormatter(formatter_fh)

        # adding console handler / file handler to logger
        
        logger.addHandler(fh)

        return logger

    def read_data_from_excel(file_path):

        df = pd.read_excel(file_path, sheet_name="Sheet1")

        row_count = len(df)

        data_list = []

        for i in range(0,row_count):
            row = []
            for x in df.iloc[i]:
                row.append(x)
            data_list.append(row)

        return data_list

    def read_data_from_csv(file_path):

        df = pd.read_csv(file_path)

        row_count = len(df)

        data_list = []

        for i in range(0,row_count):
            row = []
            for x in df.iloc[i]:
                row.append(x)
            data_list.append(row)

        return data_list

    def read_data_from_json(file_path):

        df = pd.read_json(file_path)
        print(df)
        #print("The colun name are : ", df.columns)
        data_list = []
        list_1 = [eachitem for eachitem in df['test1']]
        list_2 = [eachitem for eachitem in df['test2']]
        data_list.append(list_1)
        data_list.append(list_2)
        #print(data_list)
        return data_list

        # row_count = len(df)

        # data_list = []

        # for i in range(0,row_count):
        #     row = []
        #     for x in df.iloc[i]:
        #         row.append(x)
        #     data_list.append(row)
        # print(data_list)
        # return data_list

    
