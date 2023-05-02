import json

fh = open('config.json')                                    # 'File' Object
conf = json.load(fh)                                        # list, [{"domain" : "www.example1.com"...}, {"domain" : "www.example2.com"...}, {"domain" : "www.example3.com"...}]

fh.close()

for website in conf:                                        # dict, {"domain" : "www.example1.com", "database" : {"host" : "localhost1"...}, "plugins" : ["plugin1"...]}
    domain = "domain : " + website["domain"]                # str, "domain : "www.example1.com"
    db_host = "db_host: " + website["database"]["host"]     # str, "db_host : localhost1"
    db_port = "db_port: " + str(website["database"]["port"])# str, "db_port : 27017"
    plugins = "  " + "\n  ".join(website["plugins"])        # str, "plugins :\n  plugin1\n  eslint-plugin-plugin1\n  plugin2\n  plugin3"
    print(f"{domain}\n{db_host}\n{db_port}\n{plugins}\n\n") 