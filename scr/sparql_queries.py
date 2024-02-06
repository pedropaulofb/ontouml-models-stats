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

SPARQL_OBJECT_PROPERTY_QUERY = """
PREFIX ontouml: <https://w3id.org/ontouml#>
SELECT (COUNT(DISTINCT ?individual) AS ?individual_count)
WHERE {{
  ?individual a ontouml:{ou_class} ;
              ontouml:{ou_oprop} ontouml:{ou_ind} .
}}
"""

SPARQL_OBJECT_PROPERTY_QUERY2 = """
PREFIX ontouml: <https://w3id.org/ontouml#>
SELECT ?result (COUNT(DISTINCT ?individual) AS ?individual_count)
WHERE {{
  ?individual a ontouml:{ou_class} ;
              ontouml:{ou_oprop} ?result .
}}
GROUP BY ?result
"""

SPARQL_CLASS_ST_ON = """
PREFIX ontouml: <https://w3id.org/ontouml#>
SELECT ?stereotype ?ontological_nature (COUNT(DISTINCT ?individual) AS ?individual_count)
WHERE {
  ?individual a ontouml:Class;
              ontouml:stereotype ?stereotype;
              ontouml:restrictedTo ?ontological_nature .
}
GROUP BY ?stereotype ?ontological_nature
"""


SPARQL_GENERALIZATION_STEREOTYPES = """
PREFIX ontouml: <https://w3id.org/ontouml#>
SELECT ?stereotypeA ?stereotypeB (COUNT(?generalization) AS ?individual_count)
WHERE {
  ?generalization a ontouml:Generalization ;
                  ontouml:general ?generalClass ;
                  ontouml:specific ?specificClass .
  
  ?generalClass a ontouml:Class ;
                ontouml:stereotype ?stereotypeB .
  
  ?specificClass a ontouml:Class ;
                 ontouml:stereotype ?stereotypeA .
}
GROUP BY ?stereotypeA ?stereotypeB
"""

