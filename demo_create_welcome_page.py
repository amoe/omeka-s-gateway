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

post_slider_blurb = """
<div class="qhs-post-slider-blurb text-center">
  <p>We are a heritage learning project celebrating and promoting the rich
    cultural life of the Lesbian, Gay, Bisexual and Transgender (LGBT)
    community in Brighton & Hove.</p>
</div>
"""

lipsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in ante
ante. Aliquam ultrices mi consequat eros pulvinar, porta ornare odio
consequat. Quisque lectus felis, ultricies nec nibh in, blandit ullamcorper
enim. Nam vel neque non enim rutrum varius. Suspendisse tempor massa elit, ut
tincidunt neque euismod sit amet. Sed fringilla auctor venenatis. Vestibulum eu
consectetur quam. Aenean lorem purus, hendrerit ac odio vel, posuere placerat
enim.
"""

email_form_markup = """
<input class="form-control qhs-input" placeholder="Name"></input>
<input class="form-control qhs-input" placeholder="Email"></input>
<button type="submit" class="btn btn-default qhs-submit">Submit</button>
"""

action_bubble_rows = [
    {'o:attachment': [],
     'o:data': {'color_scheme': 'accent1',
                'content1': lipsum,
                'content2': lipsum,
                'heading1': 'Heading value 1',
                'heading2': 'Heading value 2',
                'hyperlink1': 'http://www.example1.com/',
                'hyperlink2': 'http://www.example2.com/'},
     'o:layout': 'qhsActionBubble'},
    {'o:attachment': [],
     'o:data': {'color_scheme': 'accent2',
                'content1': email_form_markup,
                'content2': lipsum,
                'heading1': 'Heading value 3',
                'heading2': 'Heading value 4',
                'hyperlink1': 'http://www.example3.com/',
                'hyperlink2': 'http://www.example4.com/'},
     'o:layout': 'qhsActionBubble'}
]


blocks = [
    {'o:attachment': [{'o:caption': '',
                       'o:item': {'@id': 'http://omeka-s.steenvlieg.phys.solasistim.net/api/items/15',
                                  'o:id': 15},
                       'o:media': {'@id': 'http://omeka-s.steenvlieg.phys.solasistim.net/api/media/16',
                                   'o:id': 16}}],
     'o:data': {'click_through_url_1': '',
                'click_through_url_2': '',
                'click_through_url_3': ''},
     'o:layout': 'qhsSlider'},
    {'o:attachment': [], 'o:data': {'html': post_slider_blurb},'o:layout': 'html'},
    *action_bubble_rows
]
#
slug = 'welcome-scripted'

data = {
    'o:slug': slug,
    'o:site': site_link,
    'o:title': "Welcome (Scripted)",
    'o:block': blocks
}

response = gtw.get_page_by_slug(slug)
if response is None:
    gtw.create_page(data)
else:
    gtw.update_page(response['o:id'], data)

pprint.pprint(gtw.get_page_by_slug(slug))
    
