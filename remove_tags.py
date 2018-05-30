# removes html tags from page content source code and returns list of words in content
test = 'Hey <h1>Welcome <b>to</b> me</h1> <p>Yeaaah</p>'

def remove_tags(content):
    start = content.find('<')
    while start != -1:
        end = content.find('>',start)
        content = content[:start] + " " + content[end+1:]
        start = content.find('<')
    return content.split()
