#!/bin/bash

rm -Rf _site/*
bundle exec jekyll build --verbose
bundle exec jekyll server --host localhost
