import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"Dataset\battles.csv")
#cleaning dataset
df.dropna(subset=["attacker_king","attacker_outcome"],inplace=True)
#create new dataset with required columns
df2 = df.filter(["battle_type","attacker_size","defender_size","location","region"],axis=1)
#print(df2.to_string())
#create data frame with king names and number of wins for each
df_count = df.groupby("attacker_king")["attacker_outcome"].apply(lambda x:(x=="win").sum()).reset_index(name='wins')
print(df_count.sort_values("wins",ascending=False))
df_count.plot(kind="bar", x= "attacker_king",y="wins")
plt.show()
#find the king with most wins
print(df_count[df_count.wins == df_count.wins.max()])