from unicodedata import category
from oscar.apps.catalogue.categories import create_from_breadcrumbs

categories = [
    'Snowboarding > Snowboard > Burton', 
    'Snowboarding > Board Mounts',
    'Snowboarding > Snowshoes',

    'Skiing > Ski', 
    'Skiing > Ski Poles', 
    'Skiing > Ski Boots', 
    'Skiing > Ski Leash', 

    'Climbing > Climbing Gear',
    'Climbing > Climbing Frames',

    'Snowshoes',
]


for breadcrumb in categories:
    create_from_breadcrumbs(breadcrumb)


print("categories succesfuly added")