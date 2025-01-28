# Ensemble Learning with Semantic Feature Fusion
This repository contains resources related to the research titled "**Ensemble Learning Approach with Semantic Feature Fusion for Granular Nucleosome Position Mapping**."
This work emphased the spatio-temporal dependencies inherent in the DNA sequence and proposed an ensemble learning model with semantic feature fusion. A detailed archtecture for the proposed framework which consists of core spaces including the Data Space, the Feature Fusion Space, and the Model Space.

<p align="center">
<img src="https://github.com/shahid3167/Ensemble_Learning_with_Semantic_Feature_Fusion/blob/ca8c6adafb0b3b6ca913754e6ebf90237e1122f1/Figures/SystemModel.jpg" width="700" height="500">


**System model of the ensemble learning framework highlighting data, feature fusion, and model spaces**

## Proposed Framework
### Data Space
The **Data Space** represents the continuous nature of DNA and RNA sequences and emphasizes the necessity of transforming these continuous chains into **semantic vector representations** through **tokenization and vectorization** processes. 

### Feature Fusion Space
The **Feature Space** presents the cosine **semantic similarity mechanism** to characterize the semantic relationship among the vectorized tokens and subsequently **fuse the correlated features into a semantic vector** that is utilized in the developed framework. A section also provides a detailed mathematical framework for identifying the semantic relationships and fusion mechanisms.

### Model Space
The **Model Space** presents a **mathematical framework** for the individual models such as **Fully Connected Network and Convolutional Neural Network** to capture the **spatial dependencies**, while **Gated Recurrent Unit and Long Short-Term Memory Networks** address the **temporal dependencies**. Furthermore, a **hybrid function** leveraging the **uniform and weighted inference** mechanisms fuses these **spatio-temporal-based models** into the developed **ensemble learning framework**.

## Results
The developed framework is applied to three (**C. elegans, D. melanogaster, and H. sapiens**) datasets (available in the dataset folder) and the results are evaluated under several different scenarios against the individual models (FCN, CCN, GRU, and LSTM) and state-of-the-art DNA identification models, followed by statistical evaluation using mean, standard deviation, and 95% confidence interval.

### With and Without Semantic Fusion
To highlight the **impact of semantic feature fusion**, a **with and without feature fusion** evaluation is conducted on the developed **ensemble learning framework**. The results showcased a significant influence on various performance metrics (**Accuracy, Sensitivity, and Specificity**) across the **C. elegans, D. melanogaster, and H. sapiens**  datasets.

<p align="center">
<img src="https://github.com/shahid3167/Ensemble_Learning_with_Semantic_Feature_Fusion/blob/a007c764193dbd6663d3648de1d0d75cfffd9197/Figures/WithWithoutFusion_Accuracy.jpg" width="700" height="300">



