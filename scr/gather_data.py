from icecream import ic
from loguru import logger
from rdflib.plugins.sparql import prepareQuery

from scr.constants import ONTOUML_BOOLEAN_DATA_PROPERTIES, ONTOUML_CLASS_STEREOTYPES, ONTOUML_RELATION_STEREOTYPES, \
    ONTOUML_CLASS_NATURE, ONTOUML_PROPERTY_STEREOTYPES, ONTOUML_AGGREGATION_KIND
from scr.sparql_queries import SPARQL_ONTOUML_TYPES_OCCURRENCES, SPARQL_BOOLEAN_DATA_PROPERTIES, \
    SPARQL_OBJECT_PROPERTY_QUERY, SPARQL_GENERALIZATION_STEREOTYPES, \
    SPARQL_CLASS_ST_ON, SPARQL_OBJECT_PROPERTY_QUERY2
from scr.utils import load_graph_safely


def query_instances_vocab_classes(data_graph, model_stats):
    query_answer = data_graph.query(SPARQL_ONTOUML_TYPES_OCCURRENCES)

    for row in query_answer:
        ontouml_type = (row.type).fragment
        ontouml_type_count = (row.individual_count).toPython()

        if hasattr(model_stats, ontouml_type):
            setattr(model_stats, ontouml_type, ontouml_type_count)
        else:
            raise ValueError(f"Invalid OntoUML type {ontouml_type} found!")


def query_boolean_data_properties(data_graph, model_stats):
    for ontouml_type, properties in ONTOUML_BOOLEAN_DATA_PROPERTIES.items():
        for property in properties:

            sparql_query = SPARQL_BOOLEAN_DATA_PROPERTIES.format(ontouml_type=ontouml_type, ontouml_property=property)
            prepared_query = prepareQuery(sparql_query)
            query_answer = data_graph.query(prepared_query)

            for row in query_answer:
                ontouml_property_count_true = (row.count_true).toPython()
                ontouml_property_count_false = (row.count_false).toPython()

                register_true = f"{ontouml_type}_{property}_True"
                if hasattr(model_stats, register_true):
                    setattr(model_stats, register_true, ontouml_property_count_true)
                else:
                    raise ValueError(f"Invalid OntoUML {register_true} found!")

                register_false = f"{ontouml_type}_{property}_False"
                if hasattr(model_stats, register_false):
                    setattr(model_stats, register_false, ontouml_property_count_false)
                else:
                    raise ValueError(f"Invalid OntoUML {register_false} found!")


def query_class_stereotypes(data_graph, model_stats):
    total = 0
    sparql_query = SPARQL_OBJECT_PROPERTY_QUERY2.format(ou_class="Class", ou_oprop="stereotype")
    prepared_query = prepareQuery(sparql_query)
    query_answer = data_graph.query(prepared_query)

    for row in query_answer:
        result = (row.result).fragment
        ontouml_count = (row.individual_count).toPython()
        column = f"Class_St_{result}"
        total += ontouml_count
        if hasattr(model_stats, column):
            setattr(model_stats, column, ontouml_count)
        else:
            model_stats.Class_St_others += ontouml_count

    model_stats.Class_St_none = model_stats.Class - total

def query_relation_stereotypes(data_graph, model_stats):
    # TODO: TO BE UPDATED
    total_st = 0
    for relation_st in ONTOUML_RELATION_STEREOTYPES:
        sparql_query = SPARQL_OBJECT_PROPERTY_QUERY.format(ou_class="Relation", ou_oprop="stereotype",
                                                           ou_ind=relation_st)
        prepared_query = prepareQuery(sparql_query)
        query_answer = data_graph.query(prepared_query)

        for row in query_answer:
            ontouml_count = (row.individual_count).toPython()
            column = f"Relation_St_{relation_st}"
            if hasattr(model_stats, column):
                setattr(model_stats, column, ontouml_count)
            else:
                raise ValueError(f"Invalid OntoUML {column} found!")
        total_st += ontouml_count

    model_stats.Relation_St_others = model_stats.Relation - total_st


