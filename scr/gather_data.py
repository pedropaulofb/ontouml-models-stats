from icecream import ic
from loguru import logger
from rdflib import URIRef
from rdflib.plugins.sparql import prepareQuery

from scr.constants import ONTOUML_BOOLEAN_DATA_PROPERTIES, ONTOUML_CLASS_STEREOTYPES
from scr.sparql_queries import SPARQL_ONTOUML_TYPES_OCCURRENCES, SPARQL_CLASS_ST_ON, \
    SPARQL_BOOLEAN_DATA_PROPERTIES, SPARQL_OBJECT_PROPERTY_QUERY, SPARQL_ALL_STEREOTYPES_ABOVE, \
    SPARQL_GENERALIZATION_ONLY_GENERAL_STEREOTYPE, SPARQL_STEREOTYPE_NOT_IN_GENERALIZATION, \
    SPARQL_GENERALIZATION_BOTH_SPECIFIC_GENERAL_STEREOTYPE
from scr.utils import load_graph_safely, update_pair_counter
from scr.utils_graph import get_all_classes, get_direct_superclasses, get_class_stereotype, get_all_superclasses


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

                register_true = f"{ontouml_type}_{property}_True"
                if hasattr(model_stats, register_true):
                    setattr(model_stats, register_true, ontouml_property_count_true)

                ontouml_property_count_false = getattr(model_stats, ontouml_type) - ontouml_property_count_true
                register_false = f"{ontouml_type}_{property}_False"
                if hasattr(model_stats, register_false):
                    setattr(model_stats, register_false, ontouml_property_count_false)


def query_class_stereotypes(data_graph, model_stats):
    total = 0
    sparql_query = SPARQL_OBJECT_PROPERTY_QUERY.format(ou_class="Class", ou_oprop="stereotype")
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
    total = 0
    sparql_query = SPARQL_OBJECT_PROPERTY_QUERY.format(ou_class="Relation", ou_oprop="stereotype")
    prepared_query = prepareQuery(sparql_query)
    query_answer = data_graph.query(prepared_query)

    for row in query_answer:
        result = (row.result).fragment
        ontouml_count = (row.individual_count).toPython()
        column = f"Relation_St_{result}"
        total += ontouml_count
        if hasattr(model_stats, column):
            setattr(model_stats, column, ontouml_count)
        else:
            model_stats.Relation_St_others += ontouml_count

    model_stats.Relation_St_none = model_stats.Relation - total


def query_property_stereotypes(data_graph, model_stats):
    total = 0
    sparql_query = SPARQL_OBJECT_PROPERTY_QUERY.format(ou_class="Property", ou_oprop="stereotype")
    prepared_query = prepareQuery(sparql_query)
    query_answer = data_graph.query(prepared_query)

    for row in query_answer:
        result = (row.result).fragment
        ontouml_count = (row.individual_count).toPython()
        column = f"Property_St_{result}"
        total += ontouml_count
        if hasattr(model_stats, column):
            setattr(model_stats, column, ontouml_count)
        else:
            model_stats.Property_St_others += ontouml_count

    model_stats.Property_St_none = model_stats.Property - total


def query_class_ontological_nature(data_graph, model_stats):
    total = 0
    sparql_query = SPARQL_OBJECT_PROPERTY_QUERY.format(ou_class="Class", ou_oprop="restrictedTo")
    prepared_query = prepareQuery(sparql_query)
    query_answer = data_graph.query(prepared_query)

    for row in query_answer:
        result = (row.result).fragment
        ontouml_count = (row.individual_count).toPython()
        column = f"Class_ON_{result}"
        total += ontouml_count
        if hasattr(model_stats, column):
            setattr(model_stats, column, ontouml_count)
        else:
            model_stats.Class_ON_others += ontouml_count

    model_stats.Class_ON_none = model_stats.Class - total


def query_property_aggregation_kind(data_graph, model_stats):
    total = 0
    sparql_query = SPARQL_OBJECT_PROPERTY_QUERY.format(ou_class="Property", ou_oprop="aggregationKind")
    prepared_query = prepareQuery(sparql_query)
    query_answer = data_graph.query(prepared_query)

    for row in query_answer:
        result = (row.result).fragment
        ontouml_count = (row.individual_count).toPython()
        column = f"Property_AK_{result}"
        total += ontouml_count
        if hasattr(model_stats, column):
            setattr(model_stats, column, ontouml_count)
        else:
            model_stats.Property_AK_others += ontouml_count

    model_stats.Property_AK_none = model_stats.Property - total


