import requests
import bs4
import json

BASE_URL = 'https://www.timesjobs.com/candidate/job-search.html?' \
        'searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
FILE_NAME = 'job.html'

    
class Web:
    # initializing the class members
    def __init__(self, url: str, filename: str) -> None:
        self.list_of_data = []
        self.url = url
        self.filename = filename
        self.response = requests.get(self.url)  # Object
        self.soup = bs4.BeautifulSoup(self.response.text, "html.parser")

    # ----------------------------------------------------------------------

    # Saving the parsed Website code in Local File
    def save_code(self) -> None:
        formatted_text = self.soup.prettify()
        with open(self.filename, "w", encoding="utf-8") as file:
            file.write(formatted_text)

    # ----------------------------------------------------------------------

    #   Extracting The webpage Code ,Parsing and saving the Http request data in a Local file
    def website_scraping(self) -> None:
        print("Put some skill that you are familiar with ")
        familiar_skill = input('> ')
        print(f'Filtering out {familiar_skill}')

        jobs = self.soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        count = 0

        for index, job in enumerate(jobs):
            job_published_date = job.find('span', class_='sim-posted').get_text()

            if 'few' in job_published_date:
                company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
                skills_required = job.find('span', class_='srp-skills').text.replace(' ', '')
                more_info = job.header.h2.a['href']

                if familiar_skill in skills_required:
                    count += 1
                    
                    data = {
                        'Job Post Number': index, 'Company Name': company_name.strip(),
                        'Required Skills': skills_required.strip(),
                        'Published Date': job_published_date.strip(),
                        'More_info': more_info
                            }
                    self.list_of_data.append(data)

        with open(f'Job_Posts/vacancies_list.json', 'w') as file:
            json.dump(self.list_of_data, file, indent=4)

        print(f'{count} New Jobs Saved In : Job_Posts/vacancies_list.json')

    # ----------------------------------------------------------------------


def main() -> None:
    while True:
        w = Web(BASE_URL, FILE_NAME)
        w.save_code()
        w.website_scraping()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Exception", e.message)
