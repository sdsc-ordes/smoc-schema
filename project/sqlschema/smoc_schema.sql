

CREATE TABLE "AlignmentSet" (
	uri TEXT NOT NULL, 
	format VARCHAR(5) NOT NULL, 
	has_sample TEXT, 
	has_reference TEXT, 
	PRIMARY KEY (uri, format, has_sample, has_reference)
);

CREATE TABLE "Array" (
	uri TEXT NOT NULL, 
	format VARCHAR(5) NOT NULL, 
	has_sample TEXT, 
	has_reference TEXT, 
	PRIMARY KEY (uri, format, has_sample, has_reference)
);

CREATE TABLE "DataEntity" (
	uri TEXT NOT NULL, 
	format VARCHAR(5) NOT NULL, 
	has_sample TEXT, 
	has_reference TEXT, 
	PRIMARY KEY (uri, format, has_sample, has_reference)
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
	uri TEXT NOT NULL, 
	sequence_md5 TEXT, 
	source_uri TEXT, 
	PRIMARY KEY (name, uri, sequence_md5, source_uri)
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
	uri TEXT NOT NULL, 
	format VARCHAR(5) NOT NULL, 
	has_sample TEXT, 
	has_reference TEXT, 
	PRIMARY KEY (uri, format, has_sample, has_reference)
);

CREATE TABLE "Assay" (
	has_sample TEXT, 
	has_data TEXT, 
	"Study_id" TEXT, 
	PRIMARY KEY (has_sample, has_data, "Study_id"), 
	FOREIGN KEY("Study_id") REFERENCES "Study" (id)
);
