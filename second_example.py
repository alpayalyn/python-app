text = input("Submit your Book name")

book_name_length = len(text)

if book_name_length > 100:
    print("Your book name has more than 100 characters")

else:
    print(f"your book has {book_name_length} characters")
