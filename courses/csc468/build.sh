#!/bin/bash
 
 rm -Rf _build
source activate jupyter-book
jupyter-book build .

git add .
git commit -m 'csc468'
git push

if [[ $1 == "site" ]]
then
  rsync -a _build/html/* lngo@cs.wcupa.edu:~/public_html/csc468/
fi
