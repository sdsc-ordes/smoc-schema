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
Experiment {

}
Record {
    uriorcurie location
    DataFormat format
}
ReferenceGenome {
    string name
    integer taxon_id
    uriorcurie location
    uriorcurie source_uri
}
ReferenceSequence {
    string name
    string sequence_md5
    uriorcurie location
    uriorcurie source_uri
}
Sample {
    integer taxon_id
    string collector
}

StudyCollection ||--}o Study : "entries"
Study ||--|o Experiment : "has_experiment"
Experiment ||--|o Sample : "has_sample"
Experiment ||--|o Record : "has_record"
Record ||--|o Sample : "has_sample"
Record ||--|o ReferenceGenome : "has_reference"
ReferenceGenome ||--|o ReferenceSequence : "has_sequence"
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
