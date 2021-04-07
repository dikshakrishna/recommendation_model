# recommendation_model <br/>
PyCharm can be used to run this file locally. <br/>
Run the following command to install `scikit-surprise 1.1.1`  <br/>
 ```!pip install surprise``` <br/> 
 Dataset contains item wise ratings provided various friends of the user. <br/>
 Each friend has a weight depending upon the similarities with the user. <br/>
 If a certain friend has not rated an item then it will have a rating = 0. <br/>
 The model uses user-based cosine similarity to give the predictions.
