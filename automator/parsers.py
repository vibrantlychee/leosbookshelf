from Block import TableBlock, TextBlock, ImageBlock, ParagraphBlock, TitleBlock
import caller

def parse_page_url(url):
    last_index = 0
    i = 0
    while i < len(url):
        if url[i] == "-":
            last_index = i

        i += 1

    return url[last_index + 1:]

def parse_text_block(block):
    # text content, bold, italics, underline, link
    content = block["text"]["content"]
    bold = block["annotations"]["bold"]
    italics = block["annotations"]["italic"]
    underline = block["annotations"]["underline"]
    link = block["text"]["link"]

    return TextBlock(content, bold, italics, underline, link)


def parse_image_block(block):
    # image content, caption (text)
    url = block["image"]["file"]["url"]
    
    parsed_captions = []
    
    caption_blocks = block["image"]["caption"]
    for b in caption_blocks:
        parsed_captions.append(parse_text_block(b))

    return ImageBlock(url, parsed_captions)

def parse_paragraph_block(block):
    children = []
    
    block = block["paragraph"]["rich_text"]
    for subblock in block:
        children.append(parse_text_block(subblock))

    return ParagraphBlock(children)

def parse_table_block(block, token, notion_version):
    table_contents = caller.get_page_contents(token, block["id"], notion_version)

    attributes = []
    for row in table_contents:
        attributes.append(row["table_row"]["cells"][1][0]["text"]["content"])

    return TableBlock(attributes[0], attributes[1], attributes[2], attributes[3])

def parse_page_results(page):
    title = page["properties"]["title"]["title"][0]["text"]["content"]
    favicon_url = page["icon"]["file"]["url"]
    poster_url = page["cover"]["file"]["url"]

    return TitleBlock(title, favicon_url, poster_url)