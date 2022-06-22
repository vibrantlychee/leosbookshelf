# leosbookshelf
My personal website.

# automator
A bare bones content management system (CMS) I made to automate the publishing of content. The high level process:
1. I write my post on Notion.
2. I wrote simple python scripts to use the Notion API to export Notion posts into appropriate HTML, CSS, and image files for this website. It also automatically updates `index.html`.
3. I `add`, `commit`, and `push` the changes to this repo to publish new post to the web. 

## Usage
In a terminal window whose working director is the highest level of this repo, run:
1. `python automator/run.py`
2. Enter Notion authentication token and public URL to Notion page as prompted.
3. Wait for success message. If successful, new files will have been written to this repo. 
5. `add`, `commit`, and `push` changes. 
6. Wait for changes to propagate. 
7. Check https://leosbookshelf.page/ for changes.

