# Search engine made as practice for Udacity's Intro to Computer Science course
# Makes use of Depth first search to crawl the web, find all content and links on pages, index them to be looked up, rank the pages by popularity


# Retrieves page from url using urllib library
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

# Find the next link on page
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

# Find all links on the page and return a list of them
def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

# Joins 2 lists and removes duplicates
def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

# Crawls all links starting from a seed page and return an index of all content
def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph


# Add a page associated with all the words on it to index
def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

# Add a keyword or url to the index
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

# Lookup what pages a certain word appears on
def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None
        

# Calculates the ranks of crawled pages by giving a score based on outlinks and inlinks
def compute_ranks(graph):
    d = 0.8 # damping constant
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    inlinks = len(graph[node])
                    newrank += d*ranks[node]/inlinks
            newranks[page] = newrank
        ranks = newranks
    return ranks


# Find the most popular page (by rank) for a keyword in an index
def lucky_search(index, ranks, keyword):
    pages = lookup(index, keyword)
    if not pages:
        return None
    best_page = pages[0]
    for candidate in pages:
        if ranks[candidate] > ranks[best_page]:
            best_page = candidate
    return best_page

# Sorts pages by rank
def quicksort(pages, ranks):
    if not pages or len(pages) <= 1:
        return pages
    else:
        pivot = ranks[pages[0]]
        worse = []
        better = []
        for page in pages[1:]:
            if ranks[page] <= pivot:
                worse.append(page)
            else:
                better.append(page)
        return quicksort(better, ranks) + [pages[0]] + quicksort(worse, ranks)


# returns pages for a keyword ranked by popularity
def ordered_search(index, ranks, keyword):  
    pages = lookup(index,keyword)
    if pages == None:
        return None
    if len(pages) <= 1:
        return pages
    else:
        return quicksort(pages, ranks) 

