import pandas as pd
from proccesing.data_cleaning import cleaning_2025


def main():
    df = cleaning_2025()
    print(df.head())


if __name__ == "__main__":
    main()
