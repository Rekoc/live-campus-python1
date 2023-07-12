import os, pandas, pathlib
from pandas.core.frame import DataFrame


def read_data_file(path: str) -> DataFrame:
    if not os.path.exists(path):
        return None
    data_file = open(path, 'rb')
    if ".csv" in path:
        df = pandas.read_csv(data_file)
    elif ".xlsx" in path:
        df = pandas.read_excel(data_file, sheet_name='excel_file')
    elif ".json" in path:
        df = pandas.read_json(data_file)
    elif ".html" in path:
        df = pandas.read_html(data_file)
    else:
        return None
    return df

def my_method(x: int) -> int:
   return x ** 2

def main():
    root_file = pathlib.Path(__file__).parent.resolve()
    data = read_data_file(
        os.path.join(root_file, "csv_files", "big.csv")
    )
    # print("--- Your data file ---")
    # print(f"Data types:\n{data.dtypes}\n")
    # print(f"File's info:\n{data.info()}\n")
    # print(f"{data.count()}\n")
    # print(f"Columns:\n{data.columns}\n")
    # print(f"{data.to_json()}\n")
    # print(f"{data.to_html()}\n")
    # print(f"{data.to_dict()}\n")

    # Copy one column
    temp_df = data.get("clientid").copy()
    # Equivalent
    # temp_df = data["clientid"].copy()
    print(temp_df)
    # Apply one method to each row of this column
    temp_df = temp_df.apply(my_method)
    print(temp_df)
    # Erase the old column with the updated ones
    data["clientid"] = temp_df

    # Write an Excel file with the updated values
    data.to_excel(
        os.path.join(root_file, "demo_excel.xlsx")
    )

if __name__ == "__main__":
    main()