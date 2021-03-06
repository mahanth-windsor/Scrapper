from bs4 import BeautifulSoup
from requests import request
import requests
from selenium import webdriver
import time

from src.JobDetails import JobDetails
from writeCSV import CSVWriter

class LinkedIn:

    def processLinkedInLinks(self, allLinks):

        jobs = []

        for link in allLinks:

            # print(link)

            response = requests.get(link)
            
            if response.status_code != 200:
                continue

            linkedInJobPage = response.text

            soup = BeautifulSoup(linkedInJobPage, 'lxml')

            description = soup.find('div', class_='show-more-less-html__markup').text

            jobTitle = soup.find('h1', class_='top-card-layout__title').string

            company = soup.find('a', class_='topcard__org-name-link').string

            jobs.append(JobDetails(jobTitle, company, link, description, 'LinkedIn'))

        return jobs

    def process(self):
        browser=webdriver.Chrome()
        browser.get("https://ca.linkedin.com/jobs/search?keywords=&location=Windsor")

        i = 0
        while i < 1:

            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
            i += 1

        pageSource = browser.page_source

        browser.close()

        soup = BeautifulSoup(pageSource, 'lxml')

        allAnchors = soup.find_all('a', class_='base-card__full-link')

        allLinks = []

        for anchor in allAnchors:
            allLinks.append(anchor['href'])

        jobs = self.processLinkedInLinks(allLinks)

        # CSVWriter.writeToCsv(jobs, 'LinkedIn_Jobs.csv')
        CSVWriter.writeToCsv(jobs, 'All_Jobs.csv')




