# Customer Satisfaction Analysis System

This is a decision support system for analyzing customer satisfaction in online shopping platforms using machine learning algorithm Support Vector Machine.
It includes a web application for user interaction and sentiment analysis of product reviews.

## Getting Started

Follow these instructions to set up and run the system locally.

### Prerequisites
- Python 3.11.4
  - Required Python libraries (listed in `requirements.txt`)
- SVM Model
- Model Dependency
  - SpaCy's NLP model, en_core_web_sm

### Installation
1. <b>Clone the Repository:</b> 
    ```bash
   gh repo clone Aerienn/Rev-Us
    ```
3. <b>Install the required dependencies:</b>
    ```bash
    pip install -r requirements.txt
    ```
    Note: It is recommended to create a virtual environment.

4. <b> Obtain the SVM Model.</b>
      - You can use this project's SVM model. ([TF-IDF Vectorizer](https://drive.google.com/file/d/1EzHFwNxd1FXUvZ8sArzX0moWrhA0fdHP/view?usp=drive_link) and [SVM Classifier](https://drive.google.com/file/d/1ABWUGve7-HnrITGXyiQ2GpGj0yEXaOxm/view?usp=drive_link)).
      Save the joblib files in `machine_learning/models/` folder
      - If you want to make your own model, You may use the provided jupyter notebooks in the machine learning folder. Please check the README file in the machine_learning folder for the complete instructions.

5. <b>Model Dependency: </b> In order to perform a consolidated analysis with our tool, you will need to download the 'en_core_web_sm' SpaCy model. This model provides essential linguistic information for various natural language processing tasks. In the website's case, the model is used to analyze the what are the top negative,positive, and neutral phases.
    ```bash
    python -m spacy download en_core_web_sm
    ```

6. <b> Running the Web app:
    - For Development:
    ```bash
    set FLASK_ENV=development
    python run.py
    ```
    
    - For Production:
    ```
    waitress-serve --host=127.0.0.1 --port=5000 app:app
    ```
      You can deploy the app online using [ngrok](https://ngrok.com/download).


## Data Source

The dataset used in this project was obtained from the [Amazon Review Data (2018)](https://nijianmo.github.io/amazon/index.html#subsets) generously provided by Jianmo Ni, UCSD.

- Dataset Name: Amazon Review Data (2018)
- Source: [https://nijianmo.github.io/amazon/index.html#subsets](https://nijianmo.github.io/amazon/index.html#subsets)
- Citation:
  "Justifying recommendations using distantly-labeled reviews and fined-grained aspects"
  Jianmo Ni, Jiacheng Li, Julian McAuley
  Empirical Methods in Natural Language Processing (EMNLP), 2019
  [PDF](http://cseweb.ucsd.edu/~jmcauley/pdfs/emnlp19a.pdf)
