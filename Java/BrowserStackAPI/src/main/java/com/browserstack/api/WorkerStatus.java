package com.browserstack.api;

public class WorkerStatus extends Worker {

    enum Status {
        Running, Queued, Terminated;

        public static Status fromSting(String str) {
            return str == null ? Terminated : str.equals("queue") ? Queued : Running;
        }
    }

    private String status;
    private String browser;
    private String browser_version;
    private String browser_url;
    private String os;
    private String os_version;


    public String getBrowser_url() {
        return browser_url;
    }

    private void setBrowser_url(String browser_url) {
        this.browser_url = browser_url;
    }

    public Status getStatus() {
        return Status.fromSting(status);
    }

    private void setStatus(String status) {
        this.status = status;
    }

    public String getBrowser() {
        return browser;
    }

    private void setBrowser(String browser) {
        this.browser = browser;
    }

    public String getBrowser_version() {
        return browser_version;
    }

    private void setBrowser_version(String browser_version) {
        this.browser_version = browser_version;
    }

    public String getOs() {
        return os;
    }

    private void setOs(String os) {
        this.os = os;
    }

    public String getOs_version() {
        return os_version;
    }

    private void setOs_version(String os_version) {
        this.os_version = os_version;
    }

    @Override
    public String toString() {
        return "WorkerStatus{" +
                "[" + getId() +" is '" + getStatus() + '\'' +
                "] browser='" + browser + '\'' +
                ", browser_version='" + browser_version + '\'' +
                ", os='" + os + '\'' +
                ", os_version='" + os_version + '\'' +
                '}';
    }
}
