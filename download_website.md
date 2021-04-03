<!--
category: Tools
-->

# Download a Website

In order to download a working copy of a website use the following wget command

```
wget --recursive -p -k www.example.com
```

## How does it work?
```
--recursive
```
Recursivly get all the web pages on the website
```
-p
```
Fix the paths of the links

```
-k
```
Get all the resources: images, css, javascript
