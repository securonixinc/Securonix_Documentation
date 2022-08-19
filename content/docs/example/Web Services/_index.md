---
bookCollapseSection: true
---

# Web Services/REST API
Application Programing Interface (API) allows you to interface between two applications. It provides a communication channel to request for information or perform a task, and receive a response.

SNYPR provides a list of Representational State Transfer (REST) APIs for third-party applications to communicate with SNYPR. Third-party applications can also perform the following:

* Retrieve information from SNYPR, such as activity events, violations alerts, and metrics on incidents created.
* Perform selective actions on incidents, such as changing a workflow, status, or assignee.

REST API is a web service and it uses HTTP or HTTPS protocol to communicate with other applications. Rest API defines a set of functions, such as GET, POST, PUT, DELETE, and POST, that are used by developers to perform requests and receive responses.


{{< hint info >}}
**Note:**  
In the 6.3.1 release, every SNYPR web service requires token based authentication for better security. Earlier, there was an option to disable token based authentication. If you have disabled it in the previous version of SNYPR, you have to add the token authentication for all your SNYPR webservices.
{{< /hint >}}

ou can develop and test REST APIs in any API development tool such as Postman, Swagger, or SOAP UI. In this document, we have used Postman to test the REST APIs.

The following REST APIs are available:

| API Category | Description |
| ------------ | ----------: |
| Auth         | Allows you to generate and validate tokens. It includes the following APIs: \\ Generate Token <br /> Validate Token <br /> Renew Token |