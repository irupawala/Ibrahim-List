

## 1. Key Characteristics of Distributed Systems

### 1. Scalability

* **Scalability is the capability of a system, process, or a network to grow and manage increased demand.** Any distributed system that can continuously evolve in order to support the growing amount of work is considered to be scalable.

* **Horizontal vs. Vertical Scaling:**

  Horizontal scaling means that you scale by adding more servers into your pool of resources whereas Vertical scaling means that you scale by adding more power (CPU, RAM, Storage, etc.) to an existing server.

* **Good Examples of horizontal scaling are Cassandra and [MongoDB**](https://en.wikipedia.org/wiki/MongoDB) as they both provide an easy way to scale horizontally by adding more machines to meet growing needs.

* Similarly, **a good example of vertical scaling is MySQL** as it allows for an easy way to scale vertically by switching from smaller to bigger machines. However, this process often involves downtime.



### 2. Reliability

* By definition, reliability is the probability a system will fail in a given period. In simple terms, a distributed system is considered reliable if it keeps delivering its services even when one or several of its software or hardware components fail.
* A reliable distributed system achieves this through redundancy of both the software components and data.
* Obviously, redundancy has a cost and a reliable system has to pay that to achieve such resilience for services by eliminating every single point of failure.



### 3. Availability

* Availability is the time a system remains operational to perform its required function in a specific period. It is a simple measure of the percentage of time that a system, service, or a machine remains operational under normal conditions.

* Reliability is availability over time considering the full range of possible real-world conditions that can occur. An aircraft that can make it through any possible weather safely is more reliable than one that has vulnerabilities to possible conditions.

* If a system is reliable, it is available. However, if it is available, it is not necessarily reliable.

  

### 4. Efficiency

* Throughput and Bandwidth



### 5. Serviceability or Manageability

* Serviceability or manageability is the simplicity and speed with which a system can be repaired or maintained; if the time to fix a failed system increases, then availability will decrease.
* Early detection of faults can decrease or avoid system downtime. For example, some enterprise systems can automatically call a service center (without human intervention) when the system experiences a system fault.



## 2. Load Balancer

* It has two functions:
  * It helps to spread the traffic across a cluster of servers to improve responsiveness and availability of applications, websites or databases. 
  * LB also keeps track of the status of all the resources while distributing requests. If a server is not available to take new requests or is not responding or has elevated error rate, LB will stop sending traffic to such a server.
  
* By balancing application requests across multiple servers, a load balancer reduces individual server load and prevents any one application server from becoming a single point of failure, thus improving overall application availability and responsiveness.

* **Benefits of Load Balancing**

  * faster uninterrupted service by decreasing wait time for users
  * less downtime 
  * higher throughput
  * smart load balancers can predict traffic bottlenecks before they happen 
  * system experiences few failed and stressed components

* **Load Balancing Algorithms**

  Load balancers consider two factors before forwarding a request to a backend server.

  1. They will first ensure that the server they choose is actually responding appropriately to requests
  2. then use a pre-configured algorithm to select one from the set of healthy servers.

* **Health Checks** - Load balancers should only forward traffic to “healthy” backend servers. To monitor the health of a backend server, “health checks” regularly attempt to connect to backend servers to ensure that servers are listening. If a server fails a health check, it is automatically removed from the pool, and traffic will not be forwarded to it until it responds to the health checks again.

* Load Balancing Methods:
  * Least Connection Method
  * Least Response Time Method
  * Least Bandwidth Method
  * Round Robin Method
  * Weighted Round Robin Method
  * IP Hash - the IP address of the client determines which server receives the request.
  
* [load balancing](https://www-stage.avinetworks.com/glossary/load-balancing/) took on more responsibilities with the advent of Application Delivery Controllers (ADCs).

* ADCs fall into three categories:
  * hardware appliances
  * virtual appliances (essentially the software extracted from legacy hardware)
  * software-native load balancers

* Redundant Load Balancers
  
  * The load balancer can be a single point of failure; to overcome this, a second load balancer can be connected to the first to form a cluster. Each LB monitors the health of the other and, since both of them are equally capable of serving traffic and failure detection, in the event the main load balancer fails, the second load balancer takes over.

### Load Balancing and SSL

* Secure Sockets Layer (SSL) is the standard security technology for establishing an encrypted link between a web server and a browser. [SSL](https://blog.hubspot.com/marketing/what-is-ssl?__hstc=153467111.2d0a90cd66bb1b9eaba24fd7c827edec.1656009245767.1656009245767.1656226159490.2&__hssc=153467111.1.1656226159490&__hsfp=579608783) traffic is often decrypted at the load balancer. 
* When a load balancer decrypts traffic before passing the request on, it is called SSL termination. 
* The load balancer saves the web servers from having to expend the extra CPU cycles required for decryption. This improves application performance.
* However, [SSL termination](https://parksehun.medium.com/ssl-passthrough-vs-ssl-termination-vs-ssl-bridging-f66b24d4d0aa) comes with a security concern. The traffic between the load balancers and the web servers is no longer encrypted. This can expose the application to possible attack. However, the risk is lessened when the load balancer is within the same data center as the web servers.

### Load Balancing and Security

* Load Balancing plays an important security role as computing moves evermore to the cloud. The off-loading function of a load balancer defends an organization against distributed denial-of-service (DDoS) attacks. 
* It does this by shifting attack traffic from the corporate server to a public cloud provider.

### From Additional Links mentioned on Grokking

* Load balancers conduct continuous health checks on servers to ensure they can handle requests. If necessary, the load balancer removes unhealthy servers from the pool until they are restored. Some load balancers even trigger the creation of new virtualized application servers to cope with increased demand.

### OSI Model

https://www.webopedia.com/definitions/7-layers-of-osi-model/

## 3. Caching

* Load balancing helps you scale horizontally across an ever-increasing number of servers, but caching will enable you to make vastly better use of the resources you already have.
* Caches take advantage of the locality of reference principle: recently requested data is likely to be requested again.
* A cache is like short-term memory: it has a limited amount of space, but is typically faster than the original data source and contains the most recently accessed items.

### Cache Invalidation

* While caching is fantastic, it requires some maintenance to keep the cache coherent with the source of truth (e.g., database). If the data is modified in the database, it should be invalidated in the cache; if not, this can cause inconsistent application behavior. Solving this problem is known as cache invalidation.
* There are three main schemes that are used:
  1. Write-through cache
  2. Write-around cache
  3. Write-back cache

### Cache eviction policies

1. First In First Out (FIFO)
2. Last In First Out (LIFO)
3. Least Recently Used (LRU)
4. Most Recently Used (MRU)
5. Least Frequently Used (LFU)
6. Random Replacement (RR)

## 4. Data Partitioning

* Data partitioning is a technique to break a big database (DB) into many smaller parts. It is the process of splitting up a DB/table across multiple machines to improve the manageability, performance, availability, and load balancing of an application.

### Partitioning Methods

**a. Horizontal Partitioning**

* In this scheme, we put different rows into different tables. For example, if **we store different places in a table**, we can decide that locations with ZIP codes less than 10000 are stored in one table and places with ZIP codes greater than 10000 are stored in a separate table. 

**b. Vertical Partitioning**

* In this scheme, **we divide our data to store tables related to a specific feature in their own server.** For example, if we are building an Instagram-like application - where we need to store data related to users, photos they upload, and people they follow - we can decide to place user profile information on one DB server, friend lists on another, and photos on a third server.
* The main problem with this approach is that if our application experiences additional growth, then it may be necessary to further partition a feature specific DB across various servers (e.g. it would not be possible for a single server to handle all the metadata queries for 10 billion photos by 140 million users).

**c. Directory-Based Partitioning**

* A loosely coupled approach to work around issues mentioned in the above schemes is to create a **lookup service** that knows your current partitioning scheme and abstracts it away from the DB access code. So, to find out where a particular data entity resides, we query the **directory server that holds the mapping between each tuple key to its DB server.**

### Partitioning Criteria

**a. Key or Hash-based Partitioning**

* Under this scheme, we apply a hash function to some key attributes of the entity we are storing; that yields the partition number. For example, if we have 100 DB servers and our ID is a numeric value that gets incremented by one each time a new record is inserted. In this example, the hash function could be ‘ID % 100’, which will give us the server number where we can store/read that record.

**b. List Partitioning**

* In this scheme, each partition is assigned a list of values, so whenever we want to insert a new record, we will see which partition contains our key and then store it there. For example, we can decide all users living in Iceland, Norway, Sweden, Finland, or Denmark will be stored in a partition for the Nordic countries.

**c. Round-robin Partitioning**

* This is a very simple strategy that ensures uniform data distribution. With ‘n’ partitions, the ‘i’ tuple is assigned to partition (i mod n).

**d. Composite Partitioning**

* Under this scheme, we combine any of the above partitioning schemes to devise a new scheme. For example, first applying a list partitioning scheme and then a hash-based partitioning.
* Consistent hashing could be considered a composite of hash and list partitioning where the hash reduces the key-space to a size that can be listed.

### Common Problems of Data Partitioning

On a partitioned database, there are certain extra constraints on the different operations that can be performed. Most of these constraints are due to the fact that operations across multiple tables or multiple rows in the same table will no longer run on the same server.

**a. Joins and Denormalization:** Performing joins on a database that is running on one server is straightforward, but once a database is partitioned and spread across multiple machines it is often not feasible to perform joins that span database partitions. Such joins will not be performance efficient since data has to be compiled from multiple servers.

A common workaround for this problem is to de-normalize the database so that queries that previously required joins can be performed from a single table. Of course, the service now has to deal with denormalization’s perils, such as data inconsistency.

**b. Referential integrity:** As we saw that performing a cross-partition query on a partitioned database is not feasible; similarly, trying to enforce data integrity constraints such as foreign keys in a partitioned database can be extremely difficult.

**c. Rebalancing:** There could be many reasons we have to change our partitioning scheme:

1. The data distribution is not uniform, e.g., there are a lot of places for a particular ZIP code that cannot fit into one database partition.
2. There is a lot of load on a partition, e.g., there are too many requests being handled by the DB partition dedicated to user photos.

## 5. Database Indexes

* A **database index** is a [data structure](https://en.wikipedia.org/wiki/Data_structure) that improves the speed of data retrieval operations on a [database table](https://en.wikipedia.org/wiki/Table_(database)) at the cost of additional writes and storage space to maintain the index data structure. Indexes are used to quickly locate data without having to search every row in a database table every time a database table is accessed. Indexes can be created using one or more [columns of a database table](https://en.wikipedia.org/wiki/Column_(database)), providing the basis for both rapid random [lookups](https://en.wikipedia.org/wiki/Lookup) and efficient access of ordered records.
* Indexes can be created using one or more columns of a database table, providing the basis for both rapid random lookups and efficient access of ordered records.

### Example: A library Catalog

* Simply saying, an index is a data structure that can be perceived as a table of contents that points us to the location where actual data lives. **So when we create an index on a column of a table, we store that column and a pointer to the whole row in the index.**

### How do Indexes decrease write performance?

* An index can dramatically speed up data retrieval but may itself be large due to the additional keys, which slow down data insertion & update.
* When adding rows or making updates to existing rows for a table with an active index, we not only have to write the data but also have to update the index. This will decrease the write performance.

## 6. Proxies

### What is a proxy server?

* A proxy server is an intermediate piece of software or hardware that sits between the client and the server. Clients connect to a proxy to make a request for a service like a web page, file, or connection from the server.
* **Essentially, a proxy server (aka the forward proxy) is a piece of software or hardware that facilitates the request for resources from other servers on behalf of clients, thus anonymizing the client from the server.**
* A proxy is a piece of software or hardware that sits between a client and a server to facilitate traffic. A forward proxy hides the identity of the client, whereas a reverse proxy conceals the identity of the server.

### Forward Proxy

* ***A forward proxy can hide the identity of the client from the server by sending requests on behalf of the client.***
* In addition to coordinating requests from multiple servers, proxies can also optimize request traffic from a system-wide perspective. Proxies can combine the same data access requests into one request and then return the result to the user; this technique is called **collapsed forwarding**.

### Reverse Proxy

* A reverse proxy retrieves resources from one or more servers on behalf of a client. These resources are then returned to the client, appearing as if they originated from the proxy server itself, thus anonymizing the server.
* Contrary to the forward proxy, which hides the client’s identity, a reverse proxy hides the server’s identity.

## 7. Redundancy and Replication

**Redundancy**

* [Redundancy](https://en.wikipedia.org/wiki/Redundancy_(engineering)) is the duplication of critical components or functions of a system with the intention of increasing the reliability of the system, usually in the form of a backup or fail-safe, or to improve actual system performance. 
* Redundancy plays a key role in removing the single points of failure in the system and provides backups if needed in a crisis. 

**Replication**

* [Replication](https://en.wikipedia.org/wiki/Replication_(computing)) means sharing information to ensure consistency between redundant resources, such as software or hardware components, to improve reliability, [fault-tolerance](https://en.wikipedia.org/wiki/Fault_tolerance), or accessibility.
* Replication is widely used in many database management systems (DBMS), usually with a primary-replica relationship between the original and the copies. The primary server gets all the updates, which then ripple through to the replica servers. Each replica outputs a message stating that it has received the update successfully, thus allowing the sending of subsequent updates.

## 8. SQL vs. NoSQL

* Relational databases are structured and have predefined schemas like phone books that store phone numbers and addresses. 
* Non-relational databases are unstructured, distributed, and have a dynamic schema like file folders that hold everything from a person’s address and phone number to their Facebook ‘likes’ and online shopping preferences.

**SQL**

* Relational databases store data in rows and columns. Each row contains all the information about one entity and each column contains all the separate data points.
* Some of the most popular relational databases are **MySQL, Oracle, MS SQL Server, SQLite, Postgres, and MariaDB.**

**NoSQL**

Following are the most common types of NoSQL:

1. **Key-Value Stores:** Data is stored in an array of key-value pairs. Well-known key-value stores include Redis, **Voldemort**, and **Dynamo**.
2. **Document Databases:** In these databases, data is stored in documents (instead of rows and columns in a table) and these documents are grouped together in collections. Document databases include the **CouchDB** and **MongoDB**.
3. **Wide-Column Databases:** Instead of ‘tables,’ in columnar databases we have column families, which are containers for rows. Unlike relational databases, we don’t need to know all the columns up front and each row doesn’t have to have the same number of columns. Columnar databases are best suited for analyzing large datasets - big names include **Cassandra** and HBase.
4. **Graph Databases:** These databases are used to store data whose relations are best represented in a graph. Data is saved in graph structures with nodes (entities), properties (information about the entities), and lines (connections between the entities). Examples of graph database include Neo4J and **InfiniteGraph**.

### High level differences between SQL and NoSQL

* **Storage**
* **Schema** - 
  * In SQL, each record conforms to a fixed schema, meaning the columns must be decided and chosen before data entry and each row must have data for each column. 
  * In NoSQL, schemas are dynamic. Columns can be added on the fly and each ‘row’ (or equivalent) doesn’t have to contain data for each ‘column.’
* **Querying:** 
  * SQL databases use SQL (structured query language) for defining and manipulating the data, which is very powerful. 
  * In a NoSQL database, queries are focused on a collection of documents. Sometimes it is also called UnQL (Unstructured Query Language). Different databases have different syntax for using UnQL.
* **Scalability:** 
  * In most common situations, SQL databases are vertically scalable, i.e., by increasing the horsepower (higher Memory, CPU, etc.) of the hardware, which can get very expensive.
  * On the other hand, NoSQL databases are horizontally scalable, meaning we can add more servers easily in our NoSQL database infrastructure to handle a lot of traffic.
* **Reliability or ACID Compliancy (Atomicity, Consistency, Isolation, Durability)**
  * The vast majority of relational databases are ACID compliant. So, when it comes to data reliability and safe guarantee of performing transactions, SQL databases are still the better bet.
  * Most of the NoSQL solutions sacrifice ACID compliance for performance and scalability.

### Reasons to use SQL database

* ACID Compliance
* Data is structured and unchanging 

### Reasons to use NoSQL database

* Storing large volumes of data that often have little to no structure
* Making the most of cloud computing and storage
* Rapid development

## 9. CAP Theorem

CAP theorem states that it is **impossible** for a distributed system to simultaneously provide all three of the following desirable properties:

**Consistency ( C ):** All nodes see the same data at the same time. This means users can read or write from/to any node in the system and will receive the same data.

**Availability ( A ):** Availability means every request received by a non-failing node in the system must result in a response.

**Partition tolerance ( P ):** A partition is a communication break (or a network failure) between any two nodes in the system, i.e., both nodes are up but cannot communicate with each other. A partition-tolerant system continues to operate even if there are partitions in the system. Such a system can sustain any network failure that does not result in the failure of the entire network. Data is sufficiently replicated across combinations of nodes and networks to keep the system up through intermittent outages.

**According to the CAP theorem, any distributed system needs to pick two out of the three properties. The three options are CA, CP, and AP.**

**In the presence of a network partition, a distributed system must choose either Consistency or Availability.** 

## 10. PACELC Theorem

* **ACID** (Atomicity, Consistency, Isolation, Durability) databases, such as RDBMSs like MySQL, Oracle, and Microsoft SQL Server, chose consistency (refuse response if it cannot check with peers)
* **BASE** (Basically Available, Soft-state, Eventually consistent) databases, such as NoSQL databases like MongoDB, Cassandra, and Redis, chose availability (respond with local data without ensuring it is the latest with its peers).
* **One place where the CAP theorem is silent is what happens when there is no network partition?** What choices does a distributed system have when there is no partition?

The PACELC theorem states that in a system that replicates data:

* if there is a partition (‘P’), a distributed system can tradeoff between availability and consistency (i.e., ‘A’ and ‘C’);
* else (‘E’), when the system is running normally in the absence of partitions, the system can tradeoff between latency (‘L’) and consistency (‘C’).

## 11. Consistent Hashing 

While designing a scalable system, the most important aspect is defining how the data will be partitioned and replicated across servers.

**Data partitioning:** It is the process of distributing data across a set of servers.

**Data replication:** It is the process of making multiple copies of data and storing them on different servers.

### What is data partitioning?

The act of distributing data across a set of nodes is called data partitioning. There are two challenges when we try to distribute data:

1. How do we know on which node a particular piece of data will be stored?
2. When we add or remove nodes, how do we know what data will be moved from existing nodes to the new nodes? Additionally, how can we minimize data movement when nodes join or leave?

* A naive approach will use a suitable hash function to map the data key to a number. Then, find the server by applying modulo on this number and the total number of servers. 

* The scheme described in the above diagram solves the problem of finding a server for storing/retrieving the data. But when we add or remove a server, all our existing mappings will be broken. 
* This is because the total number of servers will be changed, which was used to find the actual server storing the data. So to get things working again, we have to **remap all the keys** and move our data based on the new server count

### Consistent Hashing to the rescue

* Distributed systems can use Consistent Hashing to distribute data across nodes. Consistent Hashing maps data to physical nodes and ensures that **only a small set of keys move when servers are added or removed.**
* Consistent Hashing stores the data managed by a distributed system in a ring. Each node in the ring is assigned a range of data. 
* Whenever the system needs to read or write data, the first step it performs is to apply the MD5 hashing algorithm to the key. The output of this hashing algorithm determines within which range the data lies and hence, on which node the data will be stored. Thus, the hash generated from the key tells us the node where the data will be stored.
* Adding and removing nodes in any distributed system is quite common. Existing nodes can die and may need to be decommissioned. Similarly, new nodes may be added to an existing cluster to meet growing demands. To efficiently handle these scenarios, Consistent Hashing makes use of virtual nodes (or Vnodes).

### Virtual Nodes

* Existing nodes can die and may need to be decommissioned. Similarly, new nodes may be added to an existing cluster to meet growing demands. To efficiently handle these scenarios, Consistent Hashing makes use of virtual nodes (or Vnodes).
* Consistent Hashing introduces a new scheme of distributing the tokens to physical nodes. Instead of assigning a single token to a node, the hash range is divided into multiple smaller ranges, and each physical node is assigned several of these smaller ranges. Each of these subranges is considered a Vnode. With Vnodes, instead of a node being responsible for just one token, it is responsible for many tokens (or subranges).

* Practically, Vnodes are **randomly distributed** across the cluster and are generally **non-contiguous** so that no two neighboring Vnodes are assigned to the same physical node or rack. 
* Additionally, nodes do carry replicas of other nodes for fault tolerance. 
* Also, since there can be heterogeneous machines in the clusters, some servers might hold more Vnodes than others. 

### Advantages if Vnodes

1. As Vnodes help spread the load more evenly across the physical nodes on the cluster by dividing the hash ranges into smaller subranges, this speeds up the rebalancing process after adding or removing nodes. When a new node is added, it receives many Vnodes from the existing nodes to maintain a balanced cluster. Similarly, when a node needs to be rebuilt, instead of getting data from a fixed number of replicas, many nodes participate in the rebuild process.
2. Vnodes make it easier to maintain a cluster containing heterogeneous machines. This means, with Vnodes, we can assign a high number of sub-ranges to a powerful server and a lower number of sub-ranges to a less powerful server.
3. In contrast to one big range, since Vnodes help assign smaller ranges to each physical node, this decreases the probability of hotspots.

### Data replication using Consistent Hashing

* To ensure highly availability and durability, Consistent Hashing replicates each data item on multiple N nodes in the system where the value N is equivalent to the replication factor.
* The replication factor is the number of nodes that will receive the copy of the same data. For example, a replication factor of two means there are two copies of each data item, where each copy is stored on a different node.
* Each key is assigned to a **coordinator node** (generally the first node that falls in the hash range), which first stores the data locally and then replicates it to N-1*N*−1 clockwise successor nodes on the ring. This results in each node owning the region on the ring between it and its Nth predecessor. In an **eventually consistent** system, this replication is done asynchronously (in the background).
* In eventually consistent systems, copies of data don’t always have to be identical as long as they are designed to eventually become consistent. In distributed systems, eventual consistency is used to achieve high availability.

### Consistent Hashing use cases

* Amazon’s [Dynamo](https://www.allthingsdistributed.com/2007/10/amazons_dynamo.html) and Apache [Cassandra](https://en.wikipedia.org/wiki/Apache_Cassandra) use Consistent Hashing to distribute and replicate data across nodes.

## 12. Long-Polling vs WebSockets vs Server-Sent Events

* Long-Polling, WebSockets, and Server-Sent Events are popular communication protocols between a client like a web browser and a web server.

### Ajax Polling

* The basic idea is that the client repeatedly polls (or requests) a server for data. The client makes a request and waits for the server to respond with data. If no data is available, an empty response is returned.
* The problem with Polling is that the client has to keep asking the server for any new data. As a result, a lot of responses are empty, creating HTTP overhead.

### HTTP Long-Polling

* This is a variation of the traditional polling technique that allows the server to push information to a client whenever the data is available. 
* If the server does not have any data available for the client, instead of sending an empty response, the server holds the request and waits until some data becomes available.
* Once the data becomes available, a full response is sent to the client. The client then immediately re-request information from the server so that the server will almost always have an available waiting request that it can use to deliver data in response to an event.
* Each Long-Poll request has a timeout. The client has to reconnect periodically after the connection is closed due to timeouts.

### WebSockets

* WebSocket provides [Full duplex](https://en.wikipedia.org/wiki/Duplex_(telecommunications)#Full_duplex) communication channels over a single TCP connection.
* The client establishes a WebSocket connection through a process known as the WebSocket handshake. If the process succeeds, then the server and client can exchange data in both directions at any time.

### Server-Sent Events (SSEs)

* The server uses this connection to send data to a client. If the client wants to send data to the server, it would require the use of another technology/protocol to do so.
* SSEs are best when we need real-time traffic from the server to the client or if the server is generating data in a loop and will be sending multiple events to the client.

## 13. Bloom Filters

* Bloom filters are used to quickly find if an element might be present in a set.
* The Bloom filter data structure tells whether an element **may be in a set, or definitely is not**. The only possible errors are false positives.
* An empty Bloom filter is a bit-array of `m` bits, all set to 0. There are also `k` different hash functions, each of which maps a set element to one of the `m` bit positions.
* To add an element, feed it to the hash functions to get `k` bit positions, and set the bits at these positions to 1.
* To test if an element is in the set, feed it to the hash functions to get k bit positions.
  - If any of the bits at these positions is 0, the element is **definitely not** in the set.
  - If all are 1, then the element **may be** in the set.
* For a fixed error rate, adding a new element and testing for membership are both constant time operations, and a filter with room for ‘n’ elements requires O(n) space.

## 14. Quorum

* In a distributed environment, a quorum is the minimum number of servers on which a distributed operation needs to be performed successfully before declaring the operation’s overall success.
* Suppose a database is replicated on five machines. In that case, quorum refers to the minimum number of machines that perform the same action (commit or abort) for a given transaction in order to decide the final operation for that transaction. So, in a set of 5 machines, three machines form the majority quorum, and if they agree, we will commit that operation. Quorum enforces the consistency requirement needed for distributed operations.
* **What value should we choose for a quorum?** More than half of the number of nodes in the cluster:(*N*/2+1) where *N* is the total number of nodes in the cluster
* Because of this logic, it is recommended to always have an odd number of total nodes in the cluster.
* Quorum is achieved when nodes follow the below protocol: *R* + *W* > *N*, where:
  *N* = nodes in the quorum group
  *W* = minimum write nodes
  *R* = minimum read nodes

* If a distributed system follows *R*+*W*>*N* rule, then every read will see at least one copy of the latest value written. For example, a common configuration could be (N=3, W=2, R=2) to ensure strong consistency. Here are a couple of other examples:
  - (N=3, W=1, R=3): fast write, slow read, not very durable
  - (N=3, W=3, R=1): slow write, fast read, durable
* The following two things should be kept in mind before deciding read/write quorum:
  * R=1 and W=N ⇒ full replication (write-all, read-one): undesirable when servers can be unavailable because writes are not guaranteed to complete.
  * Best performance (throughput/availability) when 1 < r < w < n1<*r*<*w*<*n*, because reads are more frequent than writes in most applications

## 15. Leader and Follower

* Using quorum can lead to another problem, that is, lower availability; at any time, the system needs to ensure that at least a majority of replicas are up and available, otherwise the operation will fail. Quorum is also not sufficient, as in certain failure scenarios, the client can still see inconsistent data.
* Solution: Allow only a single server (called leader) to be responsible for data replication and to coordinate work.
* At any time, one server is elected as the leader. This leader becomes responsible for data replication and can act as the central point for all coordination. 
* The followers only accept writes from the leader and serve as a backup. In case the leader fails, one of the followers can become the leader. 
* In some cases, the follower can serve read requests for load balancing.

## 16. Heartbeat 

* In a distributed environment, work/data is distributed among servers. To efficiently route requests in such a setup, servers need to know what other servers are part of the system. Furthermore, servers should know if other servers are alive and working.
* Each server periodically sends a heartbeat message to a central monitoring server or other servers in the system to show that it is still alive and functioning.

## 17. Checksum 

* In a distributed system, while moving data between components, it is possible that the data fetched from a node may arrive corrupted. This corruption can occur because of faults in a storage device, network, software, etc. How can a distributed system ensure data integrity, so that the client receives an error instead of corrupt data?
* Calculate a checksum and store it with data.
* To calculate a checksum, a cryptographic hash function like MD5, SHA-1, SHA-256, or SHA-512 is used. The hash function takes the input data and produces a string (containing letters and numbers) of fixed length; this string is called the checksum.
* When a system is storing some data, it computes a checksum of the data and stores the checksum with the data. When a client retrieves data, it verifies that the data it received from the server matches the checksum stored. If not, then the client can opt to retrieve that data from another replica.