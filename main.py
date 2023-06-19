import requests
import json
import argparse

DATA_PATH = "data/"

def query_jobs(jobs, limit = 60):
    query = "query searchJobs($data: JobSearchConditionInput!) {  searchJobs(data: $data) {    jobsInPage {      id      title      isRemote      status      createdAt      updatedAt      isActivelyHiring      isHot      shouldShowSalary      salaryEstimate {        minAmount        maxAmount        CurrencyCode        __typename      }      company {        ...CompanyFields        __typename      }      citySubDivision {        id        name        __typename      }      city {        ...CityFields        __typename      }      country {        ...CountryFields        __typename      }      category {        id        name        __typename      }      salaries {        ...SalaryFields        __typename      }      location {        ...LocationFields        __typename      }      minYearsOfExperience      maxYearsOfExperience      source      hierarchicalJobCategory {        id        level        name        children {          name          level          id          __typename        }        parents {          id          level          name          __typename        }        __typename      }      skills {        skill {          id          name          __typename        }        mustHave        __typename      }      __typename    }    totalJobs    __typename  }}fragment CompanyFields on Company {  id  name  logo  __typename}fragment CityFields on City {  id  name  __typename}fragment CountryFields on Country {  code  name  __typename}fragment SalaryFields on JobSalary {  id  salaryType  salaryMode  maxAmount  minAmount  CurrencyCode  __typename}fragment LocationFields on HierarchicalLocation {  id  name  administrativeLevelName  formattedName  level  parents {    id    name    administrativeLevelName    formattedName    level    __typename  }  __typename}"

    query_data = {
            "SearchTerm": jobs,
            "CountryCode": "ID",
            "limit": limit,
            "offset": 0,
            "includeExternalJobs": True,
            "sources": [
                "NATIVE",
                "SUPER_POWERED"
            ],
            "searchVariant": "CURRENT"
    }

    data_dict = {
        "operationName": "searchJobs",
        "query": query,
        "variables": {
            "data": query_data
        }
    }

    resp = requests.post(url = "https://glints.com/api/graphql",
                        json = data_dict)

    print(f"Status code: {resp.status_code}")

    result = resp.json()

    return result

def save_json_data(json_data, filename):
    print("Start process...")

    with open(DATA_PATH + filename, 'w', encoding = "utf-8") as f:
        json.dump(json_data, f, indent = 4)

    print("End process...")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()

    parser.add_argument("--jobs",
                        type=str,
                        help="Insert jobs name",
                        required=True)
    
    parser.add_argument("--filename",
                        type=str,
                        help="Insert json filename to save file",
                        required=True)

    args = parser.parse_args()

    print("===== START SCRAPING DATA =====")

    # 1. Input jobs name and limit (optional)
    json_data = query_jobs(args.jobs,
                           limit = 100)

    # 2. Save data into json file
    save_json_data(json_data = json_data,
                   filename = args.filename)
    
    print("===== END SCRAPING DATA =====")


