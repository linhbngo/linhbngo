set args1=%1
echo %args1%
echo ${PWD}
rm -Force -Recurse _site
docker run --rm -v "%cd%":/srv/jekyll -it jekyll/jekyll jekyll build --verbose
scp -r _site\about %args1%:~/public_html
scp -r _site\assets %args1%:~/public_html
scp -r _site\blog %args1%:~/public_html
scp -r _site\css %args1%:~/public_html
scp -r _site\docs %args1%:~/public_html
scp -r _site\publications %args1%:~/public_html
scp -r _site\research %args1%:~/public_html
scp -r _site\reveal.js %args1%:~/public_html
scp -r _site\teaching %args1%:~/public_html
scp -r _site\technical %args1%:~/public_html
scp -r _site\feed.xml %args1%:~/public_html
scp -r _site\index.html %args1%:~/public_html
scp -r _site\robots.txt %args1%:~/public_html
scp -r _site\sitemap.xml %args1%:~/public_html
