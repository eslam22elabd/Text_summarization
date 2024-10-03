#  Text_summarization


## Introduction
Now days it's really a hectic task to generate title to any realtime article like news or comments. As we see the increasing need of real-time data to leverage the models to their full potential, so that any content can be summarized with 10-15 words.

## Requirements
- Python 3.7 or higher
- Required libraries:
  - pandas
  - numpy
  - seaborn
  - transformers
  - datasets
  - scikit-learn
  - nltk
  - fastapi
  - uvicorn
 
# There are two Files large so we will put the links in this file and you can download files from here 
1-File summarization_toknizer
- [Download Large File](https://drive.google.com/drive/folders/1G3fde_aTZnN3f06JA3yfcafS14IsuXBL?usp=sharing)
2_ File summarization_model
- [Download Large File](https://drive.google.com/drive/folders/1oOYyi837cHpA_IbEWNaJMrD2fIe4M6av?usp=sharing)


You can install the requirements using:
```bash
pip install -r requirements.txt

project-directory/
|
├──summarization_toknizer
├── summarization_model
├── main.py                     # FastAPI application                    # Testing script for the model
├── README.md                   # This file
└── requirements.txt            # Project dependencies



How to Use
Run the Model: You can start the application using the following command:

uvicorn main:app --reload




