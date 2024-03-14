
# ***API***
## *Authors*

- [***Brandon Montezuma****](https://github.com/Bmontezuma)

### *Email*:
***brandon.montezuma@atlasschool.com***

# ***Background Context***
[![Watch the Video](https://img.youtube.com/vi/qn08N7Zx0Lw/0.jpg)](https://www.youtube.com/watch?v=qn08N7Zx0Lw&t=2s)

Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.

# ***Resources***
### ***Read or watch***:
- [***Friends don’t let friends program in shell script***](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
- [***What is an API***](https://www.webopedia.com/definitions/api/)
- [***What is an API? In English, please***](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
- [***What is a REST API***](https://www.sitepoint.com/rest-api/)
- [***What are microservices***](https://smartbear.com/learn/api-design/microservices/)
- [***PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry***](https://peps.python.org/pep-0008/)

# ***Learning Objectives***
At the end of this project, you are expected to be able to [***explain to anyone***](https://fs.blog/feynman-learning-technique/), without the help of Google:

## ***General***
- ***What Bash scripting should not be used for?***
```
Bash scripting, while powerful and versatile for many tasks, has limitations and might not be suitable for certain scenarios. Here are some cases where using Bash scripting might not be the best choice:

-Performance-Critical Applications: Bash scripting is interpreted and may not be as efficient as compiled languages like C or C++. For applications requiring high-performance execution, especially those involving heavy computation or processing large datasets, Bash may not offer the speed or optimization needed.

- Cross-Platform Development: Bash scripting is primarily used in Unix-like environments and may not be easily portable to other operating systems like Windows. If cross-platform compatibility is a requirement, using a language like Python or Java with broad platform support would be more appropriate.

- Complex Data Processing: While Bash can handle basic text processing tasks, it may not be the best choice for dealing with complex data structures or formats. Languages like Python or Perl offer more robust libraries and features for parsing, manipulating, and analyzing data.

- Large-Scale Projects: Bash scripts can become difficult to maintain and scale as the complexity of the project increases. For large-scale projects with multiple contributors and intricate requirements, using a more structured language like Python or Ruby, along with proper software engineering practices, would be more suitable.

- Graphical User Interfaces (GUIs): While it's possible to create simple GUI applications using Bash and tools like GTK or Qt, Bash is not well-suited for developing complex or feature-rich GUI applications. Languages like Python or Java with dedicated GUI frameworks offer better support and abstraction for GUI development.

- Tasks Requiring Advanced Data Structures or Algorithms: Bash lacks built-in support for advanced data structures like hash tables or sophisticated algorithms. If your task involves complex data manipulation or algorithmic challenges, using a language like Python, C++, or Java would be more appropriate.

- Long-Running or Daemon Processes: Bash scripting is primarily designed for executing short-lived tasks or shell commands. It's not well-suited for writing long-running processes or daemons. For such tasks, languages like Python or Go, along with proper concurrency management, would be more suitable.

While Bash scripting is incredibly useful for automating system administration tasks, managing file operations, and orchestrating shell commands, it's essential to recognize its limitations and choose the appropriate tool for the job. Depending on the task at hand, other languages or technologies may offer better performance, maintainability, and scalability.
```




- ***What is an API?***
```
An API, or Application Programming Interface, is a set of rules, protocols, and tools that allows different software applications to communicate with each other. It defines the methods and data formats that applications can use to request and exchange information.

APIs are used to enable interaction between various software components, services, or systems, allowing them to work together and share data seamlessly. They abstract away the underlying implementation details and provide a standardized interface for interacting with a software component or service.

There are different types of APIs, including:

- Web APIs: These APIs are accessed over the internet using standard web protocols such as HTTP. Web APIs allow applications to interact with remote servers and access resources such as data, services, or functionality.

- Library APIs: Library APIs provide a set of functions or classes that can be used by software developers to perform specific tasks within their applications. These APIs are typically bundled with software libraries or frameworks and are called directly by the application code.

- Operating System APIs: Operating system APIs provide interfaces for interacting with various components of an operating system, such as file systems, processes, memory management, and hardware devices. They enable developers to write applications that can run on different operating systems while accessing OS-specific features.

APIs can be proprietary, developed and maintained by a single organization, or open, allowing access to anyone and often governed by standards bodies or open-source communities.

In summary, an API serves as an intermediary that allows different software components, services, or systems to communicate and interact with each other, enabling seamless integration and interoperability.
```
-***What is a REST API?***
```
A REST API (Representational State Transfer Application Programming Interface) is a type of web API (Application Programming Interface) that follows the principles of REST architecture. REST is an architectural style for designing networked applications, particularly web services, that relies on a stateless, client-server communication protocol.

Here are the key characteristics of a REST API:

- Statelessness: REST APIs are stateless, meaning each request from a client to the server must contain all the necessary information to understand and process the request. The server does not store any client state between requests. This simplifies server implementation and improves scalability.

- Client-Server Architecture: REST APIs operate based on a client-server architecture, where the client sends requests to the server, and the server processes those requests and sends back appropriate responses. This separation of concerns allows the client and server components to evolve independently.

- Uniform Interface: REST APIs have a uniform interface, which means they use standard HTTP methods (GET, POST, PUT, DELETE) to perform operations on resources. Additionally, resources are identified by unique URLs (Uniform Resource Locators).

- Resource-Based: REST APIs are resource-oriented, where resources are the key abstractions that clients interact with. Each resource is identified by a unique URL, and clients can perform CRUD (Create, Read, Update, Delete) operations on these resources using standard HTTP methods.

- Representation: Resources in a REST API are represented using standard data formats such as JSON (JavaScript Object Notation) or XML (eXtensible Markup Language). Clients and servers communicate by exchanging representations of these resources.

- State Transfer: REST APIs transfer state between the client and server in the form of representations of resources. Clients can request the current state of a resource or modify its state by sending representations of the desired state to the server.

Overall, a REST API provides a standardized, scalable, and flexible way for clients to interact with server-side resources over the internet. It promotes simplicity, interoperability, and scalability, making it a popular choice for building web services and APIs.
```
- ***What are microservices?***
```
Microservices are an architectural style for designing software applications as a collection of small, independently deployable services. Each service in a microservices architecture is built around a specific business capability and can be developed, deployed, and scaled independently of other services.

Here are some key characteristics of microservices:

- Decomposition: In a microservices architecture, the application is decomposed into a set of loosely coupled services, each responsible for a specific domain or business function. These services are typically small and focused, with a well-defined scope.

- Independence: Microservices are designed to be independently deployable and scalable. Each service can be developed, tested, and deployed independently of other services, allowing teams to work on different parts of the application simultaneously.

- Service Boundary: Each microservice has its own boundaries and communicates with other services through well-defined APIs, typically over HTTP/REST or messaging protocols like Kafka or RabbitMQ. This allows services to be developed using different technologies and programming languages.

- Data Management: Microservices can have their own databases, either relational or NoSQL, to manage their data. Each service owns its data and is responsible for maintaining data consistency within its boundary. Services may also communicate with each other to maintain data consistency across service boundaries.

- Autonomy: Microservices promote autonomy and decentralization. Development teams are responsible for the entire lifecycle of their services, including development, testing, deployment, and operations. This allows teams to make decisions independently and move at their own pace.

- Resilience: Microservices are designed to be resilient to failures. Since services are decoupled, failures in one service do not necessarily impact other services. Services can be designed to handle failures gracefully, using techniques like circuit breakers, retries, and fallback mechanisms.

- Scalability: Microservices enable horizontal scalability by allowing individual services to be scaled independently based on demand. Services can be replicated and deployed across multiple servers or containers to handle increased load efficiently.

Overall, microservices offer benefits such as improved agility, scalability, and resilience, making them well-suited for building complex and rapidly evolving software systems. However, they also introduce challenges related to distributed systems, such as network latency, service discovery, and data consistency, which need to be carefully managed.
```
- What is the CSV format
- What is the JSON format
- Pythonic Package and module name style
- Pythonic Class name style
- Pythonic Variable name style
- Pythonic Function name style
- Pythonic Constant name style
- Significance of CapWords or CamelCase in Python

# ***Requirements***
## ***General***
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.X)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Libraries imported in your Python files must be organized in alphabetical order
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- Your code should not be executed when imported (by using if __name__ == "__main__":)


