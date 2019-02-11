set args1=%1
echo %args1%
rm -Force -Recurse _site
docker run --rm --label=jekyll --volume=c:\Users\linhb\Documents\Github\linhbngo.github.io\:/srv/jekyll -it -p 4000:4000 jekyll/jekyll jekyll build --verbose
scp -r _site\* %args1%:~/public_html
