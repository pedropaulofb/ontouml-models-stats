from scr.constants import ONTOUML_VOCABULARY_TYPES


class Stats:
    def __init__(self, model: str):
        # Mandatory for init
        self.model: str = model

        for ontouml_type in ONTOUML_VOCABULARY_TYPES:
            setattr(self, ontouml_type, 0)

    def calculate_derived(self):
        pass

    def validate(self):
        pass

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
#         # DATA ASSERTED
#
#         # All Vocabulary Classes
#
#         self.aggregationkind:int = 0
#         self.cardinality:int = 0
#         self.ou_class:int = 0
#         self.classifier:int = 0
#         self.classstereotype:int = 0
#         self.classview:int = 0
#         self.connectorview:int = 0
#         self.decoratableelement:int = 0
#         self.diagram:int = 0
#         self.diagramelement:int = 0
#         self.elementview:int = 0
#         self.generalization:int = 0
#         self.generalizationset:int = 0
#         self.generalizationsetview:int = 0
#         self.generalizationview:int = 0
#         self.literal:int = 0
#         self.modelelement:int = 0
#         self.nodeview:int = 0
#         self.note:int = 0
#         self.noteview:int = 0
#         self.ontologicalnature:int = 0
#         self.ontoumlelement:int = 0
#         self.package:int = 0
#         self.packageview:int = 0
#         self.path:int = 0
#         self.point:int = 0
#         self.project:int = 0
#         self.property:int = 0
#         self.propertystereotype:int = 0
#         self.rectangle:int = 0
#         self.rectangularshape:int = 0
#         self.relation:int = 0
#         self.relationstereotype:int = 0
#         self.relationview:int = 0
#         self.shape:int = 0
#         self.stereotype:int = 0
#         self.text:int = 0
#
#
#         # Classes' Stereotypes
#
#         self.cs_abstract: int = 0
#         self.cs_category: int = 0
#         self.cs_collective: int = 0
#         self.cs_datatype: int = 0
#         self.cs_enumeration: int = 0
#         self.cs_event: int = 0
#         self.cs_historicalrole: int = 0
#         self.cs_historicalrolemixin: int = 0
#         self.cs_kind: int = 0
#         self.cs_mixin: int = 0
#         self.cs_mode: int = 0
#         self.cs_phase: int = 0
#         self.cs_phasemixin: int = 0
#         self.cs_quality: int = 0
#         self.cs_quantity: int = 0
#         self.cs_relator: int = 0
#         self.cs_role: int = 0
#         self.cs_rolemixin: int = 0
#         self.cs_situation: int = 0
#         self.cs_subkind: int = 0
#         self.cs_type: int = 0
#
#         self.cs_other: int = 0
#         self.cs_other_list: str = ""
#         self.cs_none: int = 0
#
#         # Relations' Stereotypes
#
#         self.rs_bringsabout:int = 0
#         self.rs_characterization:int = 0
#         self.rs_comparative:int = 0
#         self.rs_componentof:int = 0
#         self.rs_creation:int = 0
#         self.rs_derivation:int = 0
#         self.rs_externaldependence:int = 0
#         self.rs_historicaldependence:int = 0
#         self.rs_instantiation:int = 0
#         self.rs_manifestation:int = 0
#         self.rs_material:int = 0
#         self.rs_mediation:int = 0
#         self.rs_memberof:int = 0
#         self.rs_participation:int = 0
#         self.rs_participational:int = 0
#         self.rs_subcollectionof:int = 0
#         self.rs_subquantityof:int = 0
#         self.rs_termination:int = 0
#         self.rs_triggers:int = 0
#
#         self.rs_other:int = 0
#         self.rs_other_list: str = ""
#         self.rs_none:int = 0
#
#
#         # Ontological Natures
#
#         self.on_abstractnature: int = 0
#         self.on_collectivenature: int = 0
#         self.on_eventnature: int = 0
#         self.on_extrinsicmodenature: int = 0
#         self.on_functionalcomplexnature: int = 0
#         self.on_intrinsicmodenature: int = 0
#         self.on_qualitynature: int = 0
#         self.on_quantitynature: int = 0
#         self.on_relatornature: int = 0
#         self.on_situationnature: int = 0
#         self.on_typenature: int = 0
#
#         self.on_other: int = 0
#         self.on_other_list: str = ""
#         self.on_none: int = 0
#
#         # Aggregation Kinds
#
#         self.ak_composite: int = 0
#         self.ak_none: int = 0
#         self.ak_shared: int = 0
#
#         self.ak_other: int = 0
#         self.ak_other_list: str = ""
#
#         # Property Stereotype
#
#         self.ps_begin: int = 0
#         self.ps_end: int = 0
#
#         self.ps_other: int = 0
#         self.ps_other_list: str = ""
#         self.ps_none: int = 0