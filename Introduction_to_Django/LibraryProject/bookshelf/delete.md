# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print(list(books))

# Expected Output:
# [] (empty list, assuming no other books exist)