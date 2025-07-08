# GetURLText!

A simple program to get the text from any website

The program utilises the following Python Libraries:

- re
- requests
- PySimpleGUI (sg)
- BeautifulSoup4 (bs4)

On startup, the program will open a maximised window with three buttons. Enabling the user to paste in a website's URL then scrape the text and display it inside a text box, which can then be copied to the clipboard and pasted wherever. This seems to be quite useful to access websites that notoriously include an appalling number of intrusive ads.

One could just install an Adblocker (Such as UBlock Origins or AdBlock) but this would still require the user to physically access the website in the browser. Some websites require the user to "sign-up" to subscritions for access. Looking at you Daily Mail, Times, NYTimes and Daily Express. So far, this works without having to type in the URL in the browser, view an obnoxious amount of Ads or sign-up to a subscription service.

The main part of the program is the get_text function:

- The URL is decoded and parsed into BS4.
- All text contained with the paragraph < p > elements are saved.
- The text is then formatted into lines for visualisation.

- build docker image with tag:$version
```bash
export APP_VERSION=0.1.1
docker build --tag url-text:$APP_VERSION .
```

- run docker image
```bash
docker run -d -p 5000:5000 url-text:$APP_VERSION
```

http://localhost/5000
