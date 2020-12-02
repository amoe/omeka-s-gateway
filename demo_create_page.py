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

response = gtw.create_page(
    {
        'o:slug': 'test-page-created-by-script',
        'o:site': site_link,
        'o:title': "A Test Page Created by Script"
    }
)
pprint.pprint(response.json())
