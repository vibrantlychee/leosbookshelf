from Block import ImageBlock, ParagraphBlock, TableBlock, TitleBlock
import parsers
import caller
import writer

# user inputs constants

MY_NOTION_TOKEN = input("Authentication token: ")
PAGE_ID = parsers.parse_page_url(input("Page ID: "))
NOTION_VERSION = "2022-02-22"

parsed_blocks = []

# get page properties
page = caller.get_page(MY_NOTION_TOKEN, PAGE_ID, NOTION_VERSION)
title_block = parsers.parse_page_results(page)
parsed_blocks.append(title_block)

# get page content
results = caller.get_page_contents(
    token=MY_NOTION_TOKEN,
    page_id=PAGE_ID,
    notion_version=NOTION_VERSION
)

# extract relevant block information
for block in results:
    # table block
    if block["type"] == "table":
        parsed_blocks.append(parsers.parse_table_block(block, MY_NOTION_TOKEN, NOTION_VERSION))
    
    # image block
    elif block["type"] == "image":
        parsed_blocks.append(parsers.parse_image_block(block))

    # text block
    elif block["type"] == "paragraph":
        parsed_blocks.append(parsers.parse_paragraph_block(block))

# write html file
outcome = writer.write_file(parsed_blocks)
if outcome == 0:
    print("Success.")
else:
    print("Failed. Please check Notion page structure.")