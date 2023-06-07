from django.db import models
import elasticsearch

# Create a search engine to store the product data.
class ProductSearchEngine(models.Model):
    # Set up the Elastic Search engine or Apache Solr
    engine_type = models.CharField(max_length=20, default="")
    

# Create a model to store the product data.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # Add a ForeignKey to the search engine
    search_engine = models.ForeignKey(ProductSearchEngine, on_delete=models.CASCADE)
    

# Create a model to store the product index data.
class ProductIndex(models.Model):
    # Add a ForeignKey to the product
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Add a field to store the index data
    index_data = models.TextField()
    

# Create a model for the search queries.
class SearchQuery(models.Model):
    query = models.CharField(max_length=100)
    # Add a ForeignKey to the search engine
    search_engine = models.ForeignKey(ProductSearchEngine, on_delete=models.CASCADE)
    # Add a field to store the search results
    results = models.TextField()