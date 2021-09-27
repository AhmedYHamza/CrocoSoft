CREATE TABLE employee (
  ssn Int,
  emp_name Text,
  job_title Text,
  email Text,
  PRIMARY KEY (ssn)
);

CREATE TABLE document (
  doc_id Int,
  is_from_outside Bool,
  doc_status Text,
  date_created Date,
  date_modified Date,
  PRIMARY KEY (doc_id)
);

CREATE TABLE draft (
  draft_id Int,
  doc_id Int,
  PRIMARY KEY (draft_id),
  FOREIGN KEY (doc_id) REFERENCES document(doc_id)
);

CREATE TABLE draft_copy (
  copy_id Int,
  draft_id Int,
  PRIMARY KEY (copy_id),
  FOREIGN KEY (draft_id) REFERENCES draft(draft_id)
);

CREATE TABLE outside_document (
  doc_id Int,
  receipt_date Date,
  receipt_num Text,
  PRIMARY KEY (doc_id),
  FOREIGN KEY (doc_id) REFERENCES document(doc_id)
);

CREATE TABLE document_circulation (
  circulation_id Int,
  source_id Int,
  source_type Text,
  emp_ssn Int,
  modify_date Date,
  PRIMARY KEY (circulation_id),
  FOREIGN KEY (emp_ssn) REFERENCES employee(ssn)
);

INSERT INTO document(doc_id,is_from_outside,doc_status,date_created,date_modified)
    VALUES (1,0,"Recieved",CURDATE(),null),
    (2,1,"Recieved",CURDATE(),null),
    (3,0,"Recieved",CURDATE(),null),
    (4,1,"Recieved",CURDATE(),null),
    (5,0,"Recieved",CURDATE(),null);
    
SELECT * 
FROM Document;

INSERT INTO outside_document(doc_id,receipt_date,receipt_num)
    VALUES (2,'2020-5-4',255),(4,'2020-6-5',1222);
    
INSERT INTO employee(ssn,emp_name,job_title,email)
    VALUES (1,"ahmed","software engineer","ahmed@gmail.com"),
			(2,"mohamed","backend engineer","mohamed@gmail.com"),
            (3,"mahmoud","QA engineer","mahmoud@gmail.com"),
            (4,"yasser","Product manager","yasser@gmail.com"),
            (5,"hamza","frontend engineer","hamza@gmail.com");

INSERT INTO draft(draft_id,doc_id)
    VALUES (1,1),
			(2,2),
            (3,1),
            (4,1),
            (5,4);
            
INSERT INTO draft_copy(copy_id,draft_id)
    VALUES (1,2),
			(2,1),
			(3,1),
            (4,5),
            (5,3);
            
INSERT INTO document_circulation(circulation_id,source_id,source_type,emp_ssn,modify_date)
    VALUES (1,1,"doc",1,CURDATE()),
			(2,2,"drft",2,CURDATE()),
			(3,1,"cpy",3,CURDATE()),
            (4,4,"drft",1,CURDATE()),
            (5,5,"doc",4,CURDATE());
            

SELECT *
FROM document_circulation;
