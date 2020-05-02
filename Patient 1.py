import pandas as pd
url = 'https://raw.githubusercontent.com/hxchua/datadoubleconfirm/master/datasets/arrivals2018.csv'
df = pd.read_csv(url, error_bad_lines=False)

