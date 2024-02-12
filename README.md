# Introduction to Django Web Store Project
**Description**

This repository serves as an introductory project for a web store, built using Django, Oscar, and Wagtail frameworks. 
The project is designed to showcase the fundamental capabilities of each of these frameworks within the context of an online store.

**1 - Clone repo**
  1. Make new folder and open it in console
```
mkdir shop
cd shop
```
  2. Clone this repository
```
git clone https://github.com/serikzhant/shop .
```
  3. Make virtual environment and activate it
```
virtualenv venv
.\venv\Scripts\activate
```
  4. Install all required packages
```
pip install -r requirements.txt
```
  5. Create superuser
```
py .\manage.py createsuperuser
```
  6. Run shop server
```
py .\manage.py runserver    
```
**2 - Create your own shop**

_Despite the fact that the oscar framework is based on a django, it has a lot of useful features out of the box, and therefore the launch of project is different._
  1. Make new working directory
```
mkdir shop
cd shop
```
  2. Create and activate virtual environment to isolate dependencies
```
virtualenv venv
.\venv\Scripts\activate
```
  3. Install required packages
```
pip install django-oscar[sorl-thumbnail]
pip install wagtail
pip install setuptools
```
  4. Initiate base _wagtail_ structure for your project
```
wagtail start shop .
```
  5. Delete "home" and "search" folders.
  
  6. Remove "home" and "search" apps from INSTALLED_APPS in shop/settings/base.py file
![image](https://github.com/serikzhant/shop/assets/138390123/16e2efce-298b-4969-a44b-214c1e149a98)

  7. In shop/urls.py delete search import and it's view
![image](https://github.com/serikzhant/shop/assets/138390123/340480b6-afb8-488f-bf11-395caf1e7ea7)

  8. In shop/settings/base.py file import default oscar settings:
```
from oscar.defaults import *
```
![image](https://github.com/serikzhant/shop/assets/138390123/f0dfcf78-0306-4945-ad76-f02fb01f4656)
  9. In the same file, extend templates settings with oscar context processors:
```
"oscar.apps.search.context_processors.search_form",
"oscar.apps.checkout.context_processors.checkout",
"oscar.core.context_processors.metadata",
```
![image](https://github.com/serikzhant/shop/assets/138390123/e40312a6-b897-4559-becb-269004bfc75d)


  10. Include oscar apps to INSTALLED_APPS list:
```
    "django.contrib.sites",
    "django.contrib.flatpages",
    "oscar.config.Shop",
    "oscar.apps.analytics.apps.AnalyticsConfig",
    "oscar.apps.checkout.apps.CheckoutConfig",
    "oscar.apps.address.apps.AddressConfig",
    "oscar.apps.shipping.apps.ShippingConfig",
    "oscar.apps.catalogue.apps.CatalogueConfig",
    "oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig",
    "oscar.apps.communication.apps.CommunicationConfig",
    "oscar.apps.partner.apps.PartnerConfig",
    "oscar.apps.basket.apps.BasketConfig",
    "oscar.apps.payment.apps.PaymentConfig",
    "oscar.apps.offer.apps.OfferConfig",
    "oscar.apps.order.apps.OrderConfig",
    "oscar.apps.customer.apps.CustomerConfig",
    "oscar.apps.search.apps.SearchConfig",
    "oscar.apps.voucher.apps.VoucherConfig",
    "oscar.apps.wishlists.apps.WishlistsConfig",
```
![image](https://github.com/serikzhant/shop/assets/138390123/ef6cb540-1d5a-41b3-a7d0-a2b759f23ca0)

```
    # dashboard apps
    "oscar.apps.dashboard.apps.DashboardConfig",
    "oscar.apps.dashboard.reports.apps.ReportsDashboardConfig",
    "oscar.apps.dashboard.users.apps.UsersDashboardConfig",
    "oscar.apps.dashboard.orders.apps.OrdersDashboardConfig",
    "oscar.apps.dashboard.catalogue.apps.CatalogueDashboardConfig",
    "oscar.apps.dashboard.offers.apps.OffersDashboardConfig",
    "oscar.apps.dashboard.partners.apps.PartnersDashboardConfig",
    "oscar.apps.dashboard.pages.apps.PagesDashboardConfig",
    "oscar.apps.dashboard.ranges.apps.RangesDashboardConfig",
    "oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig",
    "oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig",
    "oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig",
    "oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig",
```
![image](https://github.com/serikzhant/shop/assets/138390123/eb793afc-d2a8-4f11-b1fb-a84865c663b8)

```
    # 3rd-party apps that oscar depends on
    "widget_tweaks",
    "haystack",
    "treebeard",
    "sorl.thumbnail",
    "django_tables2",
```
![image](https://github.com/serikzhant/shop/assets/138390123/652b5b59-876c-49c1-9f2b-356250a32670)

  11. Set SIDE_ID
```
SITE_ID = 1
```
![image](https://github.com/serikzhant/shop/assets/138390123/1979b00f-039c-4fc1-abdf-205862927eb0)

  12. Add oscar middleware
```
    "oscar.apps.basket.middleware.BasketMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
```
![image](https://github.com/serikzhant/shop/assets/138390123/66ca635f-a5d5-48e1-b666-e48d531a78c0)

  13. Set up simple haystack connection:
```
HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.simple_backend.SimpleEngine",
    }
}
```
![image](https://github.com/serikzhant/shop/assets/138390123/35368d31-19be-4fcb-bc94-bf8768e9448a)

  14. In the shop/urls.py include oscar's urls
```
from django.apps import apps

path('', include(apps.get_app_config('oscar').urls[0])),
```
![image](https://github.com/serikzhant/shop/assets/138390123/ae196352-2deb-482d-b09f-23d3b8d4ce60)

  15. Set DEFAULT_AUTO_FIELD in base.py file
```
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
```
![image](https://github.com/serikzhant/shop/assets/138390123/3a6ded07-cfc5-4460-928d-655e6858e154)

  16. Apply all migrations: address, admin, analytics, auth, basket, catalogue, communication, contenttypes, customer, flatpages, offer, order, partner, payment, reviews, 
sessions, shipping, sites, taggit, thumbnail, voucher, wagtailadmin, wagtailcore, wagtaildocs, wagtailembeds, wagtailforms, wagtailimages, wagtailredirects, wagtailsearch, wagtailusers, wishlists
```
py .\manage.py migrate
```

  17. Create superuser
```
py .\manage.py createsuperuser
```
![image](https://github.com/serikzhant/shop/assets/138390123/2ab097b1-75f1-4acb-92f5-0d9d097c04b3)

  18. Run server
```
py .\manage.py runserver
```

If you didn't specify the email address while creating the superuser log in via http://127.0.0.1:8000/admin with your username and password
After that, you can navigate to dashboard and manage the site
