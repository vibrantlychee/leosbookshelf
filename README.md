# leosbookshelf
My personal website. Still writing! ✍🏻

https://leosbookshelf.page/

# automator
A bare bones content management system (CMS) I made to automate the publishing 
of content. It is a simple python script that uses the 
[Notion API](https://developers.notion.com/reference/intro) endpoints to grab 
all data of a written post such as the body text, poster image, inline 
images, etc., then writes them into the appropriate HTML, CSS, and image files 
based on the template files (`post.html`, `post.css`) in the `templates` 
directory. These files are then inserted into this repo, and the homepage 
`index.html` is also updated automatically. 

The high level process:
1. I write my post on Notion.
2. I use steps 1-7 set out in the **usage** section below. 
3. I `add`, `commit`, and `push` the changes to this repo to publish new post to 
the web. 

## Usage
In a terminal window whose working director is the highest level of this repo, 
run:
1. `python automator/run.py`
2. Enter Notion authentication token and public URL to Notion page as prompted.
3. Wait for success message. If successful, new files will have been written to 
the local repo. 
5. `add`, `commit`, and `push` changes. 
7. Check https://leosbookshelf.page/ for updates (may take a while for changes 
 to propagate). 

## Documentation
In progress.

- [ ] `automator/Block.py`
- [ ] `automator/caller.py`
- [ ] `automator/parsers.py`
- [ ] `automator/run.py`
- [x] `automator/writer.py`

## (Lack of) Error Handling
Because this is intended for personal use, I have not implemented any error 
handling. All my Notion pages follow the same page structure. 