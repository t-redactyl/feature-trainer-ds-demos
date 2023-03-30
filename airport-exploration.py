#%%
import pandas as pd

airlines = pd.read_csv("airlines.csv")
#%%
airport_codes = airlines["AirportCode"].unique().tolist()
#%%

if __name__ == "__main__":
    print(airlines)
