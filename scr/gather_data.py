from loguru import logger

from scr.utils import load_graph_safely

GET_ONTOUML_TYPES_OCCURRENCES = """
PREFIX ontouml: <https://w3id.org/ontouml#>
SELECT ?type (COUNT(DISTINCT ?individual) AS ?individual_count)
WHERE {
  ?individual a ?type .
  FILTER(STRSTARTS(STR(?type), STR(ontouml:)))
}
GROUP BY ?type
"""


def get_data(model, model_stats, data_file):
    logger.info(f"Collecting data from model {model}.")

    data_graph = load_graph_safely(data_file)
    query_answer = data_graph.query(GET_ONTOUML_TYPES_OCCURRENCES)

    for row in query_answer:
        ontouml_type = (row.type).fragment
        ontouml_type_count = (row.individual_count).toPython()

        if hasattr(model_stats, ontouml_type):
            setattr(model_stats, ontouml_type, ontouml_type_count)
        else:
            raise ValueError(f"Invalid OntoUML type {ontouml_type} found!")
