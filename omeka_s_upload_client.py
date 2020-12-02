import omeka_s_gateway
import pprint
import connection_details

site = 'steenvlieg'

def c(s):
    return connection_details.sites[site][s]

gtw = omeka_s_gateway.OmekaSGateway(
    c('install_location'), c('key_identity'), c('key_credential')
)

item_set_id = 5

response = gtw.create_item_with_media(
    item_set_id=item_set_id
)
pprint.pprint(response)
