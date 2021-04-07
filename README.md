# recommendation_model <br/>
PyCharm can be used to run this file locally. <br/>
Run the following command to install scikit-surprise 1.1.1
 -> !pip install surprise
 Dataset contains item wise ratings provided various friends of the user.
 Each friend has a weight depending upon the similarities with the user.
 If a certain friend has not rated an item then it will have a rating = 0. 
 The model uses user-based cosine similarity to give the predictions.
