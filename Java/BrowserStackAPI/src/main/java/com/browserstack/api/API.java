package com.browserstack.api;


import com.google.common.io.CharStreams;
import org.apache.http.HttpResponse;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpDelete;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.client.methods.HttpRequestBase;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.codehaus.jackson.map.ObjectMapper;
import sun.misc.BASE64Encoder;

import java.io.IOException;
import java.io.InputStreamReader;

import static java.util.Arrays.asList;

public class API {

    public static final String BASE_URL = "http://api.browserstack.com/3";
    private String username;
    private String password;


    public API(String username, String password) {
        this.username = username;
        this.password = password;
    }

    public String basicAuth() {
        return "Basic " + new BASE64Encoder().encode((username + ":" + password).getBytes());
    }

    public Browser[] browsers(boolean getAll) {
        return get(BASE_URL + "/browsers?flat=true&all=" + getAll, Browser[].class);
    }

    public WorkerStatus status(Worker worker) {
        return get(BASE_URL + "/worker/" + worker.getId(), WorkerStatus.class);
    }

    public Status status() {
        return get(BASE_URL + "/status", Status.class);
    }

    public void terminate(Worker worker) {
        execute(new HttpDelete(BASE_URL + "/worker/" + worker.getId()));
    }

    private <T> T get(String uri, Class<T> valueType) {
        try {
            HttpGet httpGet = new HttpGet(uri);
            //httpGet.addHeader("Authorization", basicAuth());
            HttpResponse execute = execute(httpGet);
            //if(uri.contains("/worker/"))
            //    System.out.println(CharStreams.toString(new InputStreamReader(execute.getEntity().getContent())));
            return new ObjectMapper().readValue(execute.getEntity().getContent(), valueType);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public boolean isCredentialsValid() {
        HttpResponse response = execute(new HttpGet(BASE_URL));
        return response.getStatusLine().getStatusCode() < 300;
    }

    public Worker createWorker(Browser browser, String url) {
        return createWorker(browser, url, 30, "", "", "");
    }

    //add overloads for optional params
    public Worker createWorker(final Browser browser, final String url, final int timeout, final String name, final String build, final String project) {
        try {
            HttpPost httpPost = new HttpPost(BASE_URL + "/worker");
            httpPost.setEntity(new UrlEncodedFormEntity(asList(new BasicNameValuePair("os", browser.getOs()),
                    new BasicNameValuePair("os_version", browser.getOs_version()),
                    new BasicNameValuePair("browser", browser.getBrowser()),
                    new BasicNameValuePair("device", browser.getDevice()),
                    new BasicNameValuePair("browser_version", browser.getBrowser_version()),
                    new BasicNameValuePair("timeout", String.valueOf(timeout)),
                    new BasicNameValuePair("url", url),
                    new BasicNameValuePair("name", name),
                    new BasicNameValuePair("build", build),
                    new BasicNameValuePair("project", project)
            )));

            HttpResponse response = execute(httpPost);
            //System.out.println(CharStreams.toString(new InputStreamReader(response.getEntity().getContent())));

            return new ObjectMapper().readValue(response.getEntity().getContent(), Worker.class);


        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }


/*

    public String urlEncode(Map<String, String> namevalues) {
        StringBuilder sb = new StringBuilder();
        String[] parts = new String[namevalues.size()];
        int i = 0;
        for (String name : namevalues.keySet()) {

            try {
                parts[i++] = URLEncoder.encode(name, "UTF-8") + '=' + URLEncoder.encode(namevalues.get(name) +"", "UTF-8");
            } catch (UnsupportedEncodingException e) {
                throw new RuntimeException(e);
            }
        }
        return Joiner.on("&").join(parts);
    }
*/


    public Browser[] browsers() {
        return browsers(false);
    }

    private HttpResponse execute(HttpRequestBase request) {
        request.addHeader("Authorization", basicAuth());
        DefaultHttpClient client = new DefaultHttpClient();
        try {
            return client.execute(request);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }



}
