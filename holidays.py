import pandas as pd
from workalendar.america.mexico import Mexico

calendar = Mexico()
holidays = calendar.holidays(2022)

df = pd.DataFrame(holidays, columns=['date', 'name'])
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].dt.day_name()
df = df.groupby('date').count().sort_values('name', ascending=False)

print(df)
