# from asyncio.windows_events import NULL
from concurrent.futures import process
from typing import Union, Any

from ProcessIndeed import Indeed
from ProcessLinkedIn import LinkedIn
from writeCSV import CSVWriter

def main(): 

    CSVWriter.initializeRowHeader('All_Jobs.csv')

    indeed = Indeed()
    indeed.startCrawling()

    linkedIn = LinkedIn()
    linkedIn.process()

if __name__ == "__main__":
    main()
