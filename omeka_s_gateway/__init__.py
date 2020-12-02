import requests
import json
import pprint

class OmekaSGateway(object):
    def __init__(self, install_location, key_identity, key_credential):
        self.install_location = install_location
        self.key_identity = key_identity
        self.key_credential = key_credential

    def get_final_uri(self, endpoint):
        return endpoint.format(
            self.install_location,
            self.key_identity,
            self.key_credential
        )
        
    def create_page(self, data):
        endpoint = "{}/api/site_pages?key_identity={}&key_credential={}"
        item_payload = {
        }
        final_uri = endpoint.format(self.install_location, self.key_identity, self.key_credential)
        r = requests.post(self.get_final_uri(endpoint), json=data)
        return r

    def get_page_by_slug(self, slug):
        return next((x for x in self.list_site_pages() if x['o:slug'] == slug), None)

    def update_page(self, id_, data):
        endpoint = "{}/api/site_pages/{}?key_identity={}&key_credential={}"
        requests.put(
            endpoint.format(self.install_location, id_, self.key_identity, self.key_credential),
            json=data
        )

    def list_site_pages(self):
        final_uri = self.get_final_uri("{}/api/site_pages?key_identity={}&key_credential={}")
        r = requests.get(final_uri)
        return r.json()

    def create_item_with_media(self, *, item_set_id):
        endpoint = "{}/api/items?key_identity={}&key_credential={}"
        postdata = {}

        final_uri = endpoint.format(
            self.install_location,
            self.key_identity,
            self.key_credential
        )

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
            # "o:item_set": [
            #     {"o:id": item_set_id}
            # ],
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
            return r.json()
            print(r.status_code)
        else:
            raise Exception(r.json()['errors']['error'])



