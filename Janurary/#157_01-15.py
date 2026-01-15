## Markdown Link Parser
# 2026-01-15

def parse_link(markdown):
    markdown = markdown.replace("[","")
    markdown = markdown.replace("]","</a>__split__")
    markdown = markdown.replace("(","<a href=\"")
    markdown = markdown.replace(")","\">")
    mrk = markdown.split("__split__")
    txt = mrk[0]
    link = mrk[1]
    mrk = link + txt
    return mrk
