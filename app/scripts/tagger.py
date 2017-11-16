from rake_nltk import Rake
from app.models import Organization
import pprint
import html2text


r = Rake()
pp = pprint.PrettyPrinter()

orgs = list(Organization.objects.all()[:5])
for org in orgs:
    text = html2text.html2text(org.name + ". " + org.summary + " " + org.description)
    r.extract_keywords_from_text(text)
    print(text)
    pp.pprint(r.get_ranked_phrases_with_scores())