package com.browserstack.api;

public interface API {
    Browser[] browsers(boolean getAll);

    WorkerStatus status(Worker worker);

    Status status();

    void terminate(Worker worker);

    boolean isCredentialsValid();

    Worker createWorker(Browser browser, String url);

    Worker createWorker(Browser browser, String url, int timeout, String name, String build, String project);

    Browser[] browsers();
}
