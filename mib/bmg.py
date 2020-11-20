import re
import pandas as pd

def clean(path):
    df_orig = pd.read_csv(path)
    df = df_orig
    nacounts = [sum(df.iloc[i,:].isna()) for i in df.index] # use to locate metadata
    print(nacounts)
    # retain metadata?
    # metadata rows have lots of NaN
    # use regex to find well IDs (A01, ..) & time points (0h15,..)
    # if timepoints & 1 wavelenth - idx = wells, headers = time
    # if end point, idx = wells, headers = wavelength
    return df

def test():
    df = clean('../data/20200903-LB-Ecoli-growth.csv')
    print(df)

if __name__ == '__main__':
    test()
