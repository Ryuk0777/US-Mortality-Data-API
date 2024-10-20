# USA Mortality Data API
A RESTful API for accessing and analyzing USA mortality data (2011-2013), grouped by region, gender, Cause and urban/rural status. This project was built using Python's Flask framework, with the dataset stored in MongoDB after being processed from CSV format.

**Project Overview**
This API provides endpoints to query USA mortality rates based on various factors such as region, gender, cause and urban/rural classification. The API is designed to offer efficient data access for further analysis and visualization.

**Features**
1. API for USA Mortality Data: Query mortality data by various dimensions.

2. MongoDB Storage: Efficient and scalable data storage solution.

3. Python Flask: Lightweight and flexible framework to build the API.


**Technologies Used:**
1. Flask (Python)
2. MongoDB
3. Pandas (for CSV data processing)


### Usage:

Request link ->  "http://127.0.0.1:5000/<-Your Data Request->"

**Data Request:**

1. Region
2. Urban || Rural
3. Gender
4. Cause
5. Region-Urban || Rural
6. Cause-Urban || Rural
7. Cause-Gender
8. Region-Rural-Gender
9. Region-Urban-Gender
10. Cause-Urban-Gender
11. Cause-Rural-Gender

Example -> "http://127.0.0.1:5000/Region"


**Data Request by Regions**

1. HHS<-Region NO->-Cause

Example -> "http://127.0.0.1:5000/HHS1-Cause"

2. HHS<-Region NO->-Urban || Rural

Example -> "http://127.0.0.1:5000/HHS1-Urban || Rural"

3. HHS<-Region NO->-Gender

Example -> "http://127.0.0.1:5000/HHS1-Gender"


4. HHS<-Region NO->-Cause-Urban || Rural

Example -> "http://127.0.0.1:5000/HHS1-Cause-Urban || Rural"

5. HHS<-Region NO->-Cause-Gender

Example -> "http://127.0.0.1:5000/HHS1-Cause-Gender"

6. HHS<-Region NO->-Urban || Rural-Cause

Example -> "http://127.0.0.1:5000/HHS1-Urban || Rural-Cause"