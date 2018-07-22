class Website:
    def __init__(self, host, domain, queries):
        self.host = host
        self.domain = domain
        self.queries = queries

data = input()

website_list = []

while data != "end":
    temp_list = data.split(" | ")
    host = temp_list[0]
    domain = temp_list[1]
    query_list = []
    if len(temp_list) > 2:
        query_list = temp_list[2].split(",")
    website_list.append(Website(host, domain, query_list))
    data = input()
for website in website_list:
    if website.queries == []:
        print(f"https://www.{website.host}.{website.domain}")
    else:
        query_str = "]&[".join(website.queries)
        print(f"https://www.{website.host}.{website.domain}/query?=[{query_str}]")