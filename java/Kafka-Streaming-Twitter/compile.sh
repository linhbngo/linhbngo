#!/bin/bash

mvn compile
mvn package
mvn install assembly:single
