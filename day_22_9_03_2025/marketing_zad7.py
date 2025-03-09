import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("marketing_r_bool.csv", sep=",")


def conversion_rate(dataframe, column_names):
    column_conv = dataframe[dataframe["converted"] == True].groupby(column_names)["user_id"].nunique()

    column_total = dataframe.groupby(column_names)["user_id"].nunique()

    conversion_rate = column_conv / column_total

    conversion_rate = conversion_rate.fillna(0)
    return conversion_rate


def plotting_conv(dataframe):
    for column in dataframe:
        plt.plot(dataframe.index, dataframe[column])
        plt.title("Daily " + str(column) + " converion rate\n", size=16)
        plt.ylabel("Conversation rate", size=14)
        plt.xlabel("Date", size=14)
        plt.xticks(rotation=45)
        plt.show()
        plt.clf()


if __name__ == '__main__':
    age_group_conv = conversion_rate(df, ['date_served', 'age_group'])
    print(age_group_conv)

    age_group_conv_df = pd.DataFrame(age_group_conv.unstack(level=1))
    plotting_conv(age_group_conv_df)
