import csv

class CSVWriter:

    def __init__(self) -> None:
        pass

    def initializeRowHeader(nameCsv):

        with open(nameCsv, 'w', newline='', encoding='utf-8') as csvF:
            csv_writer = csv.writer(csvF)
            csv_writer.writerow(['ID', 'Job Title', 'Company',
                                'Job Page link', 'Job Description', 'Source'])


    def writeToCsv( jobs, nameCsv):
        with open(nameCsv, 'a', newline='', encoding='utf-8') as csvF:
            csv_writer = csv.writer(csvF)

            id = 1
            for job in jobs:

                if job.link:
                    csv_writer.writerow(
                        [jobs.index(job) + 1, job.jobTitle, job.company, job.link, job.jobDescription, job.source])
                id += 1