- You can find basic CRUD operations of firestore in [Demo.py](./Demo.py) file.
- Activity for College Management System is in [CollegeManagementSystem.py](./CollegeManagementSystem.py) file.
- In here, used SQL query is:
```sql
CREATE TABLE Student (
    sid INT PRIMARY KEY,
    fname VARCHAR(255),
    lname VARCHAR(255),
    dob DATE,
    status VARCHAR(255),
    grade FLOAT
);

CREATE TABLE Class (
    cid INT PRIMARY KEY,
    cname VARCHAR(255),
    credits INT,
    grade FLOAT
);

CREATE TABLE Instructor (
    tid INT PRIMARY KEY,
    name VARCHAR(255),
    dept VARCHAR(255),
    grade FLOAT
);

CREATE TABLE Takes (
    sid INT,
    cid INT,
    PRIMARY KEY (sid, cid),
    FOREIGN KEY (sid) REFERENCES Student(sid),
    FOREIGN KEY (cid) REFERENCES Class(cid)
);

CREATE TABLE Teaches (
    tid INT,
    cid INT,
    PRIMARY KEY (tid, cid),
    FOREIGN KEY (tid) REFERENCES Instructor(tid),
    FOREIGN KEY (cid) REFERENCES Class(cid)
);
```
Migrating a SQL schema to Firestore involves transforming your relational data model into a document-oriented data model. Here's a general approach:

1. **Understand Firestore's Data Model**: Firestore organizes data as collections of documents, and documents can contain subcollections. Each document is a set of key-value pairs, similar to a row in SQL. However, unlike SQL, Firestore doesn't support joins or complex transactions⁷.

2. **Transform Your Data Model**: You'll need to convert your tables into collections, rows into documents, and columns into fields. For relationships, you might use references (like pointers), nested collections, or denormalization (duplicating data). In your case, `Student`, `Class`, and `Instructor` could be collections, and `Takes` and `Teaches` could be represented as fields within the `Student` and `Instructor` documents, respectively, containing arrays of references to `Class` documents⁷.

3. **Migrate Your Data**: You can write a script to export data from your SQL database, transform it to match your Firestore data model, and then import it into Firestore¹³. Firestore's client libraries (available in several programming languages) or REST API can be used for this¹.

4. **Query Your Data**: Firestore's query model is more limited than SQL's. You'll need to structure your data to support your queries. Firestore queries are shallow, meaning you can retrieve documents from a collection, but not documents within a subcollection of those documents⁴.

Remember, Firestore is a NoSQL database, so it's fundamentally different from SQL. It's important to design your Firestore data model based on the queries you'll need to perform, rather than trying to replicate your SQL schema⁷. If you're new to Firestore, consider working with someone experienced in NoSQL databases to help with your migration³.

In this example, the `classes` field in a `Student` document is an array of class IDs, representing the `Takes` relationship. Similarly, the `students` and `instructors` fields in a `Class` document represent the `Takes` and `Teaches` relationships, respectively⁷.

Please consult with a Firestore professional to ensure your Firestore schema meets your application's needs and follows best practices. Also, always test your migration with a subset of your data before fully migrating to Firestore³.

Source: Conversation with Bing, 11/7/2023
(1) undefined. https://stackoverflow.com/questions/47076373/how-to-design-a-cloud-firestore-database-schema.
(2) Firestore: import sql database - Stack Overflow. https://stackoverflow.com/questions/49207372/firestore-import-sql-database.
(3) How to migrate MySql Database to Firestore - Stack Overflow. https://stackoverflow.com/questions/48689817/how-to-migrate-mysql-database-to-firestore.
(4) FireSQL - Query Firestore using SQL syntax - Firebase Open Source. https://firebaseopensource.com/projects/jsayol/firesql/.
(5) . https://bing.com/search?q=convert+SQL+schema+to+Firestore.
(6) undefined. https://firebase.google.com/docs/firestore/manage-data/export-import%29.
(7) undefined. https://firebase.google.com/docs/firestore/manage-data/export-import.