def query_class_stereotype_ontological_nature(data_graph, model_stats):
    query_answer = data_graph.query(SPARQL_CLASS_ST_ON)

    for row in query_answer:
        stereotype = row.stereotype.fragment
        ontological_nature = row.ontological_nature.fragment
        ontouml_count = row.individual_count.toPython()

        column = f"Class_St-ON_{stereotype}_{ontological_nature}"
        if hasattr(model_stats, column):
            setattr(model_stats, column, ontouml_count)


def query_generalization_spec_gen_stereotypes(data_graph, model_stats):
    # Calculating SPECIFIC ONLY
    query_answer = data_graph.query(SPARQL_ALL_STEREOTYPES_ABOVE)

    for row in query_answer:
        stereotype = row.stereotype.fragment
        result = (row.individual_count).toPython()
        column = f"Generalization_only_specific_{stereotype}"
        if hasattr(model_stats, column):
            setattr(model_stats, column, result)

    # Calculating GENERAL ONLY
    query_answer = data_graph.query(SPARQL_GENERALIZATION_ONLY_GENERAL_STEREOTYPE)

    for row in query_answer:
        stereotype = row.stereotype.fragment
        result = (row.individual_count).toPython()
        column = f"Generalization_only_general_{stereotype}"
        if hasattr(model_stats, column):
            setattr(model_stats, column, result)

    # CALCULATING BOTH GENERAL AND SPECIFIC
    query_answer = data_graph.query(SPARQL_GENERALIZATION_BOTH_SPECIFIC_GENERAL_STEREOTYPE)

    for row in query_answer:
        stereotype = row.stereotype.fragment
        result = (row.result).toPython()
        column = f"Generalization_specific_general_{stereotype}"
        if hasattr(model_stats, column):
            setattr(model_stats, column, result)

    # CALCULATING NOT GENERAL AND NOT SPECIFIC
    query_answer = data_graph.query(SPARQL_STEREOTYPE_NOT_IN_GENERALIZATION)

    for row in query_answer:
        stereotype = row.stereotype.fragment
        result = (row.result).toPython()
        column = f"Generalization_none_{stereotype}"
        if hasattr(model_stats, column):
            setattr(model_stats, column, result)


def register_direct_generalization_stereotypes(data_graph, model_stats):
    counter_dict = {}

    all_classes = get_all_classes(data_graph)
    for ou_class in all_classes:
        class_stereotype = get_class_stereotype(data_graph, ou_class)
        class_stereotype = URIRef(class_stereotype).fragment if class_stereotype else "none"

        all_superclasses = get_direct_superclasses(data_graph, ou_class)
        for superclass in all_superclasses:
            superclass_stereotype = get_class_stereotype(data_graph, superclass)
            superclass_stereotype = URIRef(superclass_stereotype).fragment if superclass_stereotype else "none"
            update_pair_counter(counter_dict, class_stereotype, superclass_stereotype)

    for k1, inner_dict in counter_dict.items():
        for k2, value in inner_dict.items():

            k1f = k1 if (k1 == "none" or k1 in ONTOUML_CLASS_STEREOTYPES) else "others"
            k2f = k2 if (k2 == "none" or k2 in ONTOUML_CLASS_STEREOTYPES) else "others"

            column = f"Gen_dir_{k1f}_{k2f}"
            if hasattr(model_stats, column):
                setattr(model_stats, column, value)
            else:
                ic(k1, k2, k1f, k2f)
                raise ValueError("PROBLEM")


def register_all_generalization_stereotypes(data_graph, model_stats):
    counter_dict = {}

    all_classes = get_all_classes(data_graph)
    for ou_class in all_classes:
        class_stereotype = get_class_stereotype(data_graph, ou_class)
        class_stereotype = URIRef(class_stereotype).fragment if class_stereotype else "none"

        all_superclasses = get_all_superclasses(data_graph, ou_class)
        for superclass in all_superclasses:
            superclass_stereotype = get_class_stereotype(data_graph, superclass)
            superclass_stereotype = URIRef(superclass_stereotype).fragment if superclass_stereotype else "none"
            update_pair_counter(counter_dict, class_stereotype, superclass_stereotype)

    for k1, inner_dict in counter_dict.items():
        for k2, value in inner_dict.items():

            k1f = k1 if (k1 == "none" or k1 in ONTOUML_CLASS_STEREOTYPES) else "others"
            k2f = k2 if (k2 == "none" or k2 in ONTOUML_CLASS_STEREOTYPES) else "others"

            column = f"Gen_all_{k1f}_{k2f}"
            if hasattr(model_stats, column):
                setattr(model_stats, column, value)
            else:
                ic(k1, k2, k1f, k2f)
                raise ValueError("PROBLEM")


