---
weight: 1
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookCollapseSection: false
# bookComments: false
# bookSearchExclude: false
---

# REST API Categories
This section includes a list of REST API categories and requests. Before running any APIs, you must generate a token using Generate Token API. Token is used for authentication. Once your token is expired, you must generate it.

## Auth
Generate and validate authentication tokens.

{{< expand "Generate Token" "..." >}}
## Markdown content
Request type: GET
```py3
# Code block
"{{url}}/ws/token/generate"
```

To use a REST API with SNYPR, you must be authenticated. You can use the Generate Token API to authenticate and obtain a token, which you must then use with every API request.


Base URL |  | 
--- | --- | 
*{{url}}* | It must be in the following format:  https://<hostname or IPaddress>/Snypr |
 
 ### Request
```py3
# Code block
curl --request GET \ 
--url 'http://{{url}}/ws/token/generate' \ 
--header 'password: {{password}}' \ 
--header 'username: {{username}}' \ 
--header 'validity: 365' 
```
### Sample Response
```py3
530bf219-5360-41d3-81d1-8b4d6f75956d
```

{{< /expand >}}

