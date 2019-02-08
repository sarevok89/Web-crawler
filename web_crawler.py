from bs4 import BeautifulSoup
from requests.exceptions import MissingSchema, InvalidSchema
import requests
import sys


def fix_local_links(base_url, link):
    """
    Function checking if a provided link is local, if so it adds 'base_url' before it.
    :param link: link which needs to be checked
    :return: concatenates and returns base_url with provided link if 'link' is local, else just returns 'link'
    """

    if link.startswith('/'):
        return base_url + link
    else:
        return link


def site_map(base_url):
    print(__name__)
    """
    def site_map(base_url) - functions generating a site map of a domain as s Python dictionary.

    :param base_url: URL, where You'd like script to start fetching data from, i.e. 'http://www.python.org'
    :return sitemap_dict: dictionary containing site map, where:

    * key: URL
    * value: dictionary with:
    ** site title (HTML `<title>` tag)
    ** links - set of all target URLs within the domain on the page but without anchor links

    """

    # Checks if provided base url doesn't end with '/' and strips it, if it does.
    # It prevents joining base url ending with '/' with local link starting with '/' and having double '/'.

    if base_url.endswith('/'):
        base_url = base_url.strip('/')

    # Set with items that we haven't fetched data from yet

    to_fetch = {base_url}

    # Dictionary where we're going to store all fetched data

    sitemap_dict = {}

    # Loop checking if there are still links that needs to be fetched and if so, serving those links one by one.

    while len(to_fetch) > 0:
        url = to_fetch.pop()

        # Conditional checking if a link is within main domain and if it hasn't been already added to our dictionary.

        if url.startswith(base_url) and url not in sitemap_dict.keys():
            try:
                r = requests.get(url)
                c = r.content
                soup = BeautifulSoup(c, 'html.parser')
                links = set()

                # Creating a set of all items within <a> tag and iterating over this list extracting URLs.
                # Checking/fixing local links and adding processed links to 'links' set.

                for item in soup.find_all('a'):
                    link = item.get('href')
                    link = fix_local_links(base_url, link)
                    if link.startswith(base_url):
                        to_fetch.add(link)
                        links.add(link)

                # Adding new 'key' to our site map dictionary.

                sitemap_dict[url] = {'title': soup.title.text, 'links': links}

            except MissingSchema as e:
                print(e, file=sys.stderr)
                print(f"Invalid URL '{url}'. Please provide valid url, i.e. 'http://domainname.com'", file=sys.stderr)
            except InvalidSchema as e:
                print(e, file=sys.stderr)
                print("It looks like You forgot to add 'http://' prefix.")
            except Exception as e:
                print(e, file=sys.stderr)

    return sitemap_dict


if __name__ == '__main__':
    base_url = input("Please enter a URL (including 'http://') to recieve a site mapping: ")
    print(site_map(base_url))