def get_data(model, model_stats, data_file):
    logger.info(f"Collecting data from model {model}.")

    data_graph = load_graph_safely(data_file)

    import time

    start_time = time.perf_counter()
    query_instances_vocab_classes(data_graph, model_stats)
    end_time = time.perf_counter()
    logger.info(f"query_instances_vocab_classes = {format((end_time - start_time) * 1000, ".2f")} miliseconds.")

    start_time = time.perf_counter()
    query_class_stereotypes(data_graph, model_stats)
    end_time = time.perf_counter()
    logger.info(f"query_class_stereotypes = {format((end_time - start_time) * 1000, ".2f")} miliseconds.")

    start_time = time.perf_counter()
    query_class_ontological_nature(data_graph, model_stats)
    end_time = time.perf_counter()
    logger.info(f"query_class_ontological_nature = {format((end_time - start_time) * 1000, ".2f")} miliseconds.")

    start_time = time.perf_counter()
    query_relation_stereotypes(data_graph, model_stats)
    end_time = time.perf_counter()
    logger.info(f"query_relation_stereotypes = {format((end_time - start_time) * 1000, ".2f")} miliseconds.")

    start_time = time.perf_counter()
    query_property_stereotypes(data_graph, model_stats)
    end_time = time.perf_counter()
    logger.info(f"query_property_stereotypes = {format((end_time - start_time) * 1000, ".2f")} miliseconds.")

    start_time = time.perf_counter()
    query_property_aggregation_kind(data_graph, model_stats)
    end_time = time.perf_counter()
    logger.info(f"query_property_aggregation_kind = {format((end_time - start_time) * 1000, ".2f")} miliseconds.")

    start_time = time.perf_counter()
    query_boolean_data_properties(data_graph, model_stats)
    end_time = time.perf_counter()
    logger.info(f"query_boolean_data_properties = {format((end_time - start_time) * 1000, ".2f")} miliseconds.")

    start_time = time.perf_counter()
    query_class_stereotype_ontological_nature(data_graph, model_stats)
    end_time = time.perf_counter()
    logger.info(
        f"query_class_stereotype_ontological_nature = {format((end_time - start_time) * 1000, ".2f")} miliseconds.")

    start_time = time.perf_counter()
    register_direct_generalization_stereotypes(data_graph, model_stats)
    end_time = time.perf_counter()
    logger.info(f"register_direct_generalization_stereotypes = {format((end_time - start_time) * 1000, ".2f")} miliseconds.")

    start_time = time.perf_counter()
    query_generalization_spec_gen_stereotypes(data_graph, model_stats)
    end_time = time.perf_counter()
    logger.info(
        f"query_generalization_spec_gen_stereotypes = {format((end_time - start_time) * 1000, ".2f")} miliseconds.")

    start_time = time.perf_counter()
    register_all_generalization_stereotypes(data_graph, model_stats)
    end_time = time.perf_counter()
    logger.info(
        f"register_all_generalization_stereotypes = {format((end_time - start_time) * 1000, ".2f")} miliseconds.")



    # C1 R C2 - get C1/R, R/C2, and C1/C2 (Do this for R = Relation and for R = Generalization)
        # How many times it is just specific or just generic
            # (note that if a class has, e.g., two specific just one must be counted)
        # How many times it is specific and generic
    # Stereotype of each class/relation that is abstract, derived, etc.
    # Evaluate existing stereotypes (Class, Relation, etc.) that are not valid.
    # Classes may have more than one Ontological Nature. Verify the occurring combinations.
    # Verify classes that have value restrictedTo not listed as instance of OntologicalNature (current not being done).
    # Boolean data properties per stereotype (e.g., how many Kinds are Abstract?).
    # How to deal with cardinality values, order values?  # Number of taxonomies, min, max, average, etc.
    # Number of GeneralizationSets, min, max, average, etc.