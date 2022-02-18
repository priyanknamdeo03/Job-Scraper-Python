<h1 align="center">
  Job Scraper Python
  <br>
</h1> 

> <p align ="center" ><b>We Access the HTML of the webpage and extract useful information/data from it. This technique is called web scraping or web harvesting or web data extraction.</b></p>


## 🚀 Beautiful-Soup Library

- *Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.*
- *Beautiful Soup supports the HTML parser included in Python's standard library, however it also supports many external third party python parsers like lxml parser or html5lib parser.*


## 🧐 Steps involved in web scraping:

1. Requests Library Sends an HTTP request to the URL of the webpage you want to access. The server responds to the request by returning the HTML content of the webpage. For this task, we will use a third-party HTTP library for python-requests.

2. Once we have accessed the HTML content, we are left with the task of parsing the data. Since most of the HTML data is nested, we cannot extract data simply through string processing. One needs a parser which can create a nested/tree structure of the HTML data. There are many HTML parser libraries available but the most advanced one is html5lib.

3. Now, all we need to do is navigating and searching the parse tree that we created, i.e. tree traversal. For this task, we will be using another third-party python library, Beautiful Soup. It is a Python library for pulling data out of HTML and XML files.


## 🛠️ Required third-party libraries

- **`requests :`** Requests library is one of the integral part of Python for making HTTP requests to a specified URL. Whether it be REST APIs or Web Scrapping, requests is must to be learned for proceeding further with these technologies. When one makes a request to a URI, it returns a response.

- **`html5lib :`** html5lib is a pure-python library for parsing HTML. As is implemented by all major web browsers. ... It parses the text the same way as done by the major browsers.

- **`bs4 :`** Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. 

## Implementing bs4 Library And Parsing HTML content

A really nice thing about the BeautifulSoup library is that it is built on the top of the HTML parsing libraries like html5lib, lxml, html.parser, etc. So  BeautifulSoup object and specific parser library can be created at the same time.
```bash
self.soup = bs4.BeautifulSoup(self.response.content, "html.parser") 
```
We create a BeautifulSoup object by passing two arguments:

- **`self.response.content :`** It is the raw HTML content.
- **`html.parser :`** Specifying the HTML parser we want to use.

```bash
git clone https://github.com/priyanknamdeo03/News-Scraper-Python.git
```


<p align="center">
Developed with ❤️ by Priyank 
</p>
