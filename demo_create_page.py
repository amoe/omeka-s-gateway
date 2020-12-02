import omeka_s_gateway
import pprint
import connection_details

site = 'steenvlieg'

def c(s):
    return connection_details.sites[site][s]

gtw = omeka_s_gateway.OmekaSGateway(
    c('install_location'), c('key_identity'), c('key_credential')
)

site_link = {
    '@id': 'http://omeka-s.steenvlieg.phys.solasistim.net/api/sites/1',
    'o:id': 1
}

blocks = [
    {'o:attachment': [], 'o:data': {'html': '<p>Some text</p>\r\n'},'o:layout': 'html'}
]

slug = 'test-page-created-by-script'


data = {
    'o:slug': slug,
    'o:site': site_link,
    'o:title': "A Test Page Created by Script",
    'o:block': blocks
}

response = gtw.get_page_by_slug(slug)
if response is None:
    gtw.create_page(data)
else:
    gtw.update_page(response['o:id'], data)

pprint.pprint(gtw.get_page_by_slug(slug))   
