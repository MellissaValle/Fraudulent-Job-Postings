# Fraudulent Job Postings!! 
![fraudulent](https://images.tmcnet.com/tmc/misc/articles/image/2020-jan/3871346650-hacker-adobe.jpeg)
### Author: Mellissa Valle
## Business Problem 
![Image3](https://user-images.githubusercontent.com/74070082/144143954-625bdac0-4e54-46e5-8a5a-c12884505fd3.png)
![Image5](https://user-images.githubusercontent.com/74070082/144143013-b3cba2d0-1dea-4206-9358-428b36cee995.png)

Can’t tell if a job posting is legit? Unfortunately, there are a lot of scammers out there that can and will take advantage of jobseekers. So if you think a job posting isn’t real, it probably isn’t, we humans can have an idea how to detect those, one by one. But how much time would it take a company like Indeed to accurately identify and take down thousands and thousands of fraudulent job postings? 
#### There are several reasons why fake job postings exist: 
1. Actual employers without any intention to hire anyone but might be just testing the waters, to see what talents are out there.
2. Some spammers who would get the jobseeker’s email address and then sell it to other individuals. 
3. And lastly the Scammers, criminals who want to steal money or even the individual’s identity.

## Business Understanding
The hiring process has relatively recently been moved to the cloud. Specifically, the automated systems responsible for completing the recruitment of new employees in an online fashion, to make the hiring process faster and cost-efficient. However, the online exposure of such traditional business procedures has introduced new points of failure that may lead to privacy loss for applicants and harm the reputation of organizations. 
On the downside, the increasing adoption of online applications has also attracted the interest of scammers. Putting at risk not only the job seekers’ privacy but also the credibility of organizations such as Indeed, Monster, CareerBuilder, etc.
![Image4](https://user-images.githubusercontent.com/74070082/144143983-181cf53d-f405-4fca-9e57-6998488b779c.png)


## Data Understanding
![Target](https://user-images.githubusercontent.com/74070082/143786875-797c8179-3d69-4e59-afcd-58ac4695d1bc.png)

## Data Preparation
![Image6](https://user-images.githubusercontent.com/74070082/144144150-d27bf530-0d03-40e8-822f-d0fd3870c94e.png)

## Models
Computers are pretty good at learning from spreadsheets of data and numbers but we humans communicate with words not with numbers, Natural Language Processing NLP is focused on enabling computers to understand and communicate in human language.
### Models tried:
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier 
- Best Model:
Tuned Logistic Regression with CountVectorizer and RandomOverSampler
![Model](https://user-images.githubusercontent.com/74070082/144143583-e9684750-d44d-4330-afee-d67bbeb254bf.png)

## Conclusions and Next Steps
![IndeedPred](https://user-images.githubusercontent.com/74070082/144143750-ed5eaa47-e1c1-45ce-98f7-d62314613877.png)


## Navigating the Repository
```
├── notebooks
│         ├──EDA1.ipynb
│         ├──Models.ipynb
│         └──Indeed_NB.ipynb
├── images
│         ├──Image1.JPG
│         ├──Image2.JPG
│         ├──Image3.JPG
│         ├──Image4.JPG
│         └──Image5.JPG
├── README.md
├── presentation.pdf
└── fraudulent-job-ads.ipynb
```
