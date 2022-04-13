# from asyncio.windows_events import NULL
from concurrent.futures import process
from typing import Union, Any

from bs4 import BeautifulSoup
import requests
import csv

from src.JobDetails import JobDetails

jobsList = []
ids = 0
def processHomePage(job_page_links):
    with open('pageLinks.csv', 'a', newline='', encoding='utf-8') as csvF:
        csv_writer = csv.writer(csvF)
        # csv_writer.writerow(['Job Title', 'Company', 'Job Page link', 'Job Description' ])
        for link in job_page_links:
            # print(link)
            jobPageSource = requests.get(link).text

            soup = BeautifulSoup(jobPageSource, 'lxml')

            mainDivJobPageDescription = soup.find('div', class_='jobsearch-JobComponent-description').text

            jobTitle = soup.find('div', class_='jobsearch-JobInfoHeader-title-container').h1.text

            company = ''

            if (soup.find('div', class_='jobsearch-CompanyInfoContainer') is not None and
                    soup.find('div', class_='jobsearch-CompanyInfoContainer').a is not None and
                      soup.find('div', class_='jobsearch-CompanyInfoContainer').a.string is not None ):
                company = soup.find('div', class_='jobsearch-CompanyInfoContainer').a.string

            if link:
                csv_writer.writerow([len(jobsList)+1, jobTitle, company, link, mainDivJobPageDescription])

            job = JobDetails(jobTitle, company, link, mainDivJobPageDescription)
            jobsList.append(job)
            # print(job.jobTitle)
    print(len(jobsList))
    return jobsList


def processSoup(source):
    soup = BeautifulSoup(source, 'lxml')

    # a list to store the job links 
    job_page_links = []

    # this gets the main div that lists all the jobs 
    div_list = soup.find('div', id='mosaic-provider-jobcards')

    contents = div_list.find_all('a', class_='tapItem')

    for content in contents:

        base_link = "https://ca.indeed.com"
        link = base_link + content['href']

        if link:
            # csv_writer.writerow([link, mainDivJobPage])
            job_page_links.append(link)

    # this opens the out put file
    with open('outputs1.txt', 'a') as f:

        # this get the all  the anchors in the main div that have the class tapItem. 
        # others anchors link to company pages, reviews etc. 

        # for content in contents:
        #     link = content['href']
        #     f.write(link)
        #     f.write('\n')
        #     f.write('\n')
        #     job_page_links.append(link)
        pass

    processHomePage(job_page_links)
    print(len(jobsList))
    return jobsList

    # with open('test.csv', 'r') as readCsv:
    #     csvReader = csv.reader(readCsv)


def startCrawling():
    pagenationsLinks = ['https://ca.indeed.com/jobs?q=&l=Ontario',
                        'https://ca.indeed.com/jobs?l=Ontario&start=20',
                        'https://ca.indeed.com/jobs?l=Ontario&start=30',
                        'https://ca.indeed.com/jobs?l=Ontario&start=40',
                        'https://ca.indeed.com/jobs?l=Ontario&start=50'

                        ]
    with open('pageLinks.csv', 'w', newline='', encoding='utf-8') as csvF:
        csv_writer = csv.writer(csvF)
        csv_writer.writerow(['ID', 'Job Title', 'Company', 'Job Page link', 'Job Description'])
        # with open('outputs1.txt', 'w') as csvF:
        #     csv_writer = csv.writer(csvF)
        #     csv_writer.writerow(['links'])
        for sourceUrl in pagenationsLinks:
            source = requests.get(sourceUrl).text
            processSoup(source)
    print(jobsList[0].jobTitle)
    return jobsList


def main():
    print(startCrawling())


if __name__ == "__main__":
    main()
