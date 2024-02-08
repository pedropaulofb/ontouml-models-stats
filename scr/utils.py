import os
import glob

from rdflib import Graph


def get_project_root_dir():
    # Get the absolute path of the current script
    script_path = os.path.abspath(__file__)

    # Get the parent directory of the current script
    parent_dir = os.path.dirname(script_path)

    # Get the root directory of the project
    project_root_dir = os.path.dirname(parent_dir)

    return project_root_dir

def get_catalog_models_path():
    # Get the absolute path of the current script
    script_path = os.path.abspath(__file__)

    # Get the parent directory of the current script
    parent_dir = os.path.dirname(script_path)

    # Get the root directory of the project
    project_root_dir = os.path.dirname(parent_dir)

    # Get the directory one level up from the project's root directory
    root_dir = os.path.dirname(project_root_dir)

    # Construct the path to the 'models' directory in 'another_project'
    models_dir = os.path.join(root_dir, 'ontouml-models', 'models')

    return models_dir

def get_models_paths():
    # Get the absolute path of the current script
    script_path = os.path.abspath(__file__)

    # Get the parent directory of the current script
    parent_dir = os.path.dirname(script_path)

    # Get the root directory of the project
    project_root_dir = os.path.dirname(parent_dir)

    # Get the directory one level up from the project's root directory
    root_dir = os.path.dirname(project_root_dir)

    # Construct the path to the 'models' directory in 'another_project'
    models_dir = os.path.join(root_dir, 'ontouml-models', 'models')

    # Use a glob pattern to get all subfolders in the given directory
    models_paths = glob.glob(os.path.join(models_dir, '*'), recursive=False)

    # Filter out any files, leaving only directories
    models_paths = [path for path in models_paths if os.path.isdir(path)]

    return models_paths

def get_models_names(directory):
    # Use a glob pattern to get all subfolders in the given directory
    models_paths = glob.glob(os.path.join(directory, '*'), recursive=False)

    # Filter out any files, leaving only directories
    models_paths = [path for path in models_paths if os.path.isdir(path)]

    # Get only the subfolder names
    models_names = [os.path.basename(path) for path in models_paths]

    return models_names

def load_graph_safely(ontology_file: str, out_format: str = "not_provided") -> Graph:
    """Safely load graph from file to working memory using arguments provided by the user, which are the file path \
    and (optionally) the file type.

    :param ontology_file: Path to the ontology file to be loaded into the working memory.
    :type ontology_file: str
    :param out_format: Optional argument. Format of the file to be loaded.
    :type out_format: str
    :return: RDFLib graph loaded as object.
    :rtype: Graph
    """
    ontology_graph = Graph()

    try:
        if out_format == "not_provided":
            ontology_graph.parse(ontology_file, encoding="utf-8")
        else:
            ontology_graph.parse(ontology_file, encoding="utf-8", format=out_format)
    except OSError as error:
        raise OSError(error)

    return ontology_graph


def update_counter(counter_dict, key):
    """Update the count for a given key in a dictionary.

    Parameters:
    - counter_dict: Dict, the dictionary to update.
    - key: The key for which to update the count.

    Returns:
    None; the input dictionary is modified in place.
    """
    if key in counter_dict:
        # If the key exists, increment its value
        counter_dict[key] += 1
    else:
        # If the key does not exist, create it with an initial value of 1
        counter_dict[key] = 1

def update_pair_counter(pair_counter, key1, key2):
    """
    Update the count for a given pair of keys in a nested dictionary.

    Parameters:
    - pair_counter: Dict, the nested dictionary to update.
    - key1: The first key of the pair.
    - key2: The second key of the pair.

    Returns:
    None; the input nested dictionary is modified in place.
    """
    if key1 not in pair_counter:
        # If the first key does not exist, create it with a nested dictionary
        pair_counter[key1] = {key2: 1}
    else:
        # If the first key exists, check for the second key
        if key2 in pair_counter[key1]:
            # If the second key exists, increment its value
            pair_counter[key1][key2] += 1
        else:
            # If the second key does not exist, create it with an initial value of 1
            pair_counter[key1][key2] = 1

