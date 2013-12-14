package com.browserstack.api;
public class Browser {
    private String os;
    private String os_version;
    private String browser;
    private String browser_version;
    private String device;


    public Browser() {
    }

    public Browser(String os, String osVersion, String browser, String browserVersion, String device) {
        this.os = os;
        this.os_version = osVersion;
        this.browser = browser;
        this.browser_version = browserVersion;
        this.device = device;
    }


    public String getOs() {
        return os;
    }

    public void setOs(String os) {
        this.os = os;
    }

    public String getOs_version() {
        return os_version;
    }

    private void setOs_version(String os_version) {
        this.os_version = os_version;
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

    public String getDevice() {
        return device;
    }

    private void setDevice(String device) {
        this.device = device;
    }

    @Override
    public String toString() {
        return "Browser{" +
                "os='" + os + '\'' +
                ", os_version='" + os_version + '\'' +
                ", browser='" + browser + '\'' +
                ", browser_version='" + browser_version + '\'' +
                ", device='" + device + '\'' +
                '}';
    }
}