

CREATE TABLE "AlignmentSet" (
	location TEXT NOT NULL, 
	data_format VARCHAR(5) NOT NULL, 
	has_sample TEXT, 
	has_reference TEXT, 
	PRIMARY KEY (location, data_format, has_sample, has_reference)
);

CREATE TABLE "Array" (
	location TEXT NOT NULL, 
	data_format VARCHAR(5) NOT NULL, 
	has_sample TEXT, 
	has_reference TEXT, 
	PRIMARY KEY (location, data_format, has_sample, has_reference)
);

CREATE TABLE "DataEntity" (
	location TEXT NOT NULL, 
	data_format VARCHAR(5) NOT NULL, 
	has_sample TEXT, 
	has_reference TEXT, 
	PRIMARY KEY (location, data_format, has_sample, has_reference)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ReferenceGenome" (
	name TEXT, 
	has_sequence TEXT, 
	taxon_id INTEGER, 
	source_uri TEXT, 
	PRIMARY KEY (name, has_sequence, taxon_id, source_uri)
);

CREATE TABLE "ReferenceSequence" (
	name TEXT, 
	location TEXT NOT NULL, 
	sequence_md5 TEXT, 
	source_uri TEXT, 
	PRIMARY KEY (name, location, sequence_md5, source_uri)
);

CREATE TABLE "Sample" (
	taxon_id INTEGER, 
	collector TEXT, 
	PRIMARY KEY (taxon_id, collector)
);

CREATE TABLE "Study" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	start_date DATETIME NOT NULL, 
	completion_date DATETIME, 
	PRIMARY KEY (id)
);

CREATE TABLE "StudyCollection" (
	entries TEXT, 
	PRIMARY KEY (entries)
);

CREATE TABLE "VariantSet" (
	location TEXT NOT NULL, 
	data_format VARCHAR(5) NOT NULL, 
	has_sample TEXT, 
	has_reference TEXT, 
	PRIMARY KEY (location, data_format, has_sample, has_reference)
);

CREATE TABLE "Assay" (
	has_sample TEXT, 
	has_data TEXT, 
	omics_type VARCHAR(15) NOT NULL, 
	"Study_id" TEXT, 
	PRIMARY KEY (has_sample, has_data, omics_type, "Study_id"), 
	FOREIGN KEY("Study_id") REFERENCES "Study" (id)
);
