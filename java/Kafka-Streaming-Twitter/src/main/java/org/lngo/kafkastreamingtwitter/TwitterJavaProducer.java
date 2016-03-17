package org.lngo.kafkastreamingtwitter;

import java.util.Properties;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

import kafka.producer.KeyedMessage;
import kafka.producer.ProducerConfig;

import com.google.common.collect.Lists;
import com.twitter.hbc.ClientBuilder;
import com.twitter.hbc.core.Client;
import com.twitter.hbc.core.Constants;
import com.twitter.hbc.core.endpoint.StatusesFilterEndpoint;
import com.twitter.hbc.core.processor.StringDelimitedProcessor;
import com.twitter.hbc.httpclient.auth.Authentication;
import com.twitter.hbc.httpclient.auth.OAuth1;

import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.*;
import org.apache.hadoop.mapreduce.lib.output.*;
import org.apache.hadoop.util.*;

public class TwitterKafkaProducer extends Configured implements Tool{

	private static final String topic = "twitter-topic";

  
  public static void main(String[] args) {
    try {
      TwitterKafkaProducer.run(args[0], args[1], args[2], args[3]);
    } catch (InterruptedException e) {
      System.out.println(e);
    }
  }

 public int run(String[] args) throws Exception {
    Path inputPath = new Path(args[0]);

    Configuration conf = getConf();
    Job job = new Job(conf, this.getClass().toString());

    FileInputFormat.setInputPaths(job, inputPath);

    job.setJarByClass(TwitterKafkaProducer.class);
    job.setInputFormatClass(TextInputFormat.class);
    job.setMapOutputKeyClass(Text.class);
    job.setMapOutputValueClass(IntWritable.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);

    job.setMapperClass(Map.class);

    return job.waitForCompletion(true) ? 0 : 1;
  }

  public static class Map extends Mapper<Object, Text, Text, IntWritable> {
  
    public void setup(Context context) {
        Configuration config = context.getConfiguration();
        // get the following parameters from -D generic Options:
        String topic = config.get("mapper.word");
        String zookeeper = ;

        word.set(wordstring);
    }

    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
      String line = value.toString();
      StringTokenizer tokenizer = new StringTokenizer(line);
      String consumerKey = tokenizer[0];
      String consumerSecret = tokenizer[1];
			String token = tokenizer[2];
      String secret = tokenizer[3];

  		Properties properties = new Properties();
		  properties.put("metadata.broker.list", "localhost:9092");
		  properties.put("serializer.class", "kafka.serializer.StringEncoder");
		  properties.put("client.id","camus");

		  ProducerConfig producerConfig = new ProducerConfig(properties);
		  kafka.javaapi.producer.Producer<String, String> producer = new kafka.javaapi.producer.Producer<String, String>(producerConfig);

		  BlockingQueue<String> queue = new LinkedBlockingQueue<String>(10000);
		  StatusesFilterEndpoint endpoint = new StatusesFilterEndpoint();
		  // add some track terms
		  endpoint.trackTerms(Lists.newArrayList("twitterapi","#AAPSweep"));

		  Authentication auth = new OAuth1(consumerKey, consumerSecret, token,secret);
		  
      // Create a new BasicClient. By default gzip is enabled.
		  Client client = new ClientBuilder().hosts(Constants.STREAM_HOST)
			    .endpoint(endpoint).authentication(auth)
				  .processor(new StringDelimitedProcessor(queue)).build();

		  // Establish a connection
		  client.connect();

		  // Do whatever needs to be done with messages
		  for (int msgRead = 0; msgRead < 1000; msgRead++) {
			  KeyedMessage<String, String> message = null;
			  try {
				  message = new KeyedMessage<String, String>(topic, queue.take());
			  } catch (InterruptedException e) {
				  e.printStackTrace();
			  }
			  producer.send(message);
		  }
		  producer.close();
		  client.stop();
    }
  }
}
