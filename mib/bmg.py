import pandas as pd

def clean(path):
    df = pd.read_csv(path).iloc[6:,:]
    df = df.drop(6)

    return df

def test():
    df = clean('../data/20200903-LB-Ecoli-growth.csv')
    print(df)

if __name__ == '__main__':
    test()
