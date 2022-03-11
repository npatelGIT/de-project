create or replace TABLE DEPROJECT.PUBLIC.PHYSICIANPHONE (
	prvdr_id VARCHAR(100) NOT NULL,
	frst_name VARCHAR(100) NOT NULL,
	mid_nm VARCHAR(100),
	lst_nm VARCHAR(100),
	adrs_id VARCHAR(100),
	adrs_ln_1 VARCHAR(100),
	adrs_ln_2 VARCHAR(100),
	cty VARCHAR(100),
	st VARCHAR(10),
	zip VARCHAR(50),
	org_pac_id VARCHAR(50),
	phn_numbr VARCHAR(50),
	npi VARCHAR(50),
	primary key (prvdr_id)
);