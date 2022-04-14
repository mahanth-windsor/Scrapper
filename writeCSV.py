import csv

class CSVWriter:

    def __init__(self) -> None:
        pass

    def writeToCsv( jobs, nameCsv):
        with open(nameCsv, 'w', newline='', encoding='utf-8') as csvF:
            csv_writer = csv.writer(csvF)
            csv_writer.writerow(['ID', 'Job Title', 'Company',
                                'Job Page link', 'Job Description'])

            id = 1
            for job in jobs:

                if job.link:
                    csv_writer.writerow(
                        [jobs.index(job) + 1, job.jobTitle, job.company, job.link, job.jobDescription])
                id += 1