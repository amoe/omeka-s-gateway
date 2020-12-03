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
        return r.json()

    def get_page_by_slug(self, slug):
        return next((x for x in self.list_site_pages() if x['o:slug'] == slug), None)

    def get_item_by_title(self, title):
        return next((x for x in self.list_items() if x['o:title'] == title), None)

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

    def list_items(self, site_id):
        final_uri = "{}/api/items?key_identity={}&key_credential={}&site_id={}".format(
            self.install_location,
            self.key_identity,
            self.key_credential,
            site_id
        )
        r = requests.get(final_uri)
        return r.json()

    def create_item_with_media(self, item_payload, path, mime_type):
        endpoint = "{}/api/items?key_identity={}&key_credential={}"
        postdata = {}

        final_uri = endpoint.format(
            self.install_location,
            self.key_identity,
            self.key_credential
        )

        r = requests.post(final_uri, data={'data': json.dumps(item_payload)}, files=[
            ('file[0]', (path, open(path, 'rb'), mime_type))
        ])

        if r.ok:
            return r.json()
            print(r.status_code)
        else:
            raise Exception(r.json()['errors']['error'])



