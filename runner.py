import csv
import subprocess
# Read the csv file 

CSV_FILE = "projects.csv"


def main():
    with open(CSV_FILE) as projects_file:
        projects = csv.DictReader(projects_file)
        for project in projects:
            process = create_repository(project)
            subprocess.run(process, check=True)




# Call the process
# gh repo create "scrapians/Facebook Posts Scraper" --private --description "Scrapes the Public facebook posts"
def create_repository(details):
    organization = details.get('organization',False)
    repository_name = details.get('respository_name')
    visibility = details.get('visibility','--private')
    description = details.get('description',repository_name)
    if organization:
        repository_name = f'{organization}/{repository_name}'

    if not visibility.startswith('--'):
        visibility = '--'+visibility
    
    process = ['gh','repo', 'create', repository_name,visibility,'--description', description]
    return process

if __name__ == '__main__':
    print("Main file started")
    main()


