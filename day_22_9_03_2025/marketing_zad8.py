import marketing_zad7 as fun
import pandas as pd

df = pd.read_csv("marketing_r_bool.csv", sep=",")
df['date_served'] = pd.to_datetime(df['date_served'], format='%m/%d/%y')
house_ads = df[df["subscribing_channel"] == "House Ads"]

house_ads_bug = house_ads[house_ads['date_served'] < '2018-01-11']
lang_conv = fun.conversion_rate(house_ads_bug, ['language_displayed'])
print("lang_conv:\n", lang_conv)

spanish_index = lang_conv['Spanish'] / lang_conv['English']
arabic_index = lang_conv['Arabic'] / lang_conv['English']
german_index = lang_conv['German'] / lang_conv['English']
print("Spanish index:", spanish_index)
print("Arabic index:", arabic_index)
print("German index:", german_index)

converted = (house_ads.groupby(['date_served', 'language_preferred'])
             .agg({"user_id": "nunique", "converted": "sum"}))
converted = pd.DataFrame(converted.unstack(level=1))
print("Pełne dane w converted:\n", converted.to_string())

converted['english_conv_rate'] = (converted.loc['2018-01-11':'2018-01-31'][('converted', 'English')] /
                                  converted.loc['2018-01-11':'2018-01-31'][('user_id', 'English')])

converted['expected_spanish_rate'] = converted['english_conv_rate'] * spanish_index
converted['expected_arabic_rate'] = converted['english_conv_rate'] * arabic_index
converted['expected_german_rate'] = converted['english_conv_rate'] * german_index

print(converted['expected_spanish_rate'])
converted['expected_spanish_conv'] = converted['expected_spanish_rate'] * converted[('user_id', 'Spanish')]
converted['expected_arabic_conv'] = converted['expected_arabic_rate'] * converted[('user_id', 'Arabic')]
converted['expected_german_conv'] = converted['expected_german_rate'] * converted[('user_id', 'German')]

converted = converted.loc['2018-01-11':'2018-01-31']
expected_subs = (converted['expected_spanish_conv'].sum() +
                 converted['expected_arabic_conv'].sum() +
                 converted['expected_german_conv'].sum())
print("Expected sum:", expected_subs)

actual_subs = (converted[('converted', 'Spanish')].sum() +
               converted[('converted', 'Arabic')].sum() +
               converted[('converted', 'German')].sum())
print("Actual sum:", actual_subs)

lost = expected_subs - actual_subs
print("Lost sum:", lost)
