# smoc-schema

Metadata schema for the SMOC Multi-Omics Digital Object

```mermaid
erDiagram
StudyCollection {

}
Study {
    datetime start_date  
    datetime completion_date  
    uriorcurie id  
    string name  
    string description  
}
Assay {
    OmicsTypeList omics_type  
    uriorcurie id  
    string name  
    string description  
}
DataEntity {
    uri location  
    DataFormat data_format  
    uriorcurie id  
    string name  
    string description  
}
ReferenceGenome {
    uri location  
    integerList taxon_id  
    uri source_uri  
    uriorcurie id  
    string name  
    string description  
}
ReferenceSequence {
    string sequence_md5  
    uri source_uri  
    uriorcurie id  
    string name  
    string description  
}
Sample {
    integerList taxon_id  
    stringList collector  
    uriorcurie id  
    string name  
    string description  
}

StudyCollection ||--}o Study : "entries"
Study ||--}o Assay : "has_assay"
Assay ||--}o Sample : "has_sample"
Assay ||--}o DataEntity : "has_data"
DataEntity ||--}o Sample : "has_sample"
DataEntity ||--|o ReferenceGenome : "has_reference"
ReferenceGenome ||--}o ReferenceSequence : "has_sequence"
```


## Website

[https://sdsc-ordes.github.io/smoc-schema](https://sdsc-ordes.github.io/smoc-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [smoc_schema](src/smoc_schema)
    * [schema](src/smoc_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/smoc_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
