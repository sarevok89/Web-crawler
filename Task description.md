# Python Intern Task - Web Crawler

Clarence got lost while surfing the internet. Help him find his way out by creating a map of
the domain he is on.

Write a function `site_map(url)` that takes a site URL as an argument and creates a mapping
of that domain as a Python dictionary.

The mapping should contain all the accessible pages within that domain. Every entry should
consist of:

* key: URL
* value: dictionary with:
** site title (HTML `<title>` tag)

** links - set of all target URLs within the domain on the page but without anchor links

## Example:

### Confused? Worry not! Here is an example site with a map.

Unzip the `example.zip` file into some directory and enter it.
Run the following command `python3 -m http.server`. You are serving a website now!
Check if everything is okay by visiting the `http://0.0.0.0:8000` URL.

#### If everything works you can run your program with following parameter and verify if it gives the correct answer.

```
>>> site_map('http://0.0.0.0:8000')
```
```
{
'http://0.0.0.0:8000': {
'title': 'Index',
'links': {'http://0.0.0.0:8000/example.html', 'http://0.0.0.0:8000/site.html'}
},
‘'http://0.0.0.0:8000/site.html': {
'title': 'The Site',
'links': {'http://0.0.0.0:8000/site/subsite.html'}
},
'http://0.0.0.0:8000/example.html': {
'title': 'No links here',
'links': set()
},
'http://0.0.0.0:8000/site/subsite.html': {
'title': 'Looping',
'links': {'http://0.0.0.0:8000/site/other_site.html', 'http://0.0.0.0:8000'}
},
'http://0.0.0.0:8000/site/other_site.html': {
'title': 'Looped',
'links': {'http://0.0.0.0:8000/site/subsite.html'}
}
}
```
## Good luck!
