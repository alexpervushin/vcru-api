from vcru_api import VCRUAPISync

with VCRUAPISync() as api:
    recommendations = api.get_recommendations(contentId=1279222)
    comments = api.get_comments(contentId=1279222)
    content = api.get_content(id=962873)
    distribution = api.get_distribution()
    subsite = api.get_subsite()

print(recommendations)
print(comments)
print(content)
print(distribution)
print(subsite)
