Python Flipkart Affiliate API
==========================

Flipkarts Product api to get information about any product on flipkart


Features
--------
* Supports item lookup
* Fetch data of Products


Dependencies
--------------
Before you get started, make sure you have:

* Flipkart Affiliate Account [Flipkart](https://affiliate.flipkart.com/) 
* After login there will be "Affiliate Tracking ID" and "Token" in api section

Installation
-------------
     pip install flipkart-api

Usage
-----

Lookup:

     >>> from flipkart.api import FlipkartApi
     >>> flipkart = FlipkartApi(Affiliate_Tracking_ID, Token)
     >>> product = flipkart.lookup(id='MOBEYHZ28ZYTRJYM')
     >>> product.title
     'Apple iPhone 6 Plus'
     >>> product.selling_price
     {'currency': 'INR', 'amount': 65999.0}
     >>> product.brand
     'Apple'
     >>> product.images
     {
     'unknown': 'http://img.fkcdn.com/image/mobile/m/q/k/apple-iphone-6-plus-original-imaeymdqartzwz76.jpeg', 
     '200x200': 'http://img.fkcdn.com/image/mobile/m/q/k/apple-iphone-6-plus-200x200-imaeymdqartzwz76.jpeg', 
     '800x800': 'http://img.fkcdn.com/image/mobile/m/q/k/apple-iphone-6-plus-800x800-imaeymdqartzwz76.jpeg', 
     '400x400': 'http://img.fkcdn.com/image/mobile/m/q/k/apple-iphone-6-plus-400x400-imaeymdqartzwz76.jpeg'
     }


Batch lookup requests are also supported:

     >>> from flipkart.api import FlipkartApi
     >>> flipkart = FlipkartApi(Affiliate_Tracking_ID, Token)
     >>> products = flipkart.lookup(id='MOBEYHZ28ZYTRJYM,BKPE63TH6M2BYPFT,WATE9HBZASZB27NN')
     >>> len(products)
     5
     >>> products[0].productid
     'MOBEYHZ28ZYTRJYM'

Other Attributes of Product are
     
     title,selling_price,url,mrp,description,cod,emi,offers,discount_percentage,brand,instock,images,color,size,productid


