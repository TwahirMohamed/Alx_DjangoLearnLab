# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected Output:
# <Book: 1984> (or the actual object representation depending on the __str__ method in your model)