extensions = []

templates_path = ['_templates']

source_suffix = '.rst'
master_doc = 'index'

project = u'OctopodesKing'
copyright = u'2016, Elmer Yu'
version = '0.1'
release = '0.1'

exclude_patterns = ['_build']
pygments_style = 'sphinx'

html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'OctopodesKingdoc'

latex_elements = {}
latex_documents = [
    ('index', 'OctopodesKing.tex', u'OctopodesKing Documentation',
     u'Elmer Yu', 'manual'),
]

man_pages = [
    ('index', 'octopodesking', u'OctopodesKing Documentation',
     [u'Elmer Yu'], 1)
]

texinfo_documents = [
    ('index', 'OctopodesKing', u'OctopodesKing Documentation',
     u'Elmer Yu', 'OctopodesKing', 'I\'m the king of octopodes',
     'Miscellaneous'),
]
