ONTOUML_VOCABULARY_TYPES = ["AggregationKind", "Cardinality", "Class", "Classifier", "ClassStereotype", "ClassView",
                            "ConnectorView", "DecoratableElement", "Diagram", "DiagramElement", "ElementView",
                            "Generalization", "GeneralizationSet", "GeneralizationSetView", "GeneralizationView",
                            "Literal", "ModelElement", "NodeView", "Note", "NoteView", "OntologicalNature",
                            "OntoumlElement", "Package", "PackageView", "Path", "Point", "Project", "Property",
                            "PropertyStereotype", "Rectangle", "RectangularShape", "Relation", "RelationStereotype",
                            "RelationView", "Shape", "Stereotype", "Text"]

ONTOUML_BOOLEAN_DATA_PROPERTIES = {"Class": ["isExtensional", "isPowertype", "isAbstract", "isDerived"],
                                   "Relation": ["isAbstract", "isDerived"],
                                   "GeneralizationSet": ["isComplete", "isDisjoint"],
                                   "Property": ["isOrdered", "isReadOnly", "isDerived"]}

ONTOUML_CLASS_STEREOTYPES = ["abstract", "category", "collective", "datatype", "enumeration", "event", "historicalRole",
                             "historicalRoleMixin", "kind", "mixin", "mode", "phase", "phaseMixin", "quality",
                             "quantity", "relator", "role", "roleMixin", "situation", "subkind", "type"]

ONTOUML_CLASS_NATURE = ["abstractNature", "collectiveNature", "eventNature", "extrinsicModeNature",
                        "functionalComplexNature", "intrinsicModeNature", "qualityNature", "quantityNature",
                        "relatorNature", "situationNature", "typeNature"]

ONTOUML_RELATION_STEREOTYPES = ["bringsAbout", "characterization", "comparative", "componentOf", "creation",
                                "derivation", "externalDependence", "historicalDependence", "instantiation",
                                "manifestation", "material", "mediation", "memberOf", "participation",
                                "participational", "subCollectionOf", "subQuantityOf", "termination", "triggers"]

ONTOUML_PROPERTY_STEREOTYPES = ["begin", "end"]

ONTOUML_AGGREGATION_KIND = ["composite", "none", "shared"]