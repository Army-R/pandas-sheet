import pandas as pd

# Loading the data from a csv file
airlines_data = pd.read_csv("Airlines.csv")

# Getting the count of rows and columns in the dataframe
# Shape of a dataframe
ad_shape = airlines_data.shape 

# Head and Tail of the data frame
ad_head = airlines_data.head(n=10) # first 10
ad_tail = airlines_data.tail(n=10) # last 10

# Getting data types of the columns to understand if the columns are loaded properly with correct types
# Data types of the colums 
ad_types = airlines_data.dtypes

# Getting column names
ad_columnNames = airlines_data.columns.tolist()

# Getting the summary stats for numeric columns
# Summary states
ad_summary = airlines_data.describe()

# Getting the count of NA values in the columns 
ad_na = airlines_data.isna().sum()

# Selecting columns with data type as objects
ad_object = airlines_data.select_dtypes(include = "object").columns

# Selecting columns with data type as int64
ad_int64 = airlines_data.select_dtypes(include = "int64").columns

# Getting value counts from the columns
ad_valcol = airlines_data["Airline"].value_counts(ascending=True)

# Getting unique names of values in a column
ad_unqcol = airlines_data["Airline"].unique()

# Selecting a few columns
ad_fewcol = airlines_data[["id", "Airline", "Flight"]]

# Selecting a few rows using .iloc
ad_fewrow = airlines_data.iloc[:10,]

# Selecting a few rows and columns together using .loc
ad_fewrowcol = airlines_data.loc[:5, ["id", "Airline", "Flight"]] 

# Filtering the data using a column
ad_filtcol = airlines_data[airlines_data["Airline"] == "US"]

# Filtering the data using multiple columns
ad_filtmulcol = airlines_data[(airlines_data["Airline"] == "US") & (airlines_data["AirportFrom"] == "PHX") & (airlines_data["DayOfWeek"] == 1)]

# Filtering the data using OR conditions
ad_or = airlines_data[(airlines_data["Airline"] == "US") | (airlines_data["AirportFrom"] == "PHX")]

airliens_list = ["DL", "US"]

# Filtering the data using a list
ad_filtlist = airlines_data[airlines_data["Airline"].isin(airliens_list)]

# Filtering for the data not in the list
ad_filtnolist = airlines_data[~airlines_data["Airline"].isin(airliens_list)]

# Sorting the data using a column
ad_sortcol = airlines_data.sort_values(by="Airline", ascending=False)

# Rename a column
ad_renamecol = airlines_data.rename(columns={"Airline": "Aereolinea", "AirportFrom": "Salida"})

# Summarise data using groupby
ad_groupby = airlines_data.groupby(["Airline", "AirportFrom", "AirportTo"], as_index=False) ["id"].agg("count")

# Summarise and sort
ad_summsort = ad_groupby.sort_values(by="id", ascending=False)

# Summarise for multiple values
ad_mulgroupby = airlines_data.groupby(["Airline", "AirportFrom", "AirportTo"]) ["Time"].agg(["sum", "count"]).reset_index()

# Summarise for multiple columns and values
ad_mulcolval = airlines_data.groupby(["Airline", "AirportFrom", "AirportTo"]).aggregate({"id": "count", "Time": "sum"}).reset_index()

# Adding a new column
airlines_data["Country"] = "MXN"

# Adding a column using existing columns
airlines_data["CO_SFO"] = (airlines_data["Airline"] =="CO") & (airlines_data["AirportFrom"] == "SFO")

# Dropping a column
airlines_data.drop(["CO_SFO"], axis=1)

# Summarise using pivot_table with aggregation
ad_pivottable = airlines_data.pivot_table(index = ["Airline", "AirportFrom", "AirportTo"], values = ["Time"], aggfunc=["sum", "count"]).reset_index(col_level=1) 

# Pivot data using pivot_table where unique rows are not available for index columns
ad_pivottable2 = airlines_data.pivot_table(index = "Airline", columns="DayOfWeek", values = "id", aggfunc="count", fill_value = 0).reset_index() 

# Summarise using groupby and pivot
ad_pivogroup = airlines_data.groupby(["Airline", "DayOfWeek"], as_index=False) ["id"].agg("count").reset_index()

ad_pivogroup2 = ad_pivogroup.pivot(index = ["Airline"], columns = "DayOfWeek", values = "id").reset_index()

print(ad_pivogroup2)