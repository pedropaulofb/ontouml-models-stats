from icecream import ic
from loguru import logger
from rdflib.plugins.sparql import prepareQuery

from scr.constants import ONTOUML_BOOLEAN_DATA_PROPERTIES
from scr.utils import load_graph_safely

SPARQL_ONTOUML_TYPES_OCCURRENCES = """
PREFIX ontouml: <https://w3id.org/ontouml#>
SELECT ?type (COUNT(DISTINCT ?individual) AS ?individual_count)
WHERE {
  ?individual a ?type .
  FILTER(STRSTARTS(STR(?type), STR(ontouml:)))
}
GROUP BY ?type
"""

SPARQL_BOOLEAN_DATA_PROPERTIES = """
PREFIX ontouml: <https://w3id.org/ontouml#>
SELECT ?property (COUNT(?individual) AS ?count_true) (COUNT(?individual2) AS ?count_false)
WHERE {{
  {{
    SELECT ?property ?individual
    WHERE {{
      ?individual a ontouml:{ontouml_type} ;
                  ?property true .
      FILTER (?property = ontouml:{ontouml_property})
    }}
  }}
  UNION
  {{
    SELECT ?property ?individual2
    WHERE {{
      ?individual2 a ontouml:{ontouml_type} ;
                   ?property false .
      FILTER (?property = ontouml:{ontouml_property})
    }}
  }}
}}
GROUP BY ?property
"""


def get_data(model, model_stats, data_file):
    logger.info(f"Collecting data from model {model}.")

    data_graph = load_graph_safely(data_file)

    # QUERY SPARQL_ONTOUML_TYPES_OCCURRENCES
    query_answer = data_graph.query(SPARQL_ONTOUML_TYPES_OCCURRENCES)

    for row in query_answer:
        ontouml_type = (row.type).fragment
        ontouml_type_count = (row.individual_count).toPython()

        if hasattr(model_stats, ontouml_type):
            setattr(model_stats, ontouml_type, ontouml_type_count)
        else:
            raise ValueError(f"Invalid OntoUML type {ontouml_type} found!")


    #
    for ontouml_type, properties in ONTOUML_BOOLEAN_DATA_PROPERTIES.items():
        for property in properties:
            sparql_query = SPARQL_BOOLEAN_DATA_PROPERTIES.format(ontouml_type=ontouml_type, ontouml_property=property)
            prepared_query = prepareQuery(sparql_query)
            query_answer = data_graph.query(prepared_query)

            for row in query_answer:
                ontouml_property = (row.property).fragment
                ontouml_property_count_true = (row.count_true).toPython()
                ontouml_property_count_false = (row.count_false).toPython()

                register_true = f"{ontouml_type}_{property}_True"
                if hasattr(model_stats, register_true):
                    setattr(model_stats, register_true, ontouml_property_count_true)
                else:
                    raise ValueError(f"Invalid OntoUML type {register_true} found!")

                register_false = f"{ontouml_type}_{property}_False"
                if hasattr(model_stats, register_false):
                    setattr(model_stats, register_false, ontouml_property_count_false)
                else:
                    raise ValueError(f"Invalid OntoUML type {register_false} found!")