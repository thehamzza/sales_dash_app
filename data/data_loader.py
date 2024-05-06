import pandas as pd
import os

print(os.getcwd())

def load_data():
    dataset_path = "/data/dataset.xls"
    dataset_path = (os.getcwd()+ dataset_path)
    print("dataset_path: ", dataset_path)
    return pd.read_excel(dataset_path)


# df = pd.read_excel(r"/Users/hamza/Developer/python_projects/dash_aldi/dataset.xls")
# #print(df)
