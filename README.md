# Web-crawler
## Check `Task description.md` for more details about the task for this script

### Modules and packages

#### Requests:
```
pip install requests
```

#### BeautifulSoup:
```
pip install bs4
```

### Getting started
```
from bs4 import BeautifulSoup
from requests.exceptions import MissingSchema, InvalidSchema
import requests
import sys
```
### Running script
```
site_map(URL)
```
This function will return You a dictionary object containing:
* key: URL
* value: dictionary with:

  * site title (HTML `<title>` tag)
  * links - set of all target URLs within the domain on the page but without anchor links

### Thanks!
