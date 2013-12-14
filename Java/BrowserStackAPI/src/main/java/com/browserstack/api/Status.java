package com.browserstack.api;

public class Status {
    private String used_time;
    private String total_available_time;
    private String running_sessions;
    private String sessions_limit;
    private String message;

    public boolean expired() {
        return message != null && message.length() > 0;
    }

    public String getUsed_time() {
        return used_time;
    }

    private void setUsed_time(String used_time) {
        this.used_time = used_time;
    }

    public String getTotal_available_time() {
        return total_available_time;
    }

    private void setTotal_available_time(String total_available_time) {
        this.total_available_time = total_available_time;
    }

    public String getRunning_sessions() {
        return running_sessions;
    }

    private void setRunning_sessions(String running_sessions) {
        this.running_sessions = running_sessions;
    }

    public String getSessions_limit() {
        return sessions_limit;
    }

    private void setSessions_limit(String sessions_limit) {
        this.sessions_limit = sessions_limit;
    }

    public String getMessage() {
        return message;
    }

    private void setMessage(String message) {
        this.message = message;
    }

    @Override
    public String toString() {
        return "Status{" +
                "expired =" + expired() +
                ", used_time='" + used_time + '\'' +
                ", total_available_time='" + total_available_time + '\'' +
                ", running_sessions='" + running_sessions + '\'' +
                ", sessions_limit='" + sessions_limit + '\'' +
                ", message='" + message + '\'' +
                '}';
    }
}
