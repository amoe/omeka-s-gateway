import omeka_s_gateway
import pprint
import connection_details

site = 'steenvlieg'

def c(s):
    return connection_details.sites[site][s]

gtw = omeka_s_gateway.OmekaSGateway(
    c('install_location'), c('key_identity'), c('key_credential')
)

pages = gtw.list_site_pages()
pprint.pprint(pages)
