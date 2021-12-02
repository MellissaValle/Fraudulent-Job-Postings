![fraudulent](https://images.tmcnet.com/tmc/misc/articles/image/2020-jan/3871346650-hacker-adobe.jpeg)
# Fraudulent Job Postings!! 
### Author: Mellissa Valle
## Table of Contents
* [Reproducibility](#reproducibility)
* [Business Problem](#business-problem)
* [Business Understanding](#business-understanding)
* [Machine Learning Models](#machine-learning-models)
* [Conclusions and Next Steps](#conclusions-and-next-steps)
* [Navigating the Repository](#navigating-the-repository)

## Reproducibility
### Data
I gathered my data from these sources:

[Kaggle Competition](https://www.kaggle.com/shivamb/real-or-fake-fake-jobposting-prediction)

[Indeed Dataset](https://data.world/promptcloud/indeed-job-posting-dataset/workspace/project-summary?agentid=promptcloud&datasetid=indeed-job-posting-dataset)

### Dependencies
[environment.yml](https://github.com/MellissaValle/Fraudulent-Job-Postings/blob/main/environment.yml)
[requirement.txt](https://github.com/MellissaValle/Fraudulent-Job-Postings/blob/main/requirements.txt)

## Business Problem 
![Image3](https://user-images.githubusercontent.com/74070082/144143954-625bdac0-4e54-46e5-8a5a-c12884505fd3.png)

[www.fbi.gov/contact-us/field-offices/elpaso/news](https://www.fbi.gov/contact-us/field-offices/elpaso/news/press-releases/fbi-warns-cyber-criminals-are-using-fake-job-listings-to-target-applicants-personally-identifiable-information)

Can't tell if a job posting is legit? Unfortunately, there are a lot of scammers out there that can and will take advantage of jobseekers. So if you think a job posting isn't real, it probably isn't, we humans can have an idea how to detect those, one by one. But how much time would it take a company like Indeed to accurately identify and take down thousands and thousands of fraudulent job postings? 
#### There are several reasons why fake job postings exist: 

1. Some spammers who would get the jobseeker's email address and then sell it to other individuals. 
2. Also Scammers!! Criminals who want to steal money or even the individual's identity.

## Business Understanding
The hiring process has relatively recently been moved to the cloud. Specifically, the automated systems responsible for completing the recruitment of new employees in an online fashion, to make the hiring process faster and cost-efficient. However, the online exposure of such traditional business procedures has introduced new points of failure that may lead to privacy loss for applicants and harm the reputation of organizations. 
On the downside, the increasing adoption of online applications has also attracted the interest of scammers. Putting at risk not only the job seekers' privacy but also the credibility of organizations such as Indeed, Monster, CareerBuilder, etc.

![Image4](https://user-images.githubusercontent.com/74070082/144143983-181cf53d-f405-4fca-9e57-6998488b779c.png)

[www.fox2detroit.com/news](https://www.fox2detroit.com/news/indeed-com-scam-steals-personal-info-from-woman-with-fake-job-posting)

## Data Understanding
![Target](https://user-images.githubusercontent.com/74070082/143786875-797c8179-3d69-4e59-afcd-58ac4695d1bc.png)

Dataset used for modeling contains 17,014 legitimate and 866 fraudulent job ads (17,880 in total). All the entries were manually annotated by specialized human employees.The criteria for the classification were based on the client's suspicious activity on the system, false contact or company information, candidate complaints and periodic meticulous analysis of the clientele. 

Indeed test data contains 3002 records, all from the USA.

## Data Preparation
![Image6](https://user-images.githubusercontent.com/74070082/144144150-d27bf530-0d03-40e8-822f-d0fd3870c94e.png)

Most common words fraudulent job postings.

- English stop-words such as "the, that, with, etc..." were removed.
- Numbers and symbols were also removed
- I created the bag of words (bow) to experiment for modeling with the job description, benefits, requirements, etc. Before feeding it  to several classifiers like Naives Bayes decision trees, random forest and logistic regression (LR)

## Machine Learning Models
Computers are pretty good at learning from spreadsheets of data and numbers but we humans communicate with words not with numbers, Natural Language Processing NLP is focused on enabling computers to understand and communicate in human language.
### Models tried:
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier 
- Best Model:
Tuned Logistic Regression with CountVectorizer and RandomOverSampler

![Model](https://user-images.githubusercontent.com/74070082/144143583-e9684750-d44d-4330-afee-d67bbeb254bf.png)

Accuracy: 97.968%
Recall:  82.686%

## Conclusions and Next Steps
![IndeedPred](https://user-images.githubusercontent.com/74070082/144143750-ed5eaa47-e1c1-45ce-98f7-d62314613877.png)
### Conclusion
Key words: Reduction in time!  With this model, the process of detecting fake job postings would be much quicker. Indeed must have some kind of mechanism to find these fraudulent posts, but it probably takes a while. This model analyzes the job posts and flags those that are predicted to be fake/fraudulent, making this process of flagging  much faster.
This model will not detect immediately which ones are fraudulent to 100% but it will make it a lot easier. Instead of going through 30k I hope I can only have to go through a few thousands. 

Indeed, my model predicted:
Not fraudulent    28705
Fraudulent    1297
### Recommendations 

Add  industry and department features with Selectbox, people tend to misspell and or abbreviate words(eg. IT, Information Technology). These features can potentially help flagging those fraudulent postings. 


### Next steps
TBD


## Navigating the Repository
```
├── notebooks
│         ├──EDA1.ipynb <---------- Labelled Dataset EDA
│         ├──Machine_Learning_Models.ipynb <----------- All Models tried
│         └──Indeed_EDA.ipynb <----------- Indeed Dataset EDA
├── images
│         ├──Image1.JPG
│         ├──Image2.JPG
│         ├──Image3.JPG
│         ├──Image4.JPG
│         └──Image5.JPG
├── README.md
├── presentation.pdf <-------- Non-Technical presentation Deck
├── requirements.txt 
├── environment.yml
├── utils.py <--------- functions used to clean data
└── notebook.ipynb <--------- Complete Analysis
```
