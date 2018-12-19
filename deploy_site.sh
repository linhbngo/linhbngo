#!/bin/bash
echo $1
rm -Rf _site/*
bundle exec jekyll build --verbose
scp -r _site/* $1:~/public_html