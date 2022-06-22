from Block import *
from datetime import datetime
import os
import urllib.request

def text_block_as_html(block: TextBlock):    
    out = [block.bold, block.italics, block.underline, block.content, block.underline, block.italics, block.bold]

    i = 0
    while i < 3:
        curr = out[i]

        if curr == False:
            out[i] = ""
            out[-(i+1)] = ""
        else:
            if i == 0:
                out[i] = "<b>"
                out[-(i+1)] = "</b>"
            elif i == 1:
                out[i] = "<i>"
                out[-(i+1)] = "</i>"
            elif i == 2:
                out[i] = "<u>"
                out[-(i+1)] = "</u>"

        i += 1

    if block.link == None:
        return "".join(out)
    else:
        return "<a href=\"{}\">".format(dict(block.link)["url"]) + "".join(out) + "</a>"
            


def write_image_block(img: ImageBlock, img_counter: int, filepath: str):
    urllib.request.urlretrieve(img.url, filepath + "pic{}.jpg".format(img_counter))
    
    with open(filepath + "post.html", 'a') as f:
        # write image element
        f.write("""
        <img src="{}" alt="screen-grab" class="pic{}">
            """.format("pic{}.jpg".format(img_counter), img_counter))
        # write caption
        caption_str = ""
        for caption in img.captions:
            caption_str += text_block_as_html(caption)
        f.write("""
        <figcaption class="pic{}"> -- <br> {} <br> --</figcaption>
        """.format(img_counter, caption_str))

def write_paragraph_block(paragraph: ParagraphBlock, filepath: str):
    with open(filepath + "post.html", 'a') as f:
        paragraph_str = ""
        for block in paragraph.children:
            paragraph_str += text_block_as_html(block)
        f.write("""
        <p>
            {}
        </p>
        """.format(paragraph_str))

def str_to_filepath(string):
    out = string.lower().split(' ')
    return "-".join(out)

def write_file(blocks):
    # return 0 for success
    # return 1 for error

    # page properties
    page_title = ""
    favicon_url = ""
    poster_url = ""
    text_title = ""
    text_year = None
    text_artist = ""
    quote = ""
    today = datetime.today()
    publish_date = today.strftime("%B %d, %Y")
    publish_year = today.strftime("%Y")

    # writing order for main body
    main_body_blocks = []

    for block in blocks:
        if type(block) == TitleBlock:
            # extract page properties
            page_title = block.title
            favicon_url = block.favicon_url
            poster_url = block.poster_url
        elif type(block) == TableBlock:
            # grab text_title, year, artist
            text_title = block.name
            text_year = block.year
            text_artist = block.artist
            quote = block.quote
        elif type(block) == ImageBlock or type(block) == ParagraphBlock:
            main_body_blocks.append(block)
        else:
            return 1

    # file writing path
    filepath = str_to_filepath(page_title)
    try:
        os.makedirs(filepath)
    except:
        pass
    filepath = filepath + "/"

    urllib.request.urlretrieve(favicon_url, filepath + "favicon.jpg")
    favicon_url = "favicon.jpg"
    
    # write the html file
    with open(filepath + "post.html", 'w') as f:
        f.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- W: TITLE -->
    <title>{}</title>
    <link rel="icon" href="{}">
    <link rel="stylesheet" href="post.css">
</head>
<body>
    <div class="header">
        <!-- W: TITLE -->
        <p>{}</p>
        <p>--</p>
        <!-- W: PUBLISH DATE -->
        <p>{}</p>
        <p>--</p>
        <!-- W: QUOTE -->
        <p>{}</p>
        <p>--</p>
    </div>

    <div class="text">
        """.format(page_title.lower(), favicon_url, page_title.lower(), publish_date, quote))
    
    img_counter = 1
    for block in main_body_blocks:        
        if type(block) == ImageBlock:
            write_image_block(block, img_counter, filepath)

            img_counter += 1
        elif type(block) == ParagraphBlock:
            write_paragraph_block(block, filepath)

    with open(filepath + "post.html", 'a') as f:
        f.write("""
    </div>

    <div class="footer">
        <p>--</p>
        <!-- W: PUBLISH YEAR -->
        <p>Leo's Bookshelf &copy; {}</p>
    </div>
