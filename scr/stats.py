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
        self.Relation_St_none = 0

        for elem in ONTOUML_PROPERTY_STEREOTYPES:
            setattr(self, f"Property_St_{elem}", 0)
        self.Property_St_others = 0
        self.Property_St_none = 0


        for elem in ONTOUML_CLASS_NATURE:
            setattr(self, f"Class_ON_{elem}", 0)
            self.Class_ON_others = 0
            self.Class_ON_none = 0

        for elem in ONTOUML_AGGREGATION_KIND:
            setattr(self, f"Property_AK_{elem}", 0)
        self.Property_AK_others = 0
        self.Property_AK_none = 0

        for elem_st in ONTOUML_CLASS_STEREOTYPES:
            for elem_on in ONTOUML_CLASS_NATURE:
                setattr(self, f"Class_St-ON_{elem_st}_{elem_on}", 0)

        for stereotype in ONTOUML_CLASS_STEREOTYPES:
            setattr(self, f"Gen_only_specific_{stereotype}", 0)
            setattr(self, f"Gen_only_general_{stereotype}", 0)
            setattr(self, f"Gen_specific_general_{stereotype}", 0)
            setattr(self, f"Gen_none_{stereotype}", 0)

        for st_g in ONTOUML_CLASS_STEREOTYPES + ["none", "others"]:
            for st_s in ONTOUML_CLASS_STEREOTYPES + ["none", "others"]:
                setattr(self, f"Gen_dir_{st_s}_{st_g}", 0)
                setattr(self, f"Gen_all_{st_s}_{st_g}", 0)

    def __repr__(self):
        return f'Stats(model={self.__dict__})'
