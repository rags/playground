package main

import (
    "net/http"
    "net/http/httptest"
    "testing"
    "io/ioutil"
    "strings"
    "bytes"
    "reflect"
)

func VerifyIndexLoad(t *testing.T, req *http.Request) {
    app := NewApplication()
    res := httptest.NewRecorder()
    app.HttpHandler(res, req)
    result := res.Result()
    if result.StatusCode != http.StatusOK {
       t.Errorf("Expected OK")
    }
    defer result.Body.Close()
    data, err := ioutil.ReadAll(result.Body)
    if err != nil {
        t.Errorf("expected error to be nil got %v", err)
    }
    if !strings.HasPrefix(string(data),"<!DOCTYPE html>")  {
        t.Errorf("expected html file")
    }
}

func TestGet(t *testing.T) {
    req := httptest.NewRequest(http.MethodGet, "/", nil)
    VerifyIndexLoad(t, req)
}

func TestEmptyPost(t *testing.T) {
    req := httptest.NewRequest(http.MethodPost, "/", nil)
    VerifyIndexLoad(t, req)
}


func PostRequest(app *Application, requestBody string) *http.Response {
    req := httptest.NewRequest(http.MethodPost, "/", bytes.NewBufferString(requestBody))
    res := httptest.NewRecorder()
    app.HttpHandler(res, req)
    return res.Result()
}

func EventForSession(app *Application, sessionId string) (event Event, exists bool) {
    value, exists := app.Session.Store[sessionId]
    return value.Value, exists
}

func TestCopyPaste(t *testing.T) {
    app := NewApplication()
    result := PostRequest(app, `{"websiteUrl": "foo", "sessionId": "blahId", "eventType": "copyAndPaste",
                                "pasted": true,  "formId": "inputCardNumber"}`)
    if result.StatusCode != http.StatusOK {
       t.Errorf("Expected OK")
    }
    value, exists := EventForSession(app, "blahId")
    if !exists {
       t.Errorf("expected copypaste even in session store")
    }
    pasted, exists := value.CopyAndPaste["inputCardNumber"]
    if !exists || !pasted {
       t.Errorf("Missing copy paste data")
    }

    //2nd copy paste request
    PostRequest(app, `{"websiteUrl": "foo", "sessionId": "blahId", "eventType": "copyAndPaste",
                                "pasted": false,  "formId": "blahField"}`)
    value, _ = EventForSession(app,"blahId")
    actual := value.CopyAndPaste
    expected := map[string]bool{"inputCardNumber": true, "blahField": false}
    if !reflect.DeepEqual(expected, actual) {
       t.Errorf("Expected %v but got %v", expected, actual)
    }
}

/*
    screenResize -> timeTaken
*/
func TestEventAccumulation(t *testing.T) {
    app := NewApplication()
    result := PostRequest(app, `{"websiteUrl": "foo.com", "sessionId": "666", "eventType": "screenResize",
                               "resizeFrom": {"width": "1920", "height": "1080"},
                               "resizeTo": {"width": "1280", "height": "720"}}`)
    if result.StatusCode != http.StatusOK {
       t.Errorf("Expected OK")
    }
    actual, exists := EventForSession(app, "666")
    if !exists {
       t.Errorf("expected session 666 event in session store")
    }
    expected := Event {WebsiteUrl: "foo.com", SessionId: "666", ResizeFrom: Dimension{"1920", "1080"}, ResizeTo: Dimension{"1280", "720"}}
    if reflect.DeepEqual(actual, expected) {
       t.Errorf("Expected %v but got %v", expected, actual)
    }

    PostRequest(app, `{"websiteUrl": "foo.com", "sessionId": "666", "eventType": "timeTaken", "timeTaken": 72}`)
    _, exists = EventForSession(app, "666")
    if exists {
       t.Errorf("expected session 666 event to be cleared")
    }
}

func TestBadInpu(t *testing.T) {
    app := NewApplication()
    result := PostRequest(app, `{"websiteUrl": "foo.com"}`) // No sessionId
    if result.StatusCode != http.StatusBadRequest {
       t.Errorf("Expected 401")
    }
    result = PostRequest(app, `{"websiteUrl": "foo.com", "sessionId": "blahId"}`) // missing eventType
    if result.StatusCode != http.StatusBadRequest {
       t.Errorf("Expected 401")
    }
    result = PostRequest(app, `{"websiteUrl": "foo.com", "sessionId": "blahId", "eventType": "INVALID"}`) // unknown eventType
    if result.StatusCode != http.StatusBadRequest {
       t.Errorf("Expected 401")
    }

    result = PostRequest(app, `{"websiteUrl": "foo.com", "sessionId": "blahId", "eventType": "copyAndPaste"}`) // missing formId
    if result.StatusCode != http.StatusBadRequest {
       t.Errorf("Expected 401")
    }
}

