

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ReferenceGenome" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	source_uri TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Sample" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
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

CREATE TABLE "AlignmentSet" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	location TEXT NOT NULL, 
	data_format VARCHAR(5) NOT NULL, 
	has_sample TEXT, 
	has_reference TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_reference) REFERENCES "ReferenceGenome" (id)
);

CREATE TABLE "Array" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	location TEXT NOT NULL, 
	data_format VARCHAR(5) NOT NULL, 
	has_sample TEXT, 
	has_reference TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_reference) REFERENCES "ReferenceGenome" (id)
);

CREATE TABLE "Assay" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	has_sample TEXT, 
	"Study_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Study_id") REFERENCES "Study" (id)
);

CREATE TABLE "ReferenceSequence" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	location TEXT NOT NULL, 
	sequence_md5 TEXT, 
	source_uri TEXT, 
	"ReferenceGenome_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ReferenceGenome_id") REFERENCES "ReferenceGenome" (id)
);

CREATE TABLE "VariantSet" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	location TEXT NOT NULL, 
	data_format VARCHAR(5) NOT NULL, 
	has_sample TEXT, 
	has_reference TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_reference) REFERENCES "ReferenceGenome" (id)
);

CREATE TABLE "ReferenceGenome_taxon_id" (
	backref_id TEXT, 
	taxon_id INTEGER, 
	PRIMARY KEY (backref_id, taxon_id), 
	FOREIGN KEY(backref_id) REFERENCES "ReferenceGenome" (id)
);

CREATE TABLE "Sample_taxon_id" (
	backref_id TEXT, 
	taxon_id INTEGER, 
	PRIMARY KEY (backref_id, taxon_id), 
	FOREIGN KEY(backref_id) REFERENCES "Sample" (id)
);

CREATE TABLE "Sample_collector" (
	backref_id TEXT, 
	collector TEXT, 
	PRIMARY KEY (backref_id, collector), 
	FOREIGN KEY(backref_id) REFERENCES "Sample" (id)
);

CREATE TABLE "DataEntity" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	location TEXT NOT NULL, 
	data_format VARCHAR(5) NOT NULL, 
	has_sample TEXT, 
	has_reference TEXT, 
	"Assay_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_reference) REFERENCES "ReferenceGenome" (id), 
	FOREIGN KEY("Assay_id") REFERENCES "Assay" (id)
);

CREATE TABLE "Assay_omics_type" (
	backref_id TEXT, 
	omics_type VARCHAR(15) NOT NULL, 
	PRIMARY KEY (backref_id, omics_type), 
	FOREIGN KEY(backref_id) REFERENCES "Assay" (id)
);
