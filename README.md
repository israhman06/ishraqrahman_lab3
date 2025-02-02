# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- team member 1: Ishraq Rahman
- team member 2: Carrie Lei

## Lab Question Answers

Answer for Question 1: 
Restful APIs are scalable because the client and server are separated. Specifically, the server side is stateless, so it doesn't need to store anything across requests. This minimal need for client-server communication is what makes it more scalable and allows for more types of data formats (besides XML) to be used. (Carrie Lei)

Answer for Question 2:
According to the definition of "resources" provided in the AwS article, the resources the mail server is providing to clients is authentication and proxy services for the interal and external client connections. 
(https://learn.microsoft.com/en-us/exchange/architecture/client-access/client-access?view=exchserver-2019)

Answer for Question 3: 
The PUT methond is the REST Method not used in out mail server. We can extend out server to use this method by creating a function that will require a set of three parameters, the url, params or data, and the arguments. 

Answer for Question 4:
API keys are used for many RESTful APIs to identify and authenticate requests. Whenever the client attempts to gain access to resources, it uses unique API key to verify itself. The purpose the API keys serve is providing project authorization. The server assigns a unique generate unique value to a first-time client. 
(https://aws.amazon.com/what-is/restful-api/)
(https://cloud.google.com/endpoints/docs/openapi/when-why-api-key#:~:text=API%20keys%20provide%20project%20authorization,-To%20decide%20which&text=By%20identifying%20the%20calling%20project,or%20enabled%20in%20the%20API.) 
...