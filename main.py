from index.IndexFile import index


if __name__=="__main__":
    IndexWeb=index("crawled_urls.json")
    IndexWeb.create_reversed_index()
    IndexWeb.stat_export()
