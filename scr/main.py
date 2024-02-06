import csv
import os

from icecream import ic
from loguru import logger

from scr.gather_data import get_data
from scr.stats import Stats
from scr.utils import get_models_names, get_catalog_models_path, get_project_root_dir


def get_metadata(metadata_file):
    pass


def get_statistics(models, models_stats_list):
    project_root_dir = get_project_root_dir()

    limit = 5
    value = 0

    for model in models:
        model_stats = Stats(model=model)

        data_file = os.path.join(project_root_dir, 'models', model, "ontology.ttl")
        get_data(model, model_stats, data_file)

        metadata_file = os.path.join(project_root_dir, 'models', model, "metadata.ttl")
        get_metadata(metadata_file)

        models_stats_list.append(model_stats)

        # value += 1
        # if value == limit:
        #     break



def create_output_csv(models_stats):
    with open('output.csv', 'w', newline='') as csvfile:
        fieldnames = [attr for attr in vars(models_stats[0])]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for obj in models_stats:
            writer.writerow(vars(obj))


if __name__ == "__main__":
    original_models_path = get_catalog_models_path()
    models = get_models_names(original_models_path)
    models_stats: list[Stats] = []
    get_statistics(models, models_stats)
    create_output_csv(models_stats)
    logger.success("Execution completed!")
