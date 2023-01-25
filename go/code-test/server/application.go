package main

import (
    "net/http"
    "encoding/json"
    "log"
)

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

type JsonEvent struct {
    Event
    EventType          string
    Pasted             bool
    TimeTaken          int
    FormId             string
}

type Application struct {
     Session *SessionStore
}

func NewApplication() *Application {
     return &Application{Session: NewSessionStore()}
}


func (app *Application) ProcessEvent(jsonEvent JsonEvent, response http.ResponseWriter, request *http.Request) {
     if jsonEvent.SessionId == "" {
        http.Error(response, "Bad request. SessionId missing", http.StatusBadRequest)
        return
     }
     var event = app.Session.GetOrCreateEvent(jsonEvent.SessionId)
     event.WebsiteUrl = jsonEvent.WebsiteUrl
     event.SessionId = jsonEvent.SessionId
     switch(jsonEvent.EventType) {
     case "copyAndPaste":
          if jsonEvent.FormId == "" {
              http.Error(response, "Bad request. Missing formId for copyAndPaste", http.StatusBadRequest)
          }
          event.CopyAndPaste[jsonEvent.FormId]=jsonEvent.Pasted
     case "screenResize":
          event.ResizeFrom = jsonEvent.ResizeFrom
          event.ResizeTo = jsonEvent.ResizeTo
     case "timeTaken":
          event.FormCompletionTime = jsonEvent.TimeTaken
     default:
          http.Error(response, "Bad request. Unknown eventType", http.StatusBadRequest)
          return
     }
     log.Printf("%+v\n", event)
     switch(jsonEvent.EventType) {
     case "timeTaken":
          app.Session.RemoveEvent(event) // Done so cleanup session
     default:
          app.Session.UpdateEvent(event)
     }
     response.WriteHeader(http.StatusOK)

}

func (app *Application) HttpHandler(response http.ResponseWriter, request *http.Request) {
     if request.URL.Path != "/" {
        http.Error(response, "404 not found.", http.StatusNotFound)
		return
     }
     switch request.Method {
     case "GET":
        http.ServeFile(response, request, "../client/index.html")
     case "POST":
        var event JsonEvent
        err := json.NewDecoder(request.Body).Decode(&event)
        if err!=nil && err.Error() == "EOF" {
            // fetch() in PostEvent() and formTarget.submit() results in 2 posts.
            // This is a BUG in index.html. We handle empty post and reload page
            log.Println("WARN: Received an empty post")
            http.ServeFile(response, request, "../client/index.html")
            return
        }
        app.ProcessEvent(event, response, request)
     default:
        http.Error(response, "Method not implemented", http.StatusNotImplemented)
	}

}