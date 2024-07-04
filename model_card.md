# Model Card

## Model Details
Machine learning model for income prediction using Sckikit-Learn's GradientBoostingClassifier.

## Intended Use
Predicting whether an individual's income is above $50,000

## Training Data
The model was trained on 80% of the total dataset. The data was preprocessed using OneHotEncoder LabelBinarizer.

## Evaluation Data
The model was tested on the remaining 20% of the dataset.

## Metrics
Precision: 0.7772 | Recall: 0.5995 | F1: 0.6769

## Ethical Considerations
Inherent biases in the training data may impact bias in the model.

## Caveats and Recommendations
Users should test the model on newer population data when available.