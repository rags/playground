package main

import (
    "net/http"
)

func main() {
     mux := http.NewServeMux()
     app := NewApplication()
     mux.HandleFunc("/", app.HttpHandler)
     http.ListenAndServe(":8080", mux)
}