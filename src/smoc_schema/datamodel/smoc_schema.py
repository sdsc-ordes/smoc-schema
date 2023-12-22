# Auto generated from smoc_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-12-22T14:22:11
# Schema: smoc-schema
#
# id: https://w3id.org/sdsc-ordes/smoc-schema
# description: Metadata schema for the SMOC Multi-Omics Digital Object
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Datetime, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EDAM = CurieNamespace('EDAM', 'http://edamontology.org/')
FG = CurieNamespace('FG', 'https://w3id.org/fair-genomes/ontology/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
BIOSCHEMAS = CurieNamespace('bioschemas', 'https://bioschemas.org/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SMOC_SCHEMA = CurieNamespace('smoc_schema', 'https://w3id.org/sdsc-ordes/smoc-schema/')
SPHN = CurieNamespace('sphn', 'https://biomedit.ch/rdf/sphn-schema/sphn#')
DEFAULT_ = SMOC_SCHEMA


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class StudyId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = SMOC_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Study(NamedThing):
    """
    Represents the digital object. It encapsulates omics and other datasets and their metadata.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SMOC_SCHEMA["Study"]
    class_class_curie: ClassVar[str] = "smoc_schema:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = SMOC_SCHEMA.Study

    id: Union[str, StudyId] = None
    start_date: Union[str, XSDDateTime] = None
    completion_date: Optional[Union[str, XSDDateTime]] = None
    has_assay: Optional[Union[Union[dict, "Assay"], List[Union[dict, "Assay"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self._is_empty(self.start_date):
            self.MissingRequiredField("start_date")
        if not isinstance(self.start_date, XSDDateTime):
            self.start_date = XSDDateTime(self.start_date)

        if self.completion_date is not None and not isinstance(self.completion_date, XSDDateTime):
            self.completion_date = XSDDateTime(self.completion_date)

        if not isinstance(self.has_assay, list):
            self.has_assay = [self.has_assay] if self.has_assay is not None else []
        self.has_assay = [v if isinstance(v, Assay) else Assay(**as_dict(v)) for v in self.has_assay]

        super().__post_init__(**kwargs)


@dataclass
class Assay(YAMLRoot):
    """
    A coordinated set of actions designed to generate data from samples.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SMOC_SCHEMA["Assay"]
    class_class_curie: ClassVar[str] = "smoc_schema:Assay"
    class_name: ClassVar[str] = "Assay"
    class_model_uri: ClassVar[URIRef] = SMOC_SCHEMA.Assay

    has_sample: Optional[Union[Union[dict, "Sample"], List[Union[dict, "Sample"]]]] = empty_list()
    has_data: Optional[Union[Union[dict, "DataEntity"], List[Union[dict, "DataEntity"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.has_sample, list):
            self.has_sample = [self.has_sample] if self.has_sample is not None else []
        self.has_sample = [v if isinstance(v, Sample) else Sample(**as_dict(v)) for v in self.has_sample]

        self._normalize_inlined_as_dict(slot_name="has_data", slot_type=DataEntity, key_name="location", keyed=False)

        super().__post_init__(**kwargs)


@dataclass
class Sample(YAMLRoot):
    """
    A biological sample used in assays. Examples include a whole organism, tissue or cell line.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SMOC_SCHEMA["Sample"]
    class_class_curie: ClassVar[str] = "smoc_schema:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = SMOC_SCHEMA.Sample

    taxon_id: Optional[Union[int, List[int]]] = empty_list()
    collector: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.taxon_id, list):
            self.taxon_id = [self.taxon_id] if self.taxon_id is not None else []
        self.taxon_id = [v if isinstance(v, int) else int(v) for v in self.taxon_id]

        if not isinstance(self.collector, list):
            self.collector = [self.collector] if self.collector is not None else []
        self.collector = [v if isinstance(v, str) else str(v) for v in self.collector]

        super().__post_init__(**kwargs)


@dataclass
class DataEntity(YAMLRoot):
    """
    An entity containing data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SMOC_SCHEMA["DataEntity"]
    class_class_curie: ClassVar[str] = "smoc_schema:DataEntity"
    class_name: ClassVar[str] = "DataEntity"
    class_model_uri: ClassVar[URIRef] = SMOC_SCHEMA.DataEntity

    location: Union[str, URI] = None
    data_format: Union[str, "DataFormat"] = None
    has_sample: Optional[Union[Union[dict, Sample], List[Union[dict, Sample]]]] = empty_list()
    has_reference: Optional[Union[dict, "ReferenceGenome"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, URI):
            self.location = URI(self.location)

        if self._is_empty(self.data_format):
            self.MissingRequiredField("data_format")
        if not isinstance(self.data_format, DataFormat):
            self.data_format = DataFormat(self.data_format)

        if not isinstance(self.has_sample, list):
            self.has_sample = [self.has_sample] if self.has_sample is not None else []
        self.has_sample = [v if isinstance(v, Sample) else Sample(**as_dict(v)) for v in self.has_sample]

        if self.has_reference is not None and not isinstance(self.has_reference, ReferenceGenome):
            self.has_reference = ReferenceGenome(**as_dict(self.has_reference))

        super().__post_init__(**kwargs)


@dataclass
class ReferenceGenome(YAMLRoot):
    """
    Reference assembly of a given genome, consisting of a collection of congiguous sequences (contigs).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SMOC_SCHEMA["ReferenceGenome"]
    class_class_curie: ClassVar[str] = "smoc_schema:ReferenceGenome"
    class_name: ClassVar[str] = "ReferenceGenome"
    class_model_uri: ClassVar[URIRef] = SMOC_SCHEMA.ReferenceGenome

    name: Optional[str] = None
    has_sequence: Optional[Union[Union[dict, "ReferenceSequence"], List[Union[dict, "ReferenceSequence"]]]] = empty_list()
    taxon_id: Optional[Union[int, List[int]]] = empty_list()
    source_uri: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_dict(slot_name="has_sequence", slot_type=ReferenceSequence, key_name="location", keyed=False)

        if not isinstance(self.taxon_id, list):
            self.taxon_id = [self.taxon_id] if self.taxon_id is not None else []
        self.taxon_id = [v if isinstance(v, int) else int(v) for v in self.taxon_id]

        if self.source_uri is not None and not isinstance(self.source_uri, URI):
            self.source_uri = URI(self.source_uri)

        super().__post_init__(**kwargs)


@dataclass
class ReferenceSequence(YAMLRoot):
    """
    A contiguous sequence of DNA part of a reference coordinate system (genome assembly).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SMOC_SCHEMA["ReferenceSequence"]
    class_class_curie: ClassVar[str] = "smoc_schema:ReferenceSequence"
    class_name: ClassVar[str] = "ReferenceSequence"
    class_model_uri: ClassVar[URIRef] = SMOC_SCHEMA.ReferenceSequence

    location: Union[str, URI] = None
    name: Optional[str] = None
    sequence_md5: Optional[str] = None
    source_uri: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.location):
            self.MissingRequiredField("location")
        if not isinstance(self.location, URI):
            self.location = URI(self.location)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.sequence_md5 is not None and not isinstance(self.sequence_md5, str):
            self.sequence_md5 = str(self.sequence_md5)

        if self.source_uri is not None and not isinstance(self.source_uri, URI):
            self.source_uri = URI(self.source_uri)

        super().__post_init__(**kwargs)


@dataclass
class AlignmentSet(DataEntity):
    """
    A data entity consisting of genomic intervals aligned to a reference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SMOC_SCHEMA["AlignmentSet"]
    class_class_curie: ClassVar[str] = "smoc_schema:AlignmentSet"
    class_name: ClassVar[str] = "AlignmentSet"
    class_model_uri: ClassVar[URIRef] = SMOC_SCHEMA.AlignmentSet

    location: Union[str, URI] = None
    data_format: Union[str, "DataFormat"] = None

@dataclass
class VariantSet(DataEntity):
    """
    A data entity consisting of genomic variants relative to a reference.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SMOC_SCHEMA["VariantSet"]
    class_class_curie: ClassVar[str] = "smoc_schema:VariantSet"
    class_name: ClassVar[str] = "VariantSet"
    class_model_uri: ClassVar[URIRef] = SMOC_SCHEMA.VariantSet

    location: Union[str, URI] = None
    data_format: Union[str, "DataFormat"] = None

@dataclass
class Array(DataEntity):
    """
    Data entity consisting of an N-dimensional array.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SMOC_SCHEMA["Array"]
    class_class_curie: ClassVar[str] = "smoc_schema:Array"
    class_name: ClassVar[str] = "Array"
    class_model_uri: ClassVar[URIRef] = SMOC_SCHEMA.Array

    location: Union[str, URI] = None
    data_format: Union[str, "DataFormat"] = None

@dataclass
class StudyCollection(YAMLRoot):
    """
    A holder for Study objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SMOC_SCHEMA["StudyCollection"]
    class_class_curie: ClassVar[str] = "smoc_schema:StudyCollection"
    class_name: ClassVar[str] = "StudyCollection"
    class_model_uri: ClassVar[URIRef] = SMOC_SCHEMA.StudyCollection

    entries: Optional[Union[Dict[Union[str, StudyId], Union[dict, Study]], List[Union[dict, Study]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Study, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class OmicsType(EnumDefinitionImpl):

    GENOMICS = PermissibleValue(
        text="GENOMICS",
        description="The study of the structure, function, expression, evolution, mapping and editing of genomes.",
        meaning=NCIT["C84343"])
    TRANSCRIPTOMICS = PermissibleValue(
        text="TRANSCRIPTOMICS",
        description="The study of the complete set of RNA transcripts that are produced by the genome.",
        meaning=NCIT["C153189"])
    METABOLOMICS = PermissibleValue(
        text="METABOLOMICS",
        description="The study of biological metabolic profiles.",
        meaning=NCIT["C49019"])
    PROTEOMICS = PermissibleValue(
        text="PROTEOMICS",
        description="The global analysis of cellular proteins.",
        meaning=NCIT["C20085"])

    _defn = EnumDefinition(
        name="OmicsType",
    )

class DataFormat(EnumDefinitionImpl):

    CRAM = PermissibleValue(
        text="CRAM",
        description="Referenced-based compression of alignment format.",
        meaning=EDAM["format_3462"])
    FASTQ = PermissibleValue(
        text="FASTQ",
        description="FASTQ short read format with sequence and any type of quality scores.",
        meaning=EDAM["format_1930"])
    Zarr = PermissibleValue(
        text="Zarr",
        description="Chunked, compressed N-dimensional arrays.",
        meaning=EDAM["format_3915"])

    _defn = EnumDefinition(
        name="DataFormat",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=SMOC_SCHEMA.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=SMOC_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=SMOC_SCHEMA.description, domain=None, range=Optional[str])

slots.completion_date = Slot(uri=FG.completion_date, name="completion_date", curie=FG.curie('completion_date'),
                   model_uri=SMOC_SCHEMA.completion_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.start_date = Slot(uri=FG.start_date, name="start_date", curie=FG.curie('start_date'),
                   model_uri=SMOC_SCHEMA.start_date, domain=None, range=Union[str, XSDDateTime])

slots.omics_type = Slot(uri=SMOC_SCHEMA.omics_type, name="omics_type", curie=SMOC_SCHEMA.curie('omics_type'),
                   model_uri=SMOC_SCHEMA.omics_type, domain=None, range=Union[Union[str, "OmicsType"], List[Union[str, "OmicsType"]]])

slots.has_assay = Slot(uri=SMOC_SCHEMA.has_assay, name="has_assay", curie=SMOC_SCHEMA.curie('has_assay'),
                   model_uri=SMOC_SCHEMA.has_assay, domain=None, range=Optional[Union[Union[dict, Assay], List[Union[dict, Assay]]]])

slots.has_sample = Slot(uri=SMOC_SCHEMA.has_sample, name="has_sample", curie=SMOC_SCHEMA.curie('has_sample'),
                   model_uri=SMOC_SCHEMA.has_sample, domain=None, range=Optional[Union[Union[dict, Sample], List[Union[dict, Sample]]]])

slots.has_data = Slot(uri=SMOC_SCHEMA.has_data, name="has_data", curie=SMOC_SCHEMA.curie('has_data'),
                   model_uri=SMOC_SCHEMA.has_data, domain=None, range=Optional[Union[Union[dict, DataEntity], List[Union[dict, DataEntity]]]])

slots.data_format = Slot(uri=SMOC_SCHEMA.data_format, name="data_format", curie=SMOC_SCHEMA.curie('data_format'),
                   model_uri=SMOC_SCHEMA.data_format, domain=None, range=Union[str, "DataFormat"])

slots.taxon_id = Slot(uri=SMOC_SCHEMA.taxon_id, name="taxon_id", curie=SMOC_SCHEMA.curie('taxon_id'),
                   model_uri=SMOC_SCHEMA.taxon_id, domain=None, range=Optional[Union[int, List[int]]])

slots.collector = Slot(uri=SMOC_SCHEMA.collector, name="collector", curie=SMOC_SCHEMA.curie('collector'),
                   model_uri=SMOC_SCHEMA.collector, domain=None, range=Optional[Union[str, List[str]]])

slots.location = Slot(uri=SMOC_SCHEMA.location, name="location", curie=SMOC_SCHEMA.curie('location'),
                   model_uri=SMOC_SCHEMA.location, domain=None, range=Union[str, URI])

slots.sequence_md5 = Slot(uri=SMOC_SCHEMA.sequence_md5, name="sequence_md5", curie=SMOC_SCHEMA.curie('sequence_md5'),
                   model_uri=SMOC_SCHEMA.sequence_md5, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[a-f0-9]{32}$'))

slots.source_uri = Slot(uri=SMOC_SCHEMA.source_uri, name="source_uri", curie=SMOC_SCHEMA.curie('source_uri'),
                   model_uri=SMOC_SCHEMA.source_uri, domain=None, range=Optional[Union[str, URI]])

slots.has_sequence = Slot(uri=SMOC_SCHEMA.has_sequence, name="has_sequence", curie=SMOC_SCHEMA.curie('has_sequence'),
                   model_uri=SMOC_SCHEMA.has_sequence, domain=None, range=Optional[Union[Union[dict, ReferenceSequence], List[Union[dict, ReferenceSequence]]]])

slots.has_reference = Slot(uri=SMOC_SCHEMA.has_reference, name="has_reference", curie=SMOC_SCHEMA.curie('has_reference'),
                   model_uri=SMOC_SCHEMA.has_reference, domain=None, range=Optional[Union[dict, ReferenceGenome]])

slots.studyCollection__entries = Slot(uri=SMOC_SCHEMA.entries, name="studyCollection__entries", curie=SMOC_SCHEMA.curie('entries'),
                   model_uri=SMOC_SCHEMA.studyCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, StudyId], Union[dict, Study]], List[Union[dict, Study]]]])