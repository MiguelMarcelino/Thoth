#rest 

# API Design

## Organize API arround resources
- When possible, resource URIs should be based on nouns (the resource) and not verbs (the operations on the resource).
	- `https://adventure-works.com/orders` → Good
	- `https://adventure-works.com/create-order` → Avoid
- Avoid creating APIs that simply mirror the internal structure of a database. 
	- Model entities and the operations that an application can perform on those entities. 
	- A client should not be exposed to the internal implementation.
* Try to keep URIs relatively simple. 
- Once an application has a reference to a resource, it should be possible to use this reference to find items related to that resource.
	- E.g.: /customers/1/orders → Shows a relationship between customers and orders
	- Avoid requiring resource URIs more complex than collection/item/collection.


## API operations in terms of HTTP methods
The common HTTP methods used by most RESTful web APIs are:
- GET retrieves a representation of the resource at the specified URI.
- POST creates/submits a new resource at the specified URI. The body of the request message provides the details of the new resource.
	* Frequently applied to collections  
	- Can be used to submit data for processing without creating a resource
	-   Not guaranteed to be idempotent
- PUT either creates or replaces the resource at the specified URI.  
	- Frequently applied to resources that are individual items
	- If a resource with this URI already exists, it is replaced. Otherwise a new resource is created.
	- Using PUT depends on whether the client can meaningfully assign a URI to a resource before it exists. If not, then use POST  
	- Must be idempotent
- PATCH performs a partial update of a resource.  
	- Can be more efficient than using PUT, because the client only sends the changes. 
	- Can be used to create new resources, if server supports it  
	- Not guaranteed to be idempotent
- DELETE removes the resource at the specified URI. 

**Example**:

| Resource     | POST | GET | PUT | DELETE | 
| ------------------  | ------------------------------- |----------------------------------- |-------------------------------------- |--------------------------------- |
| /customers          | Create a new customer           | Retrieve all customers             | Bulk update customers                 | Remove all customers             | 
| /customers/1        | Error                           | Retrieve detaisl for customer 1    | Update customer 1 details (if exists) | Remove customer 1                | 
| /customers/1/orders | Create new order for customer 1 | Retrieve all orders for customer 1 | Bulk updare orders for customer 1     | Remove all orders for customer 1 |


## Filter and paginate data
* Having the client filter the data is highly innefficient, as it wastes network bandwith. 
	* The API must allow passing filters, which select only a subset of the data.
	* Example filter: `/orders?limit=25&offset=50`
* Consider imposing an upper limit on the number of items returned, to help prevent Denial of Service attacks

## Support partial responses for large binary resources
* In the case of having large binary files, we can supply the response in chunks
* The web API should support the `Accept-Ranges` header for GET requests for large resources
* The client application can submit GET requests that return a subset of a resource, specified as a range of bytes.

## Use `HATEOAS` to enable navigation to related resources
* `HATEOAS` - Hypertext as the Engine of Application State
* System is a finite state machine → Response to each request contains the information necessary to move from one state to another.
	* Each HTTP GET request should return the information necessary to find the resources related to the requested object through hyperlinks included in the response.
	* It shoud describe the operations available on each of these resources.
* Follows the fist [motivation behind REST](motivations-behind-rest.md)
	> It should be possible to navigate the entire set of resources without requiring prior knowledge of the URI scheme.

## Versioning
Goal: enable existing client applications to continue functioning unchanged while allowing new client applications to take advantage of new features and resources.
Versioning Types:
* URI versioning:
	* Add a version number to the URI for each resource.
	* Example: `https://adventure-works.com/v2/customers/3`
	* Disadvantage: server has to support a number of different versions, which is bad for maintainability
* Query string versioning
	* Specify the version of the resource by using a parameter within the query string appended to the HTTP request
	* Example: `https://adventure-works.com/customers/3?version=2`
	* Version parameter should default to a meaningful value if it is omitted by older client applications. (e.g. version `1`)
* Header versioning
	* Implement a custom header which includes the version
	* Requires client to supply the custom header
	* Example header field: `api-version=1`
* Media type versioning
	*  A web serversends the formats it can handle by using an Accept header.
	* The code handling the request is responsible for processing the Accept header.
		* The client application may specify multiple formats in the Accept header.
	* The web server chooses the most appropriate format for the response body.
	* The web server confirms the format of the data in the response body by using the Content-Type header
	* If the Accept header does not specify any known media types, the web server could generate an `HTTP 406` (Not Acceptable) response message or return a message with a default media type.

## Open API Initiative
* OpenAPI Specification comes with a set of opinionated guidelines on how a REST API should be designed. 
	* Advantage: Interoperability
* Promotes a contract-first approach rather than an implementation-first approach
	* Design the API contract (the interface) first and then write code that implements the contract.
* Example: Swagger can generate client libraries or documentation from API contracts.

<hr>

## Sources
- [https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)