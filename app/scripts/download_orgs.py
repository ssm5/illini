from urllib import request
import json
import pprint
from app.models import Organization
import html2text

pp = pprint.PrettyPrinter()
URL_BASE = 'https://illinois.campuslabs.com/engage/api/discovery/organization/bykey/'

with open('app/organizations.json') as file:
    organizations = json.load(file)
    for i in range(51, 100):
        response = request.urlopen(URL_BASE + organizations['value'][i]['WebsiteKey'])
        org_data = json.loads(response.read().decode())
        pp.pprint(org_data)

        org_object = Organization(name=org_data['name'],
                                  abbr=(org_data['shortName'] if org_data['shortName'] else None),
                                  found_date=org_data['startDate'],
                                  summary=org_data['summary'],
                                  description=html2text.html2text(org_data['description']) if org_data['description'] else org_data['summary'],
                                  is_public=True,
                                  email=org_data['email'],
                                  last_modified=org_data['modifiedOn'],
                                  is_deleted=org_data['deleted']
                                  )
        org_object.save()