TopNPI.com Physicians Review scraper
=====================================

### About

Spider built with [Scrapy](http://scrapy.org/). Scrapes pull Physicians info with Review from  [topnpi.com](https://www.topnpi.com/ny1366769796/dr-joseph-fasanello) and Exporter pipeline has been added that will generate result in csv file in each run. [Take a look on this exporter folder there is one sample csv result file]

Further scope to add back-end MySQL DB tables [ Example: `master_reviews` & `master_surveys` ], Log files in "logs" folder , log info table to track activities in `log_history` table, email notification etc features can be added.

### Data Fields:
+ name
+ category
+ description
+ hospitalAffiliation
+ email
+ telephone
+ reviewer_name
+ review_date
+ review
+ recommend
+ url


### Installation and Running
```
git clone https://github.com/azambd/topnpi.git
cd topnpi
scrapy crawl topnpi_review
```

### Note

If you need any help to upgrade this spider to a production version, shoot an email to me - I'll help you.
