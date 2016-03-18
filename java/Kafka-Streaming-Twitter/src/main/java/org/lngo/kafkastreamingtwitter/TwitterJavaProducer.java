package org.lngo.kafkastreamingtwitter;

import java.util.*;
import java.util.Properties;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.io.IOException;

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

public class TwitterJavaProducer extends Configured implements Tool{

	private static final String topic = "ElectionTwitter";

  
  public static void main(String[] args) throws Exception {
    int res = ToolRunner.run(new TwitterJavaProducer(), args);
    System.exit(res);
  }

  public int run(String[] args) throws Exception {
    Path inputPath = new Path(args[0]);
    Path outputPath = new Path(args[1]);

    Configuration conf = getConf();
    Job job = new Job(conf, this.getClass().toString());

    FileInputFormat.setInputPaths(job, inputPath);
    FileOutputFormat.setOutputPath(job, outputPath);

    job.setJarByClass(TwitterJavaProducer.class);
 
    job.setInputFormatClass(TextInputFormat.class);
    job.setOutputFormatClass(TextOutputFormat.class);

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
        String topic = config.get("kafka.topic");
        //word.set(wordstring);
    }

    public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
      String line = value.toString();
      System.out.println(line);
      StringTokenizer tokenizer = new StringTokenizer(line);
      String consumerKey = tokenizer.nextToken();
      String consumerSecret = tokenizer.nextToken();
			String token = tokenizer.nextToken();
      String secret = tokenizer.nextToken();

  		Properties properties = new Properties();
		  properties.put("metadata.broker.list", "dsci002.palmetto.clemson.edu:6667,dsci004.palmetto.clemson.edu:6667,dsci006.palmetto.clemson.edu:6667");
		  properties.put("serializer.class", "kafka.serializer.StringEncoder");
		  properties.put("client.id","lngo");

		  ProducerConfig producerConfig = new ProducerConfig(properties);
		  kafka.javaapi.producer.Producer<String, String> producer = new kafka.javaapi.producer.Producer<String, String>(producerConfig);

		  BlockingQueue<String> queue = new LinkedBlockingQueue<String>(10000);
		  StatusesFilterEndpoint endpoint = new StatusesFilterEndpoint();
		  // add some track terms
		  endpoint.trackTerms(Lists.newArrayList("Hillary","Clinton","ImWithHer","Hillary2016","HillaryForAmerica",
                                             "realDonaldTrump","Trump","TrumpNewMedia","Trump2016","MakeAmericaGreatAgain",
                                             "ChooseCruz","tedcruz","CruzCrew","CruzToVictory","Cruz2016",
                                             "BernieSanders","FeelTheBern","Bernie","bernie2016","Sanders",
                                             "Elections2016","Decision2016"));

		  Authentication auth = new OAuth1(consumerKey, consumerSecret, token,secret);
		  
      // Create a new BasicClient. By default gzip is enabled.
		  Client client = new ClientBuilder().hosts(Constants.STREAM_HOST)
			    .endpoint(endpoint).authentication(auth)
				  .processor(new StringDelimitedProcessor(queue)).build();

		  // Establish a connection
		  client.connect();

		  // Do whatever needs to be done with messages
//		  for (int msgRead = 0; msgRead < 1000; msgRead++) {
      int runTime = 0;
      while(runTime == 0){
			  KeyedMessage<String, String> message = null;
			  try {
				  message = new KeyedMessage<String, String>(topic, queue.take());
			  } catch (InterruptedException e) {
				  e.printStackTrace();
			  }
			  producer.send(message);
        if (runTime != 0) break;
		  }
		  producer.close();
		  client.stop();
    }
  }
}
