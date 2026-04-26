# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
**Model Name: Census Income Classifier**
**Model developed with Udacity starter code templates and completed by Udacity student Taylor Hiedeman.**
**Model Version: 1.0.0**
**Model Type: Logistic Regression (sklearn)**
**sklearn Logistic Regression model predicts binary classifcation of salary in the census dataset being less than or greater than $50K annually.**

## Intended Use
**This model's intended use is to predict a binary classification of annual income being greater than or less than $50K based on age, education, and other demographics in the census dataset. It's main purpose is educational as part of Udacity's Machine Learning DevOps course.**

## Training Data
**The training data is 70% of the census dataset with numerical and one-hot-encoded categorical features. The Logistic Regression model is fit with the training data.**

## Evaluation Data
**The test data (evaluation data) is the remaining 30% of the census dataset.**

## Metrics
**Precision: 0.7157**
**Recall: 0.5527**
**F1 Score: 0.6238**

## Ethical Considerations
**The census data contains sensitive demographic information such as age, sex, and race. Societal biases of various classes of people exist, so any predictions obtained from this model may also share those biases. Ethically, this model should not be used for anything that may have a negative impact, such as a loan application.**

## Caveats and Recommendations
**This model is trained on a simplified census dataset and therefore should not be used for any real predictions unless the model is retrained on a complete and current dataset. There are societal biases that exist in the data, so performance should be checked against different demographic slices before any type of deployment. This model is strictly for educational purposes.**