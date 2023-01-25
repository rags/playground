User surface
------------
The Application can be configured to setup metrics and alarms. The application also allows plugins that can stream 
log records and process it.

| Property          | Type  | Description                 |
|-------------------|-------|-----------------------------|
| metrics           | Array | List of type simple metric  |
| calculatedMetrics | Array | List of calculated metrics  |
| alarms            | Array | List of alarms              |
| rawLogConsumers   | Array | List of adhoc log consumers |

Metrics are of 2 types:

**Simple metrics** - These have the ability to aggregate data over bespoke periods. They have the ability to filter 
out logs based on certain predicates. Currently only 'count' is the aggregate for simple metrics.

| Property | Type   | Description                                                                                                                                                                                                                                                          |
|----------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name     | string | Name of the metric                                                                                                                                                                                                                                                   |
| period   | string | Duration in iso-8601 format. Format is `PnDTnHnMn.nS`. See https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html#parse-java.lang.CharSequence-                                                                                                           |
| type     | string | For now only 'COUNT' is supported. In future this can be other metrics like Latency.                                                                                                                                                                                 |
| filters  | Array  | List of filters. Each filter has these properties 1) `operand` (field name in log file) 2) `value` - A literal value to match 3) `operator` - For now only =~ (regex match) is supported. In future this can be full set of binary operators like ==,!=,>,<,>=,<= etc. |


**Calculated metrics** - These take simple matrics as input and can perform further aggregations like avg, max, sum 
on the input metrics over bespoke time period. 

So if we want to get average of hits/min for a 5 min period, you would setup a simple count metric for 1m period and 
a calculated metric that would take this as input and average the data for a 5 minute period.

| Property     | Type          | Description                                                                                                                       |
|--------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|
| name         | string        | Name of the calculated metric                                                                                                     |
| period       | string        | Duration in iso-8601 format. See `period` for simple metric.                                                                      |
| aggregate    | string        | Only AVG, SUM is currently supported. In future this can be aggregates like MAX, P99, Count etc.                                  |
| inputMetrics | Array<String> | Currently this is list of one dependent metric. In future this can used for metric calculations that involve more then one metric |

**Alarms**

Alarms can be configured for either a simple or a calculated metric. To configure an alarm we need to setup the 
following properties:


| Property           | Type   | Description                                                                                          |
|--------------------|--------|------------------------------------------------------------------------------------------------------|
| name               | string | Name of the alarm                                                                                    |
| metric             | string | Name of the input metric                                                                             |
| threshold          | double | Threshold beyond which alarm can be triggered                                                        |
| dataPointsAlarm    | int    | No of minimum consecutive datapoint above the threshold that will trigger the alarm                  |
| dataPointsRecovery | int    | No of minimum consecutive datapoint less than or equal to threshold to indicate recovery of an alarm |

**Raw log Consumers**

Log consumers can be used to `plugin` any log consumer using its class reference. Log consumers are of type 
`com.datadog.monitoring.processor.api.PeriodicProcessor`. The class specified will be loaded from classpath. Make sure 
you include the your plugin jar in classpath and use fully qualified class name in `type` parameter.

| Property | Type   | Description                                                                                                                                                |
|----------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name     | String | Name of the consumer                                                                                                                                       |
| type     | Array  | Fully qualified name of the implementation class                                                                                                           |
| period   | Array  | Duration in iso-8601 format. Format is `PnDTnHnMn.nS`. See https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html#parse-java.lang.CharSequence- |



Setup
-------

You need java and maven installed to run the code. 

**Compile and run test**
```bash
mvn test
```

**Run the application**
```bash
mvn exec:java -Dexec.cleanupDaemonThreads=false -Dexec.mainClass="com.datadog.monitoring.Main" < sample_csv.txt
```

**Run with custom configuration**

The application uses config packaged with the source code (src/main/resouces/config.json). In case we want to use a 
custom config (without rebuild) 
the config location can be passed with -Dconf=/path/to/config

```bash
mvn exec:java -Dconf=/path/to/config.json -Dexec.cleanupDaemonThreads=false \
    -Dexec.mainClass="com.datadog.monitoring.Main" < sample_csv.txt
```

**Note** that the IntelliJ idea project files are also provided with source. So you can simple use intellij to open the 
project and simply run the Main class with parameters. The project could be imported to other java ide's like eclipse as
a maven project.

Implementation notes
--------------------
The application is designed a pipeline of processors which consume a Stream of data.
A processor can generate a metric, process alarms or can be an adhoc processor. Each log record is distributed to 
leaf (independent) processors in a parallel fashion.

Core classes:
* Config - Pojo that holds deserialized config
* ProcessorFactory - Creates a pipeline of processors through which data will be streamed.
* SimpleMetricProcessor - Creates simple metric from data stream.
* CalcualtedMetricProcesor - Creates calculated metric from a stream of simple metric.
* AlarmProcessor - Monitors a metric and generates alerts.
* SectionLoadLogger - Collects stats for all sections and logs stats for section with max hits. 

**Assumptions/Limitations**

* The implementation assumes single threaded process. All the log processors assume data arrives in serial order.
* The current assumption is that the calculated metric depends on only a single simple metric.
* The output format specified in the problem statement for alerting is `“High traffic generated an
  alert - hits = {value}, triggered at {time}”`. But because of the way the alarms are designed I had to come up 
  with a more generic way of alerting. The messge contains all the relevant information but is worded differently.

Future Improvements
-------------------
This is a naive implementation of a monitoring app. Although the implementation also is biased by current 
requirements, it has been designed with a lot of points of extension.

Here are list of things that can be done on future to make this more mature and feature rich:

* LogDistributor can be replaced with a cloud based stream processing framework like AWS Kinesis.
* Calculated metric in future should be composed of one or more simple or calculated metrics and should support
  metric math (involving more than one metric). We should support deeper chains of metric dependencies and process
  metrics in topological order.
* Plugins are provided as classpath at start. java spi can be used in future to load plugins.
* `type` parameter for simple metric can be extended to support other types of metrics like latency, response size etc.
* `filters` for simple metric should support more comparison operators. Also the list of filters are currently 
  `AND`ed. We need to provide a way to 'OR'. One possibility is to make OR and AND as opertors in a filter expression.
* Right now the output does not adhere to the output format specified in the 
  problem statement. We should externalize all printed messages. One way to do this is via the config file. 


