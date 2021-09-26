CREATE TABLE document (
  doc_id Int NOT NULL,
  iS_from_outside Bool,
  doc_status Text,
  PRIMARY KEY (doc_id)
);

CREATE TABLE outside_document(
  doc_id Int NOT NULL,
  receipt_date Date,
  receipt_number Text,
  PRIMARY KEY (doc_id), 
  FOREIGN KEY (doc_id) REFERENCES document(doc_id)
);

CREATE TABLE employee (
  ssn Int NOT NULL,
  ename Text,
  job_title Text,
  email Text,
  PRIMARY KEY (ssn)
);

CREATE TABLE draft (
  doc_id Int NOT NULL,
  draft_id Int NOT NULL,
  PRIMARY KEY (doc_id,draft_id),
  FOREIGN KEY (doc_id) REFERENCES document(doc_id)
);

CREATE TABLE draft_copy (
  doc_id Int NOT NULL,
  draft_id Int NOT NULL,
  copy_id Int NOT NULL,
  PRIMARY KEY (doc_id,draft_id,copy_id),
  FOREIGN KEY (doc_id,draft_id) REFERENCES draft(doc_id,draft_id)
);

CREATE TABLE document_circulation (
  circulation_id Int NOT NULL,
  doc_id Int NOT NULL,
  essn Int NOT NULL,
  PRIMARY KEY (circulation_id),
  FOREIGN KEY (doc_id) REFERENCES document(doc_id),
  FOREIGN KEY (essn) REFERENCES employee(ssn)
);

CREATE TABLE copy_circulation (
  circulation_id Int NOT NULL,
  doc_id Int NOT NULL,
  draft_id Int NOT NULL,
  copy_id Int NOT NULL,
  essn Int NOT NULL,
  PRIMARY KEY (circulation_id),
  FOREIGN KEY (doc_id,draft_id,copy_id) REFERENCES draft_copy(doc_id,draft_id,copy_id)
);

CREATE TABLE draft_circulation (
  circulation_id Int NOT NULL,
  doc_id Int NOT NULL,
  draft_id Int NOT NULL,
  essn Int NOT NULL,
  PRIMARY KEY (circulation_id),
  FOREIGN KEY (doc_id,draft_id) REFERENCES draft(doc_id,draft_id),
  FOREIGN KEY (essn) REFERENCES employee(ssn)
);

INSERT INTO document(doc_id,is_from_outside,doc_status)
    VALUES (1,0,"Recieved"),(2,1,"Recieved"),(3,0,"Recieved"),(4,1,"Recieved"),(5,0,"Recieved");
    
SELECT * 
FROM Document;

INSERT INTO outside_document(doc_id,receipt_date,receipt_number)
    VALUES (2,'2020-5-4',255),(4,'2020-6-5',1222);
    
INSERT INTO employee(ssn,ename,job_title,email)
    VALUES (1,"ahmed","software engineer","ahmed@gmail.com"),
			(2,"mohamed","backend engineer","mohamed@gmail.com"),
            (3,"mahmoud","QA engineer","mahmoud@gmail.com"),
            (4,"yasser","Product manager","yasser@gmail.com"),
            (5,"hamza","frontend engineer","hamza@gmail.com");

INSERT INTO draft(doc_id,draft_id)
    VALUES (1,1),
			(1,2),
            (3,1),
            (4,1),
            (5,1);
            
INSERT INTO draft_copy(doc_id,draft_id,copy_id)
    VALUES (1,1,1),
			(1,1,2),
			(1,2,1),
            (4,1,1),
            (5,1,1);
            
INSERT INTO document_circulation(circulation_id,doc_id,essn)
    VALUES (1,1,1),
			(2,2,2),
			(3,1,3),
            (4,4,1),
            (5,5,4);
            
INSERT INTO draft_circulation(circulation_id,doc_id,draft_id,essn)
    VALUES (1,1,1,1),
			(2,1,2,2),
			(3,4,1,3),
            (4,3,1,1),
            (5,5,1,4);
            
INSERT INTO copy_circulation(circulation_id,doc_id,draft_id,copy_id,essn)
    VALUES (1,1,1,1,1),
			(2,1,1,2,2),
			(3,4,1,1,3),
            (4,1,2,1,1),
            (5,5,1,1,4);

SELECT *
FROM outside_document;