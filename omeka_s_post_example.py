import requests
import json
import pprint

# Translated from https://forum.omeka.org/t/example-api-usage-using-curl/8083,
# the work of user 'kgoetz'.  Thanks.

# Begin quote:
# > The API permits anonymous access to public resources (i.e., reading non-private
# > data). To perform actions or view data that only logged-in users can access, 
# > you must authenticate your requests.

# > Authentication requires every request to include two additional GET
# > parameters: key_identity and key_credential. An Omeka S user can create API
# > keys in the "API keys" tab of their user edit page.

install_location = None
key_identity = None
key_credential = None

endpoint = "{}/api/items?key_identity={}&key_credential={}"
postdata = {}

final_uri = endpoint.format(install_location, key_identity, key_credential)

predefined_item_set_id = 5

item_payload = {
    "dcterms:title": [
        {
            "property_id": 1, 
            "property_label": "Title",
            "@value": "My snappy title API upload style",
            "type" : "literal"
        }
    ],
    "@type": "o:Item",
    "o:item_set": [
        {"o:id": predefined_item_set_id}
    ],
    "o:media" : [
        {"o:ingester": "upload", "file_index": "0", "o:item": {},
         "dcterms:title": [
             {
                 "property_id": 1,
                 "property_label": "Title",
                 "@value" : "My media upload title",
                 "type" : "literal"
             }
         ]
        }
    ]
}

r = requests.post(final_uri, data={'data': json.dumps(item_payload)}, files=[
    ('file[0]', ('example.png', open('example.png', 'rb'), 'image/png'))
])

if r.ok:
    pprint.pprint(r.json())
    print(r.status_code)
else:
    print(r.content)
