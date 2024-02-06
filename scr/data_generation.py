import os
import shutil

from json2graph.library import save_graph_file, decode_json_project
from loguru import logger

from scr.utils import get_project_root_dir


def create_files(original_models_path, models):
    project_root_dir = get_project_root_dir()
    for model in models:
        # Construct the path to the new folder in your project
        new_folder_path = os.path.join(project_root_dir, 'models', model)

        # Create the new folder
        os.makedirs(new_folder_path, exist_ok=True)

        # Construct the path to the 'metadata.yaml' file in the source and destination directories
        metadata_file_source = os.path.join(original_models_path, model, 'metadata.ttl')
        metadata_file_dest = os.path.join(new_folder_path, 'metadata.ttl')

        # Copy the 'metadata.ttl' file to the new folder
        shutil.copy(metadata_file_source, metadata_file_dest)

        # Construct the path to the 'ontology.json' file in the source and destination directories
        json_file_source = os.path.join(original_models_path, model, 'ontology.json')
        ttl_file_dest = os.path.join(new_folder_path, 'ontology.ttl')

        # Using ontouml-json2graph to create the corresponding ttl files
        decoded_graph_model = decode_json_project(json_file_path=json_file_source, correct=False)
        save_graph_file(decoded_graph_model, ttl_file_dest, "ttl")

        logger.success(f"Data successfully generated to model {model}!")
