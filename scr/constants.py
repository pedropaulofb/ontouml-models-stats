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
