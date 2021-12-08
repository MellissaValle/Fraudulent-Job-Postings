![fraudulent](https://images.tmcnet.com/tmc/misc/articles/image/2020-jan/3871346650-hacker-adobe.jpeg)
# Fraudulent Job Postings!! 
### Author: Mellissa Valle
## Table of Contents
* [Business Problem](#business-problem)
* [Business Understanding](#business-understanding)
* [Machine Learning Models](#machine-learning-models)
* [Conclusion and Next Steps](#conclusion-and-next-steps)
* [Navigating the Repository](#navigating-the-repository)

## Business Problem 
![Image3](https://user-images.githubusercontent.com/74070082/144143954-625bdac0-4e54-46e5-8a5a-c12884505fd3.png)

[www.fbi.gov/contact-us/field-offices/elpaso/news](https://www.fbi.gov/contact-us/field-offices/elpaso/news/press-releases/fbi-warns-cyber-criminals-are-using-fake-job-listings-to-target-applicants-personally-identifiable-information)

Can't tell if a job posting is legit? Unfortunately, there are a lot of scammers out there that can and will take advantage of jobseekers. We humans can have an idea of how to detect those, one by one. But how much time would it take a company like Indeed to accurately identify and take down thousands and thousands of fraudulent job postings? 
#### There are several reasons why fake job postings exist: 

1. Some spammers who would get the jobseeker's email address and then sell it to other individuals. 
2. Also Scammers!! Criminals who want to steal money or even the individual's identity.

## Business Understanding
The hiring process has relatively recently been moved to the cloud. Specifically, the automated systems responsible for completing the recruitment of new employees in an online fashion, to make the hiring process faster and cost-efficient. However, the online exposure of such traditional business procedures has introduced new points of failure, the increasing adoption of online applications also attracts the interest of scammers. Putting at risk not only the job seekers' privacy but also the credibility of organizations such as Indeed, Monster, CareerBuilder, etc.

![Image4](https://user-images.githubusercontent.com/74070082/144143983-181cf53d-f405-4fca-9e57-6998488b779c.png)

[www.fox2detroit.com/news](https://www.fox2detroit.com/news/indeed-com-scam-steals-personal-info-from-woman-with-fake-job-posting)

## Data Understanding
![Target](https://user-images.githubusercontent.com/74070082/143786875-797c8179-3d69-4e59-afcd-58ac4695d1bc.png)

I gathered my data from these sources:
[Kaggle Competition](https://www.kaggle.com/shivamb/real-or-fake-fake-jobposting-prediction)
[Indeed Dataset](https://data.world/promptcloud/indeed-job-posting-dataset/workspace/project-summary?agentid=promptcloud&datasetid=indeed-job-posting-dataset)

Both datasets were downloaded as .csv files and saved into a `Data` folder

The labelled dataset used for modeling contains 17,014 legitimate and 866 fraudulent job ads (17,880 in total). All the entries were manually annotated by specialized human employees.The criteria for the classification were based on the client's suspicious activity on the system, false contact or company information, candidate complaints and periodic meticulous analysis of the clientele. 

The second dataset is scrapped from Indeed to test on my model and see if my model flags any. The Indeed dataset contains 3002 records, all from the USA.

## Data Preparation
![WORDSFAKE](https://user-images.githubusercontent.com/74070082/144646986-83731455-c0f9-45c7-a6b4-a58fc07d06a7.png)

Most common words fraudulent job postings.

- English stop-words such as "the, that, with, etc..." were removed.
- Numbers and symbols were also removed
- I created the bag of words (bow) to experiment for modeling with the job description, benefits, requirements, etc. Before feeding it  to several classifiers such as Naives Bayes decision trees, random forest and logistic regression (LR)

## Machine Learning Models
Computers are good at learning from spreadsheets of data and numbers but we humans communicate with words not with numbers, Natural Language Processing NLP is focused on enabling computers to understand and communicate in human language.
### Models tried:
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier 
- Best Model:
Tuned Logistic Regression with CountVectorizer and RandomOverSampler

![BESTMODEL](https://user-images.githubusercontent.com/74070082/144646882-6dfb141f-ddb2-45da-8e8d-ff836d01fb58.png)

- Accuracy: 97.673%  
- Recall: 81.818%

## Conclusion and Next Steps

### Conclusion
Key words: Reduction in time!  With this model, the process of detecting fake job postings would be much quicker. Indeed must have some kind of mechanism to find these fraudulent posts, but it probably takes a while. This model analyzes the job posts and flags those that are predicted to be fake/fraudulent, making this process of flagging  much faster.

This model will not detect immediately which ones are fraudulent to 100% but it will make it a lot easier. Instead of going through 30k I hope I only have to go through a few thousands. 

From the Indeed dataset, my model predicted:
- Not fraudulent:    28703 
- Fraudulent:    1299

### Recommendations and Next steps

- Add  industry and department features with Selectbox: people tend to misspell and or abbreviate words(eg. IT, Information Technology). 

- Test a dataset from different Job Search Site such: CareerBuilder, Glassdoor, Monster

- Add another second language:  Spanish 

These features can potentially help flagging those fraudulent postings.



## Navigating the Repository
```
├── notebooks
│         ├──EDA1.ipynb <---------- Labelled Dataset EDA
│         ├──Machine_Learning_Models.ipynb <----------- All Models tried
│         └──Indeed_EDA.ipynb <----------- Indeed Dataset EDA
├── images
│         ├── ... <-------- Images used for README
├── .gitignore  <------- Large Datasets listed here
├── README.md
├── presentation.pdf <-------- Non-Technical presentation Deck
├── requirements.txt 
├── environment.yml
├── utils.py <--------- functions used to clean data
└── notebook.ipynb <--------- Completed Analysis
```
