from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('books/', views.BookListView.as_view(), name='books'),
	path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
	path('book/<int:pk>/review',views.review_book,name='review-book'),
	path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('searchB/',views.SearchBook, name='searchB'),
    path('searchA', views.SearchAuthor, name='searchA')
]