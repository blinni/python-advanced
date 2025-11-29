import pandas as pd

data = {"Name": ['alice', 'Bob', 'Charlie'],
        "Age": [25,30,22],
        "City": ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)
print(df)

