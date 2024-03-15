
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
```
CSV (Comma-Separated Values) is a file format commonly used for storing tabular data. In a CSV file:

- Data is organized into rows, with each row typically representing a single record.
- Columns within each row are separated by commas (,), though other delimiters such as semicolons or tabs may also be used.
- The first row often contains column headers, describing the data in each column.
- Each subsequent row contains the actual data, with values corresponding to the respective column headers.

CSV files are widely supported across various software platforms and programming languages, making them a popular choice for data interchange and storage. They can be easily created and edited using text editors or spreadsheet software like Microsoft Excel, Google Sheets, or LibreOffice Calc.
```
- What is the JSON format
```
JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. JSON is a text-based format that is language-independent, making it widely used for representing structured data in various programming languages.

In JSON format:

- Data is organized into key-value pairs, similar to associative arrays or dictionaries in programming languages.
- Data structures supported by JSON include objects (unordered collections of key-value pairs), arrays (ordered lists of values), strings, numbers, booleans, and null values.
- Objects are enclosed in curly braces `{}`, with each key-value pair separated by a colon `:` and individual pairs separated by commas `,`.
- Arrays are enclosed in square brackets `[]`, with values separated by commas `,`.
- Strings are enclosed in double quotes `""`, and special characters within strings can be escaped using backslashes `\`.
- JSON data is typically stored in plaintext files with a `.json` extension.

JSON is commonly used for transmitting data between a server and a web application, configuring software settings, and storing structured data in databases or configuration files.
```
- Pythonic Package and module name style
```
In Python, adhering to certain naming conventions for packages and modules helps maintain code readability and consistency across projects. The Python community follows the guidelines outlined in PEP 8, the official style guide for Python code.

Package Names

- Package names should be short, lowercase, and descriptive, with words separated by underscores if needed. Avoid using hyphens or mixed-case names.
- Packages should have unique names to prevent naming conflicts with other packages.
- Choose meaningful names that convey the purpose or functionality of the package.
- Avoid using names that could clash with built-in Python modules or standard library packages.

Example: `my_package`, `data_processing`, `utils`

Module Names

- Module names should also be short, lowercase, and descriptive, following the same conventions as package names.
- Use meaningful names that reflect the contents or functionality of the module.
- Avoid using names that conflict with Python keywords or built-in functions.
- Module names should not start with a digit or contain spaces or special characters.

Example: `data_operations.py`, `file_utils.py`, `math_functions.py`

Importing Modules and Packages

- When importing modules or packages within your code, use absolute imports whenever possible to ensure clarity and avoid ambiguity.
- Avoid wildcard imports (`from module import *`) as they can pollute the namespace and make code harder to understand.
- Group imports according to their source: standard library modules, third-party modules, and local modules.
```
- Pythonic Class name style
```
In Python, adhering to certain naming conventions for class names helps maintain code readability and consistency across projects. These conventions are outlined in PEP 8, the official style guide for Python code.

Class Names

- Class names should be written in CamelCase, starting with an uppercase letter.
- Use descriptive names that clearly indicate the purpose or functionality of the class.
- Avoid using abbreviations unless they are widely understood or significantly reduce the length of the name without sacrificing clarity.
- Class names should not start with an underscore unless they are intended to be private or internal classes.

Example: `MyClass`, `DataProcessor`, `HttpRequestHandler`

Class Naming Conventions

- For classes representing objects, use singular nouns or noun phrases that describe the object being represented.
- For classes representing collections or groups of objects, use plural nouns or noun phrases.
- Avoid using names that conflict with Python keywords or built-in classes.
```
- Pythonic Variable name style
```
In Python, adhering to certain naming conventions for variables helps maintain code readability and consistency across projects. These conventions are outlined in PEP 8, the official style guide for Python code.

Variable Names

- Variable names should be lowercase, with words separated by underscores if needed (snake_case).
- Use descriptive names that clearly indicate the purpose or content of the variable.
- Avoid using single-character names or overly generic names that lack context.
- Variable names should not start with an underscore unless they are intended to be private or internal variables.
- For constant values, use all uppercase letters with words separated by underscores (CONSTANT_CASE).

Example: `count`, `total_price`, `user_input`, `MAX_ITERATIONS`

Naming Conventions

- For variables representing singular objects, use singular nouns or noun phrases.
- For variables representing collections or groups of objects, use plural nouns or noun phrases.
- When naming variables with multiple words, use underscores to separate words for improved readability.

```
- Pythonic Function name style
```
In Python, adhering to certain naming conventions for functions helps maintain code readability and consistency across projects. These conventions are outlined in PEP 8, the official style guide for Python code.

Function Names

- Function names should be lowercase, with words separated by underscores if needed (snake_case).
- Use descriptive names that clearly indicate the purpose or action performed by the function.
- Avoid using single-character names or overly generic names that lack context.
- Function names should not start with an underscore unless they are intended to be private or internal functions.

Example: `calculate_total`, `parse_data`, `generate_report`

Naming Conventions

- For functions performing specific actions or operations, use verbs or verb phrases that describe the action being performed.
- When naming functions with multiple words, use underscores to separate words for improved readability.

```
- Pythonic Constant name style
```
In Python, constants are typically variables whose values should not be changed throughout the execution of a program. Adhering to certain naming conventions for constants helps maintain code readability and consistency across projects. These conventions are outlined in PEP 8, the official style guide for Python code.

Constant Names

- Constant names should be written in uppercase letters, with words separated by underscores if needed (CONSTANT_CASE).
- Use descriptive names that clearly indicate the purpose or meaning of the constant.
- Constants are typically used for values that are fixed and immutable, such as configuration settings or mathematical constants.
- Avoid using single-character names or overly generic names that lack context.

Example: `PI`, `MAX_ATTEMPTS`, `CONFIG_FILE_PATH`

Naming Conventions

- For constants representing singular values or settings, use singular nouns or noun phrases.
- For constants representing collections or groups of values, use plural nouns or noun phrases.
- When naming constants with multiple words, use underscores to separate words for improved readability.

```
- Significance of CapWords or CamelCase in Python
```
In Python, CapWords or CamelCase refers to a naming convention where compound words or phrases are written without spaces, and each word within the phrase begins with an uppercase letter, except for the initial word which starts with a lowercase letter. This convention is commonly used for naming classes, exceptions, and constants in Python code.

Readability and Consistency

- Using CapWords or CamelCase enhances code readability by making names more distinct and easier to recognize. It helps distinguish class names and constants from variables and functions, improving code comprehension.
- Adhering to consistent naming conventions throughout a codebase fosters maintainability and reduces cognitive overhead for developers. It ensures that different parts of the code follow a unified style, making it easier to understand and modify.

Significance in Differentiating Class Names

- In Python, class names are typically written in CamelCase to distinguish them from variables, functions, and other identifiers.
- Using CamelCase for class names helps differentiate them from instances of the class, which are written in lowercase or snake_case. This distinction aids in code clarity and prevents potential naming conflicts.

Conforming to PEP 8 Guidelines

- The use of CapWords or CamelCase for class names is recommended by PEP 8, the official style guide for Python code. Adhering to PEP 8 guidelines promotes code consistency and facilitates collaboration within the Python community.
- While PEP 8 provides recommendations rather than strict rules, following its conventions contributes to writing clean, understandable, and Pythonic code.

In summary, using CapWords or CamelCase in Python serves to improve code readability, maintain consistency, and adhere to best practices outlined by PEP 8. By following these conventions, developers can create more maintainable and accessible Python codebases.
```

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


