import os
import pandas as pd

# pred_file_paths = ["gbcmen_lrwomen.csv", "Gradien boosting.csv"]
pred_file_paths = ["Gradient boosting.csv"]
base_path = "c:/nextcloud/Studia - PW/semestr 6/projekt interdyscyplinarny/march-ml-madness-2025/src/mikematuszy/submitted_pred/"
m_teams = pd.read_csv(os.path.join(base_path, "MTeams.csv"))
w_teams = pd.read_csv(os.path.join(base_path, "WTeams.csv"))

print(m_teams.columns)

for pred_file_path in pred_file_paths:
    # print(pred_file_path)
    predictions = pd.read_csv(os.path.join(base_path, pred_file_path))
    predictions["TEAM1"] = predictions["ID"].str.split("_").str[1]
    predictions["TEAM2"] = predictions["ID"].str.split("_").str[2]
    print(predictions.columns)
    pd.merge(predictions, m_teams, left_on="TEAM1", right_on="TeamID")
    print(predictions.head)
    # print(file.columns)
