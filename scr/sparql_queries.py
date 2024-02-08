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
SELECT ?property (COUNT(?individual) AS ?count_true)
WHERE {{
  ?individual a ontouml:{ontouml_type} ;
              ?property true .
  FILTER (?property = ontouml:{ontouml_property})
}}
GROUP BY ?property
"""

SPARQL_OBJECT_PROPERTY_QUERY = """
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

SPARQL_ALL_STEREOTYPES_ABOVE = """
PREFIX ontouml: <https://w3id.org/ontouml#>
SELECT ?stereotype (COUNT(?generalization) AS ?individual_count)
WHERE {
  ?generalization a ontouml:Generalization ;
                  ontouml:specific ?class .
  
  ?class a ontouml:Class ;
                ontouml:stereotype ?stereotype .

 FILTER NOT EXISTS {
     ?generalization2 a ontouml:Generalization ;
                 ontouml:general ?class .
     }
                                
}
GROUP BY ?stereotype
"""

SPARQL_GENERALIZATION_ONLY_GENERAL_STEREOTYPE = """
PREFIX ontouml: <https://w3id.org/ontouml#>
SELECT ?stereotype (COUNT(?generalization) AS ?individual_count)
WHERE {
  ?generalization a ontouml:Generalization ;
                  ontouml:general ?class .

  ?class a ontouml:Class ;
                ontouml:stereotype ?stereotype .
 
 FILTER NOT EXISTS {
     ?generalization2 a ontouml:Generalization ;
                 ontouml:specific ?class .
     }
}
GROUP BY ?stereotype
"""

SPARQL_STEREOTYPE_NOT_IN_GENERALIZATION = """
PREFIX ontouml: <https://w3id.org/ontouml#>
SELECT ?stereotype (COUNT(DISTINCT ?class) AS ?result)
WHERE {
  ?class a ontouml:Class;
         ontouml:stereotype ?stereotype .
  FILTER NOT EXISTS {
    { ?class ontouml:general ?generalization }
    UNION
    { ?generalization ontouml:specific ?class }
    ?generalization a ontouml:Generalization .
  }
} GROUP BY ?stereotype
"""

SPARQL_GENERALIZATION_BOTH_SPECIFIC_GENERAL_STEREOTYPE = """
PREFIX ontouml: <https://w3id.org/ontouml#>
SELECT ?stereotype (COUNT(DISTINCT ?class) AS ?result)
WHERE {
  ?class a ontouml:Class;
         ontouml:stereotype ?stereotype .

  FILTER EXISTS {
    ?generalization1 a ontouml:Generalization;
                      ontouml:general ?class .
  }
  FILTER EXISTS {
    ?generalization2 a ontouml:Generalization;
                      ontouml:specific ?class .
  }
}
GROUP BY ?stereotype
"""

