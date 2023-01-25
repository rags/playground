package main

import (
    "sync"
    "time"
)

/*
 * Represents a naive session store. The value here has a timestamp
 * of the last request from a given session. The timestamp is needed for the
 * LRU cache expiry logic (Not implemented).
 * WARN: Right now this is a ever growing structure (Remove only happens with submit) and a source of memory leak.
 * TODO: Peridically remove expired entries (> Session MaxAge) - i.e make this a LRU map with expiry
 */

type SessionStore struct {
     Store  map[string]SessionValue
     Lock sync.RWMutex
}

type SessionValue struct {
     Value      Event
     LastAccess int64
}

func NewSessionStore() *SessionStore {
     return &SessionStore{Store: make(map[string]SessionValue)}
}

func  (s *SessionStore) GetOrCreateEvent(sessionId string) Event {
     s.Lock.Lock()
     defer s.Lock.Unlock()
     value, exists := s.Store[sessionId]
     if !exists {
         value = SessionValue{LastAccess: time.Now().UnixNano(), Value: Event{CopyAndPaste:make(map[string]bool)}}
         s.Store[sessionId] = value
     }
     return value.Value
}

func  (s *SessionStore) RemoveEvent(event Event) {
     s.Lock.Lock()
     defer s.Lock.Unlock()
     delete(s.Store, event.SessionId)
}

func  (s *SessionStore) UpdateEvent(event Event) {
     s.Lock.Lock()
     defer s.Lock.Unlock()
     s.Store[event.SessionId] = SessionValue{LastAccess: time.Now().UnixNano(), Value: event}
}
