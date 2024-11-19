import os
import pandas as pd

# Define folder
FOLDER_DATA = os.path.join(os.getcwd(), 'data')

def read_data(n: int) -> pd.DataFrame:
    # Read in csv data
    df = pd.read_csv(os.path.join(FOLDER_DATA, 'data_products.csv'), encoding='utf-8')
    # Select a random sample of 300 data points
    df_sample = df.sample(n=n, random_state=42)
    # Reset the index of the sampled dataframe
    df_sample.reset_index(drop=True, inplace=True)
    return df_sample

def main():
    df_sample = read_data(n=300)
    return df_sample

if __name__ == '__main__':
    main()




