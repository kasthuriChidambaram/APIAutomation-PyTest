# API Automation with Pytest-BDD
This project demonstrates API automation using pytest-bdd to test the functionality of creating, deleting, and verifying bookings using the Restful Booker API. The tests are written following Behavior-Driven Development (BDD) principles using Gherkin syntax.

# Prerequisites
Before you begin, ensure you have the following installed:

Python 3.8 or higher
Pip (Python package installer)

## Project Setup
1.Clone the Repository
https://github.com/kasthuriChidambaram/APIAutomation-PyTest.git

2.Install Dependencies
Install the required Python packages using pip:
pip install -r requirements.txt

# Running the Tests
1.Run Tests Locally
To run the tests, simply use:

         pytest
    
This will automatically discover and run all the test cases defined in the features folder.

2.Generate an HTML Report
You can generate an HTML report using pytest-html by running:
    
     pytest --html=report.html

# Continuous Integration with Jenkins
This project includes a Jenkinsfile to automate the testing process and publish an HTML test report.


# Jenkins Setup Instructions
Create a Jenkins Job: Create a new Jenkins pipeline job and point it to your Git repository.

Configure Jenkinsfile: Jenkins will automatically detect and run the pipeline defined in the Jenkinsfile.

Publish Test Report: After the tests are run, Jenkins will publish the HTML report, which can be accessed from the job’s build page.