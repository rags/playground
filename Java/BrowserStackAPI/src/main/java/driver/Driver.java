package driver;

import com.browserstack.api.API;
import com.browserstack.api.APIImpl;
import com.browserstack.api.Browser;
import com.browserstack.api.Worker;

public class Driver {

    public static void main(String[] args) throws Exception {
        API invalidPwd = new APIImpl("r.raghunandan@gmail.com", "invalid_pwd");
        System.out.println("Credentials is valid = " + invalidPwd.isCredentialsValid());

        API api = new APIImpl("r.raghunandan@gmail.com", "Q1MT8e9SDgJ7tAJx7aDr");
        System.out.println("Credentials is valid = " + api.isCredentialsValid());
        System.out.println("API Usage statistics = " + api.status());
        Browser[] browsers = api.browsers();
        Worker worker = api.createWorker(browsers[0], "www.google.com");
        System.out.println("Created " + worker + " on " + browsers[0]);
        System.out.println(api.status(worker));
        System.out.println("Terminating " + worker);
        api.terminate(worker);
        System.out.println(api.status(worker));

    }
}
