from unittest import result
from bs4 import BeautifulSoup
from requests import request
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import concurrent.futures
import time

from src.JobDetails import JobDetails

class Monster:

    def __init__(self, position, location):
        self.postion = position
        self.location = location

    def processMonsterLinks(self, allLinks):

        jobs = []

        for link in allLinks:

            print(link)

            response = requests.get(link)
            
            if response.status_code != 200:
                continue

            monsterJobPage = response.text

            print(monsterJobPage)

            soup = BeautifulSoup(monsterJobPage, 'lxml')

            # description = soup.find('div', {'class': 'descriptionstyles__DescriptionContainer-'}, partial = True).text
            description = ''
            jobTitle = soup.find('h1', class_='JobViewTitle').string

            company = soup.find('h2', class_='headerstyle__JobViewHeaderCompany-sc-1ijq9nh-6').string

            jobs.append(JobDetails(jobTitle, company, link, description, 'Monster'))

        return jobs

    # def processLinkedInLinks2(self, link):

    #     # print(link)

    #     response = requests.get(link)
        
    #     if response.status_code != 200:
    #         return

    #     linkedInJobPage = response.text

    #     soup = BeautifulSoup(linkedInJobPage, 'lxml')

    #     description = soup.find('div', class_='show-more-less-html__markup').text

    #     jobTitle = soup.find('h1', class_='top-card-layout__title').string

    #     company = soup.find('a', class_='topcard__org-name-link').string

    #     return JobDetails(jobTitle, company, link, description, 'LinkedIn')

        


    # https://www.linkedin.com/jobs/search?keywords=developer%20&location=Windsor
    def process(self):
        

        # https://www.monster.ca/jobs/search?q=web+developer+&where=windsor
        urlBase = 'https://www.monster.ca/jobs/search?'

        jobPosition = 'q=' + self.postion.strip().replace(' ', '+')
        jobLocation = '&where=' + self.location.strip()

        searchUrl = urlBase + jobPosition + jobLocation

        browser=webdriver.Chrome()
        browser.get(searchUrl)
        target = browser.find_element_by_class_name('job-search-resultsstyle__LoadMoreContainer-sc-1wpt60k-1')
        i = 0
        while i < 3:

            actions = ActionChains(browser)
            actions.move_to_element(target)
            actions.perform()
            time.sleep(2)
            i += 1

        pageSource = browser.page_source

        browser.close()

        soup = BeautifulSoup(pageSource, 'lxml')

        allAnchors = soup.find_all('a', class_='job-cardstyle__JobCardTitle-sc-1mbmxes-2')

        allLinks = []

        for anchor in allAnchors:
            # print(anchor['href'])
            allLinks.append('https:' + anchor['href'])

        return self.processMonsterLinks(allLinks)
        
        # jobs = []
        # with concurrent.futures.ThreadPoolExecutor() as exec:
        #     jobs = exec.map(self.processLinkedInLinks2, allLinks)

        # return jobs



        # CSVWriter.writeToCsv(jobs, 'LinkedIn_Jobs.csv')
        # CSVWriter.writeToCsv(jobs, self.csvName)




