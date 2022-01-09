import graphene
from graphene_django import DjangoObjectType

from .models import Books

# Here we begin by initializing our model and prescribe the 
# potential models that we want to use in the specified model.

class BooksType(DjangoObjectType):

    class Meta:
        model = Books
        fields = ('id', 'title', 'excerpt')


# We then query the data against the DjangoObjectType,
# and return a graph DS of the BooksType.

class Query(graphene.ObjectType):

    all_books = graphene.List(BooksType)

    # Here we resolve the query to return all books.

    def resolve_all_books(root, info):
        return Books.objects.all()


# Now here we collect certain pieces of information from the graph. 

schema = graphene.Schema(query=Query)