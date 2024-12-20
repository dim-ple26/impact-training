class Student:
  def __init__(self):
    self.__Studentid=""
    self.__Studentname=""
    self.__Studentmailid=""
    self.__Studentpassword=""
    
  def setStudentid(self,stuid):
    self.__Studentid=stuid
    
  def getStudentid(self):
    return self.__Studentid
    
  def setStudentname(self,stuname):
    self.__Studentname=stuname
    
  def getStudentname(self):
    return self.__Studentname
    
  def setStudentmailid(self,stumail):
    self.__Studentmailid=stumail
    
  def getStudentmailid(self):
    return self.__Studentmailid
    
  def setStudentid(self,stupass):
    self.__Studentpassword=stupass
    
  def getStudentid(self):
    return self.__Studentpassword


class Book:
  def __init__(self):
    self.book_id=""
    self.book_author=""
    self.book_title=""
    
  def setBookid(self,book_id):
    self.__book_id=book_id
    
  def getBookid(self):
    return self.__book_id
    
  def setBookauthor(self,book_author):
    self.__book_author=book_author
    
  def getBookauthor(self):
    return self.__book_author
    
  def setBooktitle(self,book_title):
    self.__book_title=book_title
    
  def getBooktitle(self):
    return self.__book_title
    
  
class Librarian:
    def __init__(self):
        self.__librarian_id = ""
        self.__librarian_name = ""
        self.__librarian_email = ""
        self.__librarian_password = ""
        self.__issued_books={}
        self.__book_collection={}

    # Setter and Getter for librarian_id
    def setLibrarianid(self, librarian_id):
        self.__librarian_id = librarian_id

    def getLibrarianid(self):
        return self.__librarian_id

    # Setter and Getter for librarian_name
    def setLibrarianname(self, librarian_name):
        self.__librarian_name = librarian_name

    def getLibrarianname(self):
        return self.__librarian_name

    # Setter and Getter for librarian_email
    def setLibrarianemail(self, librarian_email):
        self.__librarian_email = librarian_email

    def getLibrarianemail(self):
        return self.__librarian_email

    # Setter and Getter for librarian_password
    def setLibrarianpassword(self, librarian_password):
        self.__librarian_password = librarian_password

    def getLibrarianpassword(self):
        return self.__librarian_password
        
    def issueBook(self,book,student_id):
      if book.getBookid() not in self.__issued_books:
        self.__issued_books[book.getBookid()]=student_id
        print(f"Book '{book.getBooktitle()}' issued to student {student_id})"
      else:
        print(f"Book is already issued")
        
    def returnBook(self,book):
      if book.getBookid in self.__issued_books:
        del self.__issued_books[book.getBookid()]
        print(f"Book Returned Successfully")
      else:
        print(f"Book issued Successfully")

    def addBook(self,book):
      if book.getBookid() not in self.__book_collection:
        self.__book_collection[book.getBookid()]=book
        print(f"Book added to the library")
      else:
        print(f"Book already exists")
        
    def viewBooks(self):
        if self.__book_collection:
            print("Books available in the library:")
            for book_id, book in self.__book_collection.items():
                print(f"Book ID: {book_id}, Title: {book.getBooktitle()}, Author: {book.getBookauthor()}")
        else:
            print("No books available in the library.")

        


class Login:
  def __init__(self):
    self.credentials={"librarian":{"id":"admin","password":"admin123"}.
      "student":{"id":"student1","password":"student123"
    }
    
  def validate_user(self,role,user_id,password):
    if role in self.credentials and self.credentials[role]["id"]==user_id and self.credentials[role]["password"]== user_pass:
      print(f"Login Successfully for {role}")
      
    else:
      print(f"Invalid user")
      
login_system = Login()
role="librarian"
user_id="admin"
password="admin123"

if login_system.validate_user(role,user_id,password):
  librarian=Librarian()


    book1 = Book()
    book1.setBookid("B001")
    book1.setBooktitle("Python Programming")
    book1.setBookauthor("John Doe")
    book1.setBookgenre("Education")

    book2 = Book()
    book2.setBookid("B002")
    book2.setBooktitle("Data Science Essentials")
    book2.setBookauthor("Jane Smith")
    book2.setBookgenre("Technology")
