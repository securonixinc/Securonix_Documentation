# Securonix Documentation as Code

![alt text](https://www.securonix.com/wp-content/uploads/2021/12/thumbnail_logo2.jpg "Securonix Logo")

This repository contains the Documentation for Securonix products and services.

## To add new content:

For adding new content to the Documentation base, please follow the steps listed below:

1. If you are accessing the repo for the first time, clone the main branch. If not, skip to step 2.
<pre><code> git clone git@github.com:documentation-securonix/doc.git
</code></pre>
2. If you already have a local repo, pull the recent changes. 
<pre><code> git pull origin main
</code></pre>

### To add documentation in markdown format:

* Add a markdown file in the content/docs path in main branch to add your data. Refer to the [markdown syntax]
* Add necessary content in the markdown file
* Add images/gifs etc in the static folder


[markdown syntax]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

### To add content from Confluence:

* For the confluence page you want to publish in the documentation portal, get the following details:
  * Page id ( securonix.atlassian.net/wiki/spaces/TD/pages/page-id-here/SamplePageName )
  * Your Confluence username ( user@securonix.com)
  * Your API token ( [Link on how to get this] )
* Update this data in the script - PublishConfluence.py. Make sure the converted .md file gets generated in the content/docs path of the repository.
* Run the script

[Link on how to get this]: https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/

3. Push your changes to the main branch
<pre><code>git add .
git commit -m "Add commit message"
git remote add origin git@github.com:documentation-securonix/doc.git
git push -u origin main
</code></pre>
4. After a few minutes, the information you added would be automatically reflected in the Documentation website