</body>
</html>
        """.format(publish_year))

    # write the css file
    with open(filepath + "post.css", 'w') as g:
        g.write("""
body {
    font-family: monospace;
    line-height: 0em;
    background-color: rgb(235, 235, 235);
    padding: 0 20%;
    text-align: justify;
}

div.header {
    padding-bottom: 4em;
    width: 100%;
    float: left;
}

div.footer {
    width: 100%;
    float: left;
    padding-top: 4em;
    text-align: right;
}

div.text {
    line-height: 1.1em;
    width: 67%;
    margin-left: auto;
    margin-right: auto;
}

figcaption {
    color: grey;
    text-align: center;
}
        """)
    
    large_window_pic_css = ""
    medium_window_pic_css = ""
    small_window_pic_css = ""
    
    img_counter = 0
    for block in main_body_blocks:
        if type(block) == ImageBlock:
            img_counter += 1
            if img_counter == 1:
                # first pic is centred and block
                large_window_pic_css += """
img.pic1 {
    width: 100%;
    display: block;
    padding: 0 0% 0% 0%;
    margin-left: auto;
    margin-right: auto;
}
                """

                medium_window_pic_css += """
    img.pic1 {
        width: 100%;
        display: block;
        padding: 0 0 2% 0;
        margin-left: auto;
        margin-right: auto;
    }
                """
            elif img_counter > 1 and img_counter % 2 == 0:
                # even numbered pics are float left
                large_window_pic_css += """
img.pic{} {{
    width: 45%;
    float: left;
    padding: 0.5% 2% 0.5% 0%;
}}
                """.format(img_counter)

                medium_window_pic_css += """
    img.pic{} {{
        width: 50%;
        float: left;
        padding: 0.5% 2% 0.5% 0%;
    }}
                """.format(img_counter)

                small_window_pic_css += """
    img.pic{} {{
        width: 100%;
        float: left;
        padding: 2% 0%;
    }}
                """.format(img_counter)
            elif img_counter > 1 and img_counter % 2 != 0:
                # odd numbered pics (except first) are float right
                large_window_pic_css += """
img.pic{} {{
    width: 45%;
    float: right;
    padding: 0.5% 0% 0.5% 2%;
}}
                """.format(img_counter)

                medium_window_pic_css += """
    img.pic{} {{
        width: 50%;
        float: right;
        padding: 0.5% 0% 0.5% 2%;
    }}
                """.format(img_counter)

                small_window_pic_css += """
    img.pic{} {{
        width: 100%;
        float: right;
        padding: 2% 0%;
    }}
                """.format(img_counter)

    with open(filepath + "post.css", 'a') as g:
        g.write(large_window_pic_css)
        g.write("\n")
        g.write("""
@media (max-width: 1000px) {
    body {
        padding: 0 10%;
    }
    div.text {
        width: 100%;
    }
        """)
        g.write(medium_window_pic_css)
        g.write("}\n")
        g.write("""
@media (max-width: 640px) {
        """)
        g.write(small_window_pic_css)
        g.write("}\n")

    # download post poster (cover on Notion)
    urllib.request.urlretrieve(poster_url, filepath + "poster.jpg")
    
    # write links to new page in index.html
    data = None
    with open("index.html", 'r') as f:
        data = f.readlines()
    
    i = 0
    while i < len(data):
        line = data[i]
        if "<!-- ADD HERE -->" in line:
            data.insert(i+1, """
            <div class="post">
                <a href="{}post.html"><img src="{}poster.jpg" alt="{}-poster" class="post"></a>
                <p>{}</p>
            </div>
            """.format(filepath, filepath, filepath[:-1], page_title.lower()))
            break

        i += 1
    
    with open("index.html", 'w') as f:
        f.writelines(data)

    return 0

if __name__ == '__main__':
    pass