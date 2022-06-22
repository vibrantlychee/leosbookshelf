import requests

def get_page(token, page_id, notion_version):
    results = requests.get(
        "https://api.notion.com/v1/pages/" + page_id,
        headers = {
            "Authorization": token,
            "Notion-Version": notion_version
        }
    ).json()

    return results


def get_page_contents(token, page_id, notion_version):
    results = requests.get(
        "https://api.notion.com/v1/blocks/" + page_id + "/children",
        headers = {
            "Authorization": token,
            "Notion-Version": notion_version
        }
    ).json()["results"]

    return results