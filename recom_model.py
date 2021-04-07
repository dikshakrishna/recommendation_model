import pandas as pd
from surprise import Dataset
from surprise import Reader

# with one new user "E" who has rated only one product out of two, now check whether product 2 will be liked by he/she
ratings_dict = {
    "item": [1, 2, 1, 2, 1, 2, 1, 2, 1],
    "user": ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E'],
    "rating": [1, 2, 2, 4, 2.5, 4, 4.5, 5, 3],
}

df = pd.DataFrame(ratings_dict)
reader = Reader(rating_scale=(1, 5))

# Loads Pandas dataframe
data = Dataset.load_from_df(df[["user", "item", "rating"]], reader)

# recommender.py

from surprise import KNNWithMeans

# To use user-based cosine similarity
sim_options = {
    "name": "cosine",
    "user_based": True,  # Compute  similarities between user
}
algo = KNNWithMeans(sim_options=sim_options)

trainingSet = data.build_full_trainset()

algo.fit(trainingSet)



#predicting on the basis of user that how much E would rate to the second product
prediction = algo.predict('E', 2)
prediction.est
if(prediction.est>3.5):
  print('The product is recommended.')
  print('Here, the prediction estimate is : '+str(prediction.est))