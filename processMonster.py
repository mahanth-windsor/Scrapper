from bs4 import BeautifulSoup
from requests import request
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

from src.JobDetails import JobDetails

class Monster:

    def __init__(self, position, location, numberOfJobs):
        self.postion = position
        self.location = location
        self.numberOfJobs = numberOfJobs

    # def processClassElements(self, elem, className, soup):

    #     text = ''
    #     for t in soup.find_all(elem, className):
    #         text += t.string

    #     return text

    def processMonsterLinks(self, jobCards):

        jobs = []

        jobCount = 0

        for card in jobCards:

            if jobCount > self.numberOfJobs:
                break
            
            try:
                link = 'https:' + card.a['href']
                jobTitle = card.a.text
                company = card.h3.text

                jobPage = requests.get(link).text
                jobPageSource = BeautifulSoup(jobPage, 'lxml')
                description = jobPageSource.find('main').text
            except:
                print('Attribute Error  at processMonsterLinks')

            # with open('jobcards.txt', 'a') as f:
            #     f.write('card -------------------------------------------------')
            #     f.write('\n link ----> ' + link)
            #     f.write('\n position ----> ' + jobTitle)
            #     f.write('\n company ---> ' + company)
            #     f.write('\n description ---> ' + description)
            #     f.write('\ncard -------------------------------------------------')
            #     f.write('\n')


            jobs.append(JobDetails(jobTitle, company, link, description, 'Monster'))

            jobCount += 1

        return jobs        


    # https://www.linkedin.com/jobs/search?keywords=developer%20&location=Windsor
    def process(self):
        

        # https://www.monster.ca/jobs/search?q=web+developer+&where=windsor
        urlBase = 'https://www.monster.ca/jobs/search?'

        jobPosition = 'q=' + self.postion.strip().replace(' ', '+')
        jobLocation = '&where=' + self.location.strip()

        searchUrl = urlBase + jobPosition + jobLocation

        try:        
            browser=webdriver.Chrome()
            browser.get(searchUrl)
        except:
            print('Selenium connection error in process of monster')

        jobCards = []
        j = 0

        while len(jobCards) == 0 and j < 3:
            
            try:
                target = browser.find_element_by_class_name('job-search-resultsstyle__LoadMoreContainer-sc-1wpt60k-1')
            except:
                print('Attribute Error to find the target monster home page')
            i = 0
            while i < self.numberOfJobs:

                actions = ActionChains(browser)
                actions.move_to_element(target)
                actions.perform()
                time.sleep(3)
                i += 10

            pageSource = browser.page_source

            browser.close()

            soup = BeautifulSoup(pageSource, 'lxml')
            try:
                jobCards = soup.find_all('article', 'job-cardstyle__JobCardComponent-sc-1mbmxes-0')
            except:
                print('Attribute error, Job Cards missing Moster Home Page')
            j += 1

        if jobCards is None or len(jobCards) == 0:
            return

        return self.processMonsterLinks(jobCards)
        




