# from asyncio.windows_events import NULL
from concurrent.futures import process
from typing import Union, Any

from ProcessIndeed import Indeed
from ProcessLinkedIn import LinkedIn
from writeCSV import CSVWriter
from processMonster import Monster

import concurrent.futures

def main(): 

    position = input("What position are you looking for ? ")
    location = input("what is your preferred location ? ")
    csvName = 'allJobs.csv'

    CSVWriter.initializeRowHeader(csvName)

    allJobs = []
    allJobsIndeed = []
    allJobsLinkedIn = []
    allJobsMonster = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # allJobsIndeed = executor.submit(indeed_thread, position, location )
        # allJobsLinkedIn = executor.submit(linkedin_thread, position, location)
        allJobsMonster = executor.submit(monster_thread, position, location)

    # print(allJobsIndeed.result())
    # allJobs.extend(allJobsIndeed.result())
    # allJobs.extend(allJobsLinkedIn.result())
    allJobs.extend(allJobsMonster.result())
    CSVWriter.writeToCsv(allJobs, csvName)

def monster_thread(position, location):
    monster = Monster(position, location)
    return monster.process()

def indeed_thread(position, location):
    indeed = Indeed(position, location)
    return indeed.process()

def linkedin_thread(position, location):
    linkedIn = LinkedIn(position, location)
    return linkedIn.process()

if __name__ == "__main__":
    main()
