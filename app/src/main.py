import pandas as pd
from proccesing.data_cleaning import cleaning_2025, save_epi_year


def main():
    df = cleaning_2025()
    print(df.head())
    save_epi_year(df)


if __name__ == "__main__":
    main()
