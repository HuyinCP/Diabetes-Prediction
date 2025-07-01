import pandas as pd
from matplotlib.pyplot import title
from ydata_profiling import ProfileReport
# Read data
df = pd.read_csv("Datasets/csgo.csv")

profile = ProfileReport(df, title="CSGO report", explorative=True)
profile.to_file("CSGO_report.html")


