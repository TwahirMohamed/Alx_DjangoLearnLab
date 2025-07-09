# Update the book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
updated_book = Book.objects.get(pk=book.pk)
print(updated_book.title)

# Expected Output:
# Nineteen Eighty-Four