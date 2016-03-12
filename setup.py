from setuptools import setup
setup(
  name = 'flipkart',
  packages = ['flipkart'], # this must be the same as the name above
  version = '0.2',
  description = 'Flipkart affilate api ',
  author = 'Siddharh Jain',
  author_email = 'sidj242@gmail.com',
  url = 'https://github.com/sidj242/flipkart-affiliate-api', # use the URL to the github repo
  download_url = 'https://github.com/sidj242/flipkart-affiliate-api/tarball/0.1', # I'll explain this in a second
  keywords = ['flipkart', 'affilate', 'api'], # arbitrary keywords
  classifiers = [],
  install_requires = ['requests',]
)
