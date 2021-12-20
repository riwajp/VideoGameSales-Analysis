import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("vgsales.csv")

dataframe = pd.DataFrame(data)


def sales_by_x(x):
    grp_by_x = dataframe.groupby(x)

    x_sales = {}
    x_arr = []
    sales_arr = []
    for key, item in grp_by_x:

        sales = item['Global_Sales'].sum()

        x_arr.append(key)
        sales_arr.append(sales)
    x_sales[x] = x_arr
    x_sales['sales'] = sales_arr
    x_sales_df = pd.DataFrame(x_sales)
    print(x_sales_df)
    sns.barplot(data=x_sales_df, x=x, y='sales')
    plt.xticks(rotation=70)

    plt.show()
# sales_by_x('Platform')


def most_sold_game_by_x(x, region):
    grp_by_x = dataframe.groupby(x)
    for key, item in grp_by_x:
        max_sales = item[region].max()
        index = item[region].tolist().index(max_sales)
        name = item['Name'].tolist()[index]
        print(str(key)+": "+name+" (" + str(max_sales)+")")


most_sold_game_by_x("Year", 'NA_Sales')


print(dataframe.columns)