def query_property_stereotypes(data_graph, model_stats):
    # TODO: TO BE UPDATED
    total_st = 0
    for property_st in ONTOUML_PROPERTY_STEREOTYPES:
        sparql_query = SPARQL_OBJECT_PROPERTY_QUERY.format(ou_class="Property", ou_oprop="stereotype",
                                                           ou_ind=property_st)
        prepared_query = prepareQuery(sparql_query)
        query_answer = data_graph.query(prepared_query)

        for row in query_answer:
            ontouml_count = (row.individual_count).toPython()
            column = f"Property_St_{property_st}"
            if hasattr(model_stats, column):
                setattr(model_stats, column, ontouml_count)
            else:
                raise ValueError(f"Invalid OntoUML {column} found!")
        total_st += ontouml_count

    model_stats.Property_St_others = model_stats.Property - total_st


def query_class_ontological_nature(data_graph, model_stats):
    # TODO: TO BE UPDATED
    for class_on in ONTOUML_CLASS_NATURE:
        sparql_query = SPARQL_OBJECT_PROPERTY_QUERY.format(ou_class="Class", ou_oprop="restrictedTo", ou_ind=class_on)
        prepared_query = prepareQuery(sparql_query)
        query_answer = data_graph.query(prepared_query)

        for row in query_answer:
            ontouml_count = (row.individual_count).toPython()
            column = f"Class_ON_{class_on}"
            if hasattr(model_stats, column):
                setattr(model_stats, column, ontouml_count)
            else:
                raise ValueError(f"Invalid OntoUML {column} found!")


def query_property_aggregation_kind(data_graph, model_stats):
    # TODO: TO BE UPDATED
    total_ak = 0
    for property_ak in ONTOUML_AGGREGATION_KIND:
        sparql_query = SPARQL_OBJECT_PROPERTY_QUERY.format(ou_class="Property", ou_oprop="aggregationKind",
                                                           ou_ind=property_ak)
        prepared_query = prepareQuery(sparql_query)
        query_answer = data_graph.query(prepared_query)

        for row in query_answer:
            ontouml_count = (row.individual_count).toPython()
            column = f"Property_AK_{property_ak}"
            if hasattr(model_stats, column):
                setattr(model_stats, column, ontouml_count)
            else:
                raise ValueError(f"Invalid OntoUML {column} found!")
        total_ak += ontouml_count

    model_stats.Property_AK_others = model_stats.Property - total_ak


def query_class_stereotype_ontological_nature(data_graph, model_stats):
    query_answer = data_graph.query(SPARQL_CLASS_ST_ON)

    for row in query_answer:
        stereotype = row.stereotype.fragment
        ontological_nature = row.ontological_nature.fragment
        ontouml_count = row.individual_count.toPython()

        column = f"Class_St-ON_{stereotype}_{ontological_nature}"
        if hasattr(model_stats, column):
            setattr(model_stats, column, ontouml_count)


def query_generalization_stereotypes(data_graph, model_stats):
    query_answer = data_graph.query(SPARQL_GENERALIZATION_STEREOTYPES)

    for row in query_answer:
        st_s = row.stereotypeA.fragment
        st_g = row.stereotypeB.fragment
        ontouml_count = (row.individual_count).toPython()
        column = f"Generalization_{st_s}_{st_g}"
        if hasattr(model_stats, column):
            setattr(model_stats, column, ontouml_count)
        else:
            raise ValueError(f"Invalid OntoUML {column} found!")


def get_data(model, model_stats, data_file):
    logger.info(f"Collecting data from model {model}.")

    data_graph = load_graph_safely(data_file)

    query_instances_vocab_classes(data_graph, model_stats)
    query_class_stereotypes(data_graph, model_stats)
    # query_class_ontological_nature(data_graph, model_stats)
    # query_relation_stereotypes(data_graph, model_stats)
    # query_property_stereotypes(data_graph, model_stats)
    # query_property_aggregation_kind(data_graph, model_stats)
    # query_boolean_data_properties(data_graph, model_stats)
    # query_class_stereotype_ontological_nature(data_graph,model_stats)
    # query_generalization_stereotypes(data_graph, model_stats)

    # C1 R C2 - get C1/R, R/C2, and C1/C2 (Do this for R = Relation and for R = Generalization)
    # Evaluate case stereotype is NONE (different from not listed)
    # Evaluate existing stereotypes (Class, Relation, etc.) that are not valid.
    # Classes may have more than one Ontological Nature. Verify the occurring combinations.
    # Verify classes that have value restrictedTo not listed as instance of OntologicalNature (current not being done).
    # Boolean data properties per stereotype (e.g., how many Kinds are Abstract?).
    # How to deal with cardinality values, order values?  # Number of taxonomies, min, max, average, etc.
    # Number of GeneralizationSets, min, max, average, etc.
