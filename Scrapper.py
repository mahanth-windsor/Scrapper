# from asyncio.windows_events import NULL
from concurrent.futures import process
from typing import Union, Any

from ProcessIndeed import Indeed
from ProcessLinkedIn import LinkedIn
from writeCSV import CSVWriter

def main(): 

    position = input("What position are you looking for ? ")
    location = input("what is your preferred location ? ")
    csvName = 'allJobs.csv'

    CSVWriter.initializeRowHeader(csvName)

    allJobs = []

    # indeed = Indeed(position, location, csvName)
    # allJobs.extend(indeed.process())

    linkedIn = LinkedIn(position, location, csvName)
    allJobs.extend(linkedIn.process())

    CSVWriter.writeToCsv(allJobs, csvName)


if __name__ == "__main__":
    main()
