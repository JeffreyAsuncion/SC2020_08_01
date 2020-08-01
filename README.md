# SC2020_08_01

# PART 4 ANSWERS

- In the Northwind database, what is the type of relationship between the
  `Employee` and `Territory` tables?
    - '`Employee` and `Territory` tables have a many-to-many relationship.
     - where Many Employees can represent a Territory 
     - as well as Many Territory can be represented by Many Employees 
     - There are three types of relationships between the data you are likely to encounter at this stage in the design: one-to-one, one-to-many, and many-to-many. To be able to identify these relationships, you need to examine the data and have an understanding of what business rules apply to the data and tables.




- What is a situation where a document store (like MongoDB) is appropriate, and
  what is a situation where it is not appropriate?
    - A Document store seems appropriate for a startup or a dynamic business model that is constantly changing data needs or "columns" Benefits of this model include: Ability to store dynamic data in unstructured, semi-structured, or structured formats. Ability to create persisted views from a base document and store the same for analysis. Ability to store and process large data sets.
    - This would be a problem with a bank or financial institution. The main disadvantage or issue in document oriented databases is security lacks. In database management systems security is very important. Relational databases are in use from a long period of time but document oriented databases are new, so they have many security issues which are discussed in the following section.



- What is "NewSQL", and what is it trying to achieve?
    - NewSQL is a new approach to relational databases that wants to combine transactional ACID (atomicity, consistency, isolation, durability) guarantees of good old RDBMSs and the horizontal scalability of NoSQL. Back in the day, Correctness and consistency were the two important metrics, rather than today’s metrics of performance and availability. With NewSQL you can have your cake and eat it too.