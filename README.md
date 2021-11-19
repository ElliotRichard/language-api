# Language Code API

This simple API returns the standardized two-letter codes used for languages, as described in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes).

Hosted: https://language-iso-code-api.herokuapp.com

# Technologies

- Python version: 3.8.12
- Flask-Restful [![PyPI version](https://badge.fury.io/py/Flask-RESTful.svg)](https://badge.fury.io/py/Flask-RESTful)
- BeautifulSoup4 [![PyPI version](https://badge.fury.io/py/beautifulsoup4.svg)](https://badge.fury.io/py/beautifulsoup4)

# Launch ![heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)

Hosted with CI/CD: https://language-iso-code-api.herokuapp.com

# Usage

Right now only one parameter type is available.

```HTML
https://language-iso-code-api.herokuapp.com/language/<language>
```

Example for English you would use

```HTML
https://language-iso-code-api.herokuapp.com/language/English
```

which would then return

```JSON
"EN"
```
