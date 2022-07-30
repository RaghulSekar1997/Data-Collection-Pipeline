# Data Collection Pipeline
An end to end, scalable data-pipeline. 

![UML Diagram Data Collection](https://user-images.githubusercontent.com/89411656/177179636-8eadff3f-8bed-4251-a29d-ea2b16a9a6c6.jpg)


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


> The goal of the project is to create a scalable data-pipeline, which runs autonomously within a cloud environment.

> Technologies Used: 

<p align="left"> <a href="https://aws.amazon.com" target="_blank" rel="noreferrer"> 
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws" width="40" href="https://www.docker.com/" target="_blank" rel="noreferrer"> 
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> 
<img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://grafana.com" target="_blank" rel="noreferrer"> 
<img src="https://www.vectorlogo.zone/logos/grafana/grafana-icon.svg" alt="grafana" width="40" height="40"/> </a> <a height="40"/> </a> 
<a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> 
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a  
<img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> 
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> 
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> 
<img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/> </a> </p>


AiCore project to learn about data collection pipelines using web scraping example. The website chosen was 'https://www.bbcgoodfood.com'.

This README documents the actions taken and decisions made during each step of the project.



## Milestone 1 - Decide Target Website
Chose 'https://www.bbcgoodfood.com' to scrape due to the amount of different types of data on the website. The Recipes sectors is very large and data insights could help maximise recipes.

## Milestone 2 - Prototype Finding Target Pages
Environment set up and creating an initial scraper using Selenium to load a webpage and navigate through it to obtain the URLS of pages with the desired information. Classe were created: the scraper class containing the methods (each doing on task) to obtain the urls of the first n (user decision) recipes pages in each category.

This has been a good opportunity to practice object oriented programming, implement expeption handling and gain more insight into how the frontend of a website is structured.

## Milestone 3 - Retrieve Data From Target Pages
Added methods to the scraper class to retrieve the relevant data from each of the recipe pages and save this locally. Thought was put into deciding which data may be relevant and how best to get these e.g. using more robust XPATHs rather than defaults. During this milestone, methods were refactored seveal times to ensure that each one was not reliant on previous, but only dealt with one problem focused on data structures. Work was also put in to remove the need for nest for loops for time efficiency. 

The section has pushed me to consider how my code is working, not just that it does work, and appreciate the traits of different data structures to allow efficient implementation.

## Milestone 4 - Documentation and Testing
The code has a dedicated refactor (rather than just doing it along the way) to further optimise the code. Doc strings have been addeed to all public methods in the Google layout and a combination of unit and end to end tests have been written. Tests have been written only to test the code logic written, leaving out those functions that merely implement python built-in functions. The project structure, including creating build files, was also updated to be more distribution ready.

This milestone has allowed me to understand some of the developer benefits of encapsulation and OOP (in terms of writing test and doc strings!), as well the computational benefits. There are many ways to test the same method and code is always a work in progress, and optimisation/refactoring is an ongoing process.

## Milestone 5 - Scalably Store the Data
Sets up AWS to save image data to S3 bucket and tabular data to a PostgreSQL database on the cloud. Code was updated to implement an AWS port in its own class, and the Scraper methods were updated to save to the cloud rather than locally. Scraper runs successfully with data saving to the cloud. 

## Milestone 6 - Getting More Data
Updates methods to ensure duplicate images are not being scraped from the website. It was deemed un-scalable to store slug names/access the database to prevent the tabular data being scraped for duplicate recipes, however, additional functionality has been added to prevent duplicate recipes data being saved to the database. Tests have been updated for the new functionality.

## Milestone 7 - Containerise Scraper and Run on Cloud Server
Containerised the scraper application using Docker to create a Dcoker Image which was pushed to DockerHub. To run the scraper remote, an EC2 instance was created, which was connected to the S3 bucket and RDS PostgreSQL database. Care was taken around ensuring security group allowed access to the database from the EC2 instance only (rather than from localhost as set up previously). As part of this, used GitHub secrets for authentication credentials to ensure these were not comitted in the code and accidentally made public, posing a security risk.

This milestone has given me practice working with AWS and the start of productionising code.


## Milestone 8 - Monitoring and Alerting
Set up a Prometheus container inside the EC2 instance to monitor the docker container running the scraper and the hardware metrics of the EC2 instance. To view these emtircs, Grafana was used to create a dashboard for monitoring.

## Milestone 9 - Setup CI/CD Pipeline
Created a GitHub Action that is triggered on a push to the main branch of the repository to build the Docker image and push it to my DockerHub account.
