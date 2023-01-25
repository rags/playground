Implementation notes
====================
I have exactly 1 day of experience working with golang. I have not coded in golang before I picked up this exercise. I'm afraid the code might not be idomatic golang in terms on coding conventions. I have tried to stick to the coding standards as much as I could based on my limited (googling) knowledge.

## Limitations
Implementation uses a naive session store. In production you would replace this with distributed session store. Also the store only removes session entries on `submit`. If this does not happen there is a change for memory leak for abandoned sessions. This is the main limiation of the implementation.

##Expected output
Events are printed via logs and are visible in the console where the server is run.


Running
====================

## Server

```
cd server
go run .
```

## Test

```
cd server
go test
```