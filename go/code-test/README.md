Ravelin Code Test
=================

#### IMPORTANT: Please do not add your name/handle/email address or any other identifiable information into the code or README, as we anonymise the submissions prior to code review.

## Summary
We need an HTTP server that will accept POST requests (JSON) from multiple clients' websites. Each request forms part of a struct (for that particular visitor) that will be printed to the terminal when the struct is fully complete. 

- Only use the Go standard library for the backend
- Give clear instructions on how to run your code
- Commit your work to a new branch of this repo
- Remember to keep things simple

## Frontend 
A sample implementation of a client website is provided in `client/index.html`. It captures and posts data (to `http://localhost:8080`) every time one of the below events happen. 

  - if the screen resizes, the before and after dimensions
  - copy & paste (for each field)
  - time taken, in seconds, from the first character being typed to submitting the form

### Example JSON Requests
```javascript
{
  "eventType": "copyAndPaste",
  "websiteUrl": "https://ravelin.com",
  "sessionId": "123123-123123-123123123",
  "pasted": true,
  "formId": "inputCardNumber"
}

{
  "eventType": "screenResize",
  "websiteUrl": "https://ravelin.com",
  "sessionId": "123123-123123-123123123",
  "resizeFrom": {
    "width": "1920",
    "height": "1080"
  },
  "resizeTo": {
    "width": "1280",
    "height": "720"
  }
}

{
  "eventType": "timeTaken",
  "websiteUrl": "https://ravelin.com",
  "sessionId": "123123-123123-123123123",
  "timeTaken": 72,
}
```

## Backend (Go)

The backend should:

1. Create a server
2. Accept POST requests in JSON format similar to those specified above
3. Map the JSON requests to relevant sections of a Event struct (specified below)
4. Print the struct for each stage of its construction
5. Also print the struct when it is complete (i.e. when the form has been submitted)

We would like the server to be written to handle multiple requests arriving on
the same session at the same time. We'd also like to see some tests.


### Go Struct
```go
type Event struct {
	WebsiteUrl         string
	SessionId          string
	ResizeFrom         Dimension
	ResizeTo           Dimension
	CopyAndPaste       map[string]bool // map[fieldId]true
	FormCompletionTime int // Seconds
}

type Dimension struct {
	Width  string
	Height string
}
```
