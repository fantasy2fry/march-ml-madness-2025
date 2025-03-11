## Idea for dataframe used in project for training and testing
- We will create dataframes based on 2 (maybe more) seasons back in time and one tournament back in time.
- And Train set will have all stats based on 2022 season and 2021 season and 2021 tournament: we will think 
what stats we will use/create. And then we will look at matchups during 2022 tournament and
create two classes: 1 if team1 won and 0 if team2 won. BALANCED CLASSES!!!
- Test set will have all stats based on 2024 season and 2023 season and 2023 tournament: similar to train set.
## Cross-validation
- We can try to use crossvalidation based on years for instance
  -  first fold will be 2022 season and 2021 season and 2021 tournament as train set and 2024 season and 2023 season and 2023 tournament as test set
    - with tournament 2024 to predict (just matchups)
  - second fold will be 2018 season and 2017 season and 2017 tournament as train set and 2020 season and 2019 season and 2019 tournament as test set
    - with tournament 2020 to predict (just matchups)
  - etc.
- We will do this to check if our model would be good in past kaggle competitions.
## Stats to use
- Seed
- Win Rate
- Points per game
- effective field goal percentage
- Turnover rate
- Offensive rebound rate
- Free throw rate
- defensive rebound rate
- etc
- and ofc opponents stats
- Difference in Elo rating
  - ELO of Coach 
  - ELO of Team (?)