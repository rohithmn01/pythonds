import yaml

with open("/Users/i346327/pythonds/pythonds/03-FileHandling/file1.yaml") as f:
    a = yaml.safe_load(f)
    print(a.keys())
    print(a["credentials"]["users"])