# This Python application loads in data from two JSON datasets from the UN peacekeeping website.
# It transforms the data using Pandas
# This application, when run, executes every 4 hours to update the data
# Website for reference: https://psdata.un.org/
# API reference: https://psdata.un.org/howto/api_structure
# TODO: Add cron job
# TODO: Add visualization
# TODO: Add additional classifications for more information
# TODO: Integrate with cloud computing services, e.g. Dataverse

from io import UnsupportedOperation
import requests
import pandas as pd

base_uri = "https://api.psdata.un.org/public"

def main():
    get_datasets()

def get_datasets():
    peacekeeping_funds_projects_dataset_id = "DPPA-PBFPROJECTS" # https://psdata.un.org/dataset/DPPA-PBFPROJECTS
    peacekeeping_funds_outputs_dataset_id = "DPPA-PBFOUTCOMES" # https://psdata.un.org/dataset/DPPA-PBFOUTCOMES

    funds_projects_data = get_data(peacekeeping_funds_projects_dataset_id)

    funds_outputs_data = get_data(peacekeeping_funds_outputs_dataset_id)

    joined_data = merge_data_on_project_id(funds_projects_data, funds_outputs_data)

def get_data(dataset_id):
    full_api_path = base_uri + "/data/{0}/json"

    print("Retrieving json data for dataset " + dataset_id)
    result = requests.get(full_api_path.format(dataset_id))
    print(result.status_code)

    return result.json()

def merge_data_on_project_id(funds_projects_data, funds_data):

    # TODO: Merge the dataframes together
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html
    funds_projects_dataframe = pd.DataFrame(funds_projects_data)
    funds_outputs_dataframe = pd.DataFrame(funds_data)

    print(funds_projects_dataframe.info())
    print(funds_outputs_dataframe.info{})

    merged_dataframe = pd.merge(funds_projects_dataframe, funds_outputs_dataframe, left_on="project_id", right_on="project_id")

    print(merged_dataframe)

if __name__ == "__main__":
    main()