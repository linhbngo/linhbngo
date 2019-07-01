#!/bin/bash
echo $1
rm -Rf _site/*
echo ${PWD}
rm -Rf _site
docker run -v ${PWD}:/srv/jekyll -it jekyll/jekyll jekyll build --verbose
scp -r _site/* $1:~/public_html
