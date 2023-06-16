import requests
import json

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

    print(resp.status_code)

    result = resp.json()

    final_res = json.dumps(result, indent=2)

    return final_res

print(query_jobs("data engineer", 30))