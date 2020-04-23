# Messages of Disaster Response by Figure Eight

## Contents

1. [Installation](#1)
2. [Instructions](#2)
3. [Project Motivation](#3) 
4. [File Descriptions](#4)
5. [Results](#5)
6. [Source, Licensing, Authors, and Acknowledgements](#6)
7. [Conclusion](#7)


---
<p style="text-align: center;"><span style="font-size: 70px; color: #D7D1C9;">&#8912;&#8901;&#8913;</span><em></em></p>

<a id="1"></a>
## 1. Installation

In order to be able to execute your own python statements it should be noted that scripts are only tested on **anaconda navigator 1.9.12** in combination with **python 3.7.6**. The scripts require additional python libraries.

Run the following commands in anaconda prompt to be able to run the scripts that are provided in this git repository.
- ` conda install pandas `
- ` conda install numpy `
- ` conda install scikit-learn `
- ` conda install -c conda-forge nltk_data `
- ` conda install plotly `
- ` conda install joblib `
- ` conda install sqlite3 `
- ` conda install flask `

**` disaster_message.csv  `** and **` disaster_categories.csv  `**  files provided by **Figure Eight**  were used as data. Also, in this project a SQLite database was used on my local machine with library of **`  sqlite3  `** and **` sqlalchemy  `**.
<br>If you want to follow along and execute these scripts you will need to [install SQLite](http://www.sqlitetutorial.net/download-install-sqlite/) on your machine.

---
<p style="text-align: center;"><span style="font-size: 70px; color: #D7D1C9;">&#8912;&#8901;&#8901;&#8913;</span><em></em></p>

<a id="2"></a>
## Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database on shell<br>

    ```python
    python data/process_data.py data/messages.csv data/categories.csv data/DisasterResponse.db
    ```
    - To run ML pipeline that trains classifier and saves on shell
    ```python
    python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
    ```
    - **Notice** : if you want to learn detail about:
        - cleaning look at the file of ` ETLPipelinePreparation.ipynb `
        - machine learning look at the file of ` MLPipelinePreparation.ipynb `
        - Raw data look at the files of `  Disaster_message.csv ` and `  Disaster_Categories.csv  ` at the data folder.

2. Run the following command in the app's directory to run your web app.
    ```python
    python app/run.py
    ```
    
3. Open your browser and navigate to the following URL:
    - `http://localhost:3001`
    - Attention, may be you should change html file for your localhost.
    
---
<p style="text-align: center;"><span style="font-size: 70px; color: #D7D1C9;">&#8912;&#8901;&#8901;&#8901;&#8913;</span><em></em></p>

<a id="3"></a>
## Project motivation
How can we separate a fake _'help request'_ message with a _'real request'_ message stating that it need help. If you want to investigate this, this study will help you.<br>
In this project, I used messages of data by **[Figure Eight](https://www.figure-eight.com/)**. I detected _what messages actually need attention during the event of a disaster._ I did use machine learning algorithms to help for that.<br>
I was very interesting to try out the **NLTK** library.<br>

### Overview
This dataset contains 30,000 messages drawn from events including an earthquake in Haiti in 2010, an earthquake in Chile in 2010, floods in Pakistan in 2010, super-storm Sandy in the U.S.A. in 2012, and news articles spanning a large number of years and 100s of different disasters.<br>
The data has been encoded with 36 different categories related to disaster response and has been stripped of messages with sensitive information in their entirety.<br>
Upon release, this is the featured dataset of a new Udacity course on Data Science and the AI4ALL summer school and is especially utile for text analytics and natural language processing (NLP) tasks and models.

### Desing of 
Data Below, you’ll find a link to the Appen template used to annotate these messages. The “Duplicate Job” button will take you to that template should you want to duplicate the workflow or build on this dataset.<br>

The input data in this job contains thousands of untranslated disaster-related messages and their English translations. In the “Data” tab above, you’ll find the annotated data, with 40 class labels for intent and content.<br>

This dataset contains the original message in its original language, the English translation, and dozens of classes for message content. These classes are noted in column titles with a simple binary 1= yes, 2=no.<br>
Look for [detail](https://appen.com/datasets/combined-disaster-response-data/).

---
<p style="text-align: center;"><span style="font-size: 70px; color: #D7D1C9;">&#8912;&#8901;&#8901;&#8901;&#8901;&#8913;</span><em></em></p>

<a id="4"></a>
## Folder-File Structure of Project

You'll find the following directories and files.

```text
DisasterResponsePipeline/
├──── README.md
├──── ETL Pipeline Preparation.ipynb # Notebook to prepare cleaning function
├──── ML Pipeline Preparation.ipynb  # Notebook to test out machine learning algorithms
├──── app/
     ├──── run.py              # Flask file that runs app
     ├──── templates/
            ├──── master.html  # main page of web app
            └──── go.html      # classification result page of web app  
├──── data/
     ├──── disaster_categories.csv  # data to process
     ├──── disaster_messages.csv    # data to process
     ├──── process_data.py
     └──── DisasterResponse.db      # database to save clean data to
└──── models/
     ├──── train_classifier.py
     └──── classifier.pkl           # saved model, not stored in github repository due to size, run ML pipeline to create this model.
```
---
<p style="text-align: center;"><span style="font-size: 70px; color: #D7D1C9;">&#8912;&#8901;&#8901;&#8901;&#8901;&#8901;&#8913;</span><em></em></p>

<a id="5"></a>
## Results
It was not what I expected, The model did not perform very well.<br>
I had tried optimization techniques to change the predictability of the model, but this did not led to an increase of correct predictions.<br> 
One of the reasons this model did not perform well might be that the data is very skewed, some categories are very rare in the provided dataset, therefore making it hard for algorithms to make correct predictions on these rare conditions.<br>


---
<p style="text-align: center;"><span style="font-size: 70px; color: #D7D1C9;">&#8912;&#8901;&#8901;&#8901;&#8901;&#8901;&#8913;</span><em></em></p>

<a id="6"></a>
## Source, Licensing, Authors, and Acknowledgements

#### Source
The [Source](https://appen.com/datasets/combined-disaster-response-data/) owner is [Figure Eight](https://www.figure-eight.com/)
#### Licensing
The data In this project is **OpenSource** and owner is [Figure Eight](https://www.figure-eight.com/). Also, if _you plan to use this database in your article research or else_ you must taken and read main Source in the **Figure Eight repository**.
#### Authors
Huseyin ELCI <br>
[Github](https://github.com/huseyinelci2000)  |  [Kaggle](https://www.kaggle.com/huseyinelci)  |  [Linkedin](https://www.linkedin.com/in/huseyinelci/)
#### Acknowledgements
Thanks to [Udacity](https://www.udacity.com/) for editing and setting the projects.
Thanks to [Figure Eight](https://www.figure-eight.com/) for providing cool data with which we can create a cutting edge project.

---
<p style="text-align: center;"><span style="font-size: 70px; color: #D7D1C9;">&#8912;&#8901;&#8901;&#8901;&#8901;&#8901;&#8901;&#8901;&#8913;</span><em></em></p>


<a id="7"></a>
## Conclusion
**It was instructive, it was worth it.** You could touch the code. Have a enjoy. **:)**
