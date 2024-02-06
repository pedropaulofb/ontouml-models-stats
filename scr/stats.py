from scr.constants import ONTOUML_VOCABULARY_TYPES, ONTOUML_BOOLEAN_DATA_PROPERTIES, ONTOUML_CLASS_STEREOTYPES, \
    ONTOUML_CLASS_NATURE, ONTOUML_RELATION_STEREOTYPES, ONTOUML_PROPERTY_STEREOTYPES, ONTOUML_AGGREGATION_KIND


class Stats:
    def __init__(self, model: str):
        # Mandatory for init
        self.model: str = model

        # DATA

        for elem in ONTOUML_VOCABULARY_TYPES:
            setattr(self, elem, 0)

        for elem, data_properties in ONTOUML_BOOLEAN_DATA_PROPERTIES.items():
            for data_property in data_properties:
                setattr(self, f"{elem}_{data_property}_True", 0)
                setattr(self, f"{elem}_{data_property}_False", 0)

        for elem in ONTOUML_CLASS_STEREOTYPES:
            setattr(self, f"Class_St_{elem}", 0)
        self.Class_St_others = 0
        self.Class_St_none = 0

        for elem in ONTOUML_RELATION_STEREOTYPES:
            setattr(self, f"Relation_St_{elem}", 0)
        self.Relation_St_others = 0

        for elem in ONTOUML_PROPERTY_STEREOTYPES:
            setattr(self, f"Property_St_{elem}", 0)
        self.Property_St_others = 0

        for elem in ONTOUML_CLASS_NATURE:
            setattr(self, f"Class_ON_{elem}", 0)

        for elem in ONTOUML_AGGREGATION_KIND:
            setattr(self, f"Property_AK_{elem}", 0)
        self.Property_AK_others = 0

        for elem_st in ONTOUML_CLASS_STEREOTYPES:
            for elem_on in ONTOUML_CLASS_NATURE:
                setattr(self, f"Class_St-ON_{elem_st}_{elem_on}", 0)

        for st_g in ONTOUML_CLASS_STEREOTYPES:
            for st_s in ONTOUML_CLASS_STEREOTYPES:
                setattr(self, f"Generalization_{st_s}_{st_g}",0)


    def __repr__(self):
        return f'Stats(model={self.__dict__})'

#         # Metadata asserted attributes
#         self.keywords: str = ""
#         self.theme: str = ""
#         self.issued: int = 0
#         self.contributors: str = ""
#         self.langs: str = ""
#         self.lang_en: bool = False
#         self.lang_pt: bool = False
#         self.lang_nl: bool = False
#         self.lang_other: bool = False
#         self.lang_other_list: str = ""
#         self.license: str = ""
#         self.modified: int = 0
#         self.sources: str = ""
#         self.dft_conceptual_clarification: bool = False
#         self.dft_data_publication: bool = False
#         self.dft_decision_support_system: bool = False
#         self.dft_example: bool = False
#         self.dft_information_retrieval: bool = False
#         self.dft_interoperability: bool = False
#         self.dft_language_engineering: bool = False
#         self.dft_learning: bool = False
#         self.dft_ontologicalanalysis: bool = False
#         self.dft_software_engineering: bool = False
#         self.context_classroom: bool = False
#         self.context_industry: bool = False
#         self.context_research: bool = False
#         self.ontology_type_application: bool = False
#         self.ontology_type_core: bool = False
#         self.ontology_type_domain: bool = False
#         self.repr_style_ufo: bool = False
#         self.repr_style_ontouml: bool = False
#
#         # Metadata derived attributes
#         self.num_keywords: int = 0
#         self.num_contributors: int = 0
#         self.num_langs: int = 0
#         self.num_sources: int = 0
#         self.num_dfts: int = 0
#         self.num_contexts: int = 0
#         self.num_ontology_types: int = 0
#         self.num_repr_styles: int = 0
#
