package com.browserstack.api;
public class Worker {

    private String id;



    public String getId() {
        return id;
    }

    private void setId(String id) {
        this.id = id;
    }

    @Override
    public String toString() {
        return "Worker{" +
                "id='" + id + '\'' +
                '}';
    }
}
