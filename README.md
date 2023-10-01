# Student Performance

![Cover-Image](https://codetoanbug.com/wp-content/uploads/2023/01/1-07.41.05.jpeg)

## Introduction

This machine learning project focuses on building and training an artificial neural network using PyTorch to predict students' performance in secondary education from attributes including student grades, demographic, social and school related features. Data for this project was collected from [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/dataset/320/student+performance) and was preprocessed using pandas, numpy and scikit-learn. A transformation pipeline was built to handle categorical and numerical transformation conveniently. A Feed-Forward-Network was designed using linear and batch normalization layers. The trained scikit-learn transformers and network parameters were saved for later use. The model will be deployed as a web application for educational purposes.

## Results
![MSE-Loss-Plot](images/MSE-Loss.png)

- The training loss and test loss curves are both decreasing over time, which indicates that the model is learning.
- The training loss and the test loss are close to each other and the former is below the latter, which indicates that the model is not overfitting to the training data.
- The test loss is relatively low, which indicates that the model is able to generalize well to unseen data.

## Usage
The model is hosted as a free web service on streamlit community cloud and can be accessed through this link: [student-performance-prediction-ml](https://github.com/shre-db/Student-Performance-ML).

Alternatively, you can run the web application locally by following these steps:

1. Choose a project directory on your local machine (e.g., C:\Users\yourname\projects\).
2. Clone this repository by typing the following command in your terminal: 
    ```
    git clone git@github.com:shre-db/Student-Performance-ML.git
    ```
    (Note: If you're on Windows, you could use 'Git Bash' instead of 'cmd' for executing git commands).
3. Before proceeding, make sure you have a Python interpreter installed (recommended version is Python 3.7+). Ensure that Python is added to the PATH environment variable during installation.
4. Open a terminal (e.g., 'cmd' on Windows) and navigate to the project directory (e.g., C:\Users\yourname\projects\).
5. Create a virutal environment running the following command:
    ```
    python -m venv student
    ```
6. Install dependencies by executing this command:
    ```
    pip install -r requirements.txt
    ```
7. Once all the dependencies are installed, run the web application locally with the following command:
    ```
    streamlit run app.py
    ```

If you have followed the instructions correctly, a new tab should open in your default web browser.

## References

1. Cortez,Paulo. (2014). Student Performance. UCI Machine Learning Repository. https://doi.org/10.24432/C5TG7T.

