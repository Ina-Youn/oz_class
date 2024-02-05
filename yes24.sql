-- USE yes24;

-- SELECT title, author FROM books;
-- SELECT * FROM books WHERE rating >= 8.0;
-- SELECT title, review FROM books WHERE review >= 100 ORDER BY review DESC;
-- SELECT title, price FROM books WHERE price < 20000;
-- SELECT * FROM books WHERE ranking_weeks >= 4 ORDER BY ranking_weeks DESC;
-- SELECT * FROM books WHERE author = '최태성 저'
-- SELECT * FROM books WHERE publisher = '유노북스'

-- SELECT author, COUNT(*) FROM Books GROUP BY author;
-- SELECT publisher, COUNT(*) AS publishing_count FROM books GROUP BY publisher;
-- SELECT author, AVG(rating) AS avg_rating FROM Books GROUP BY author ORDER BY avg_rating DESC LIMIT 1;
-- SELECT title, author FROM Books WHERE ranking = 1;
-- SELECT title, sales, review FROM Books ORDER BY sales DESC, review DESC LIMIT 10;
-- SELECT title, publishing FROM Books ORDER BY publishing DESC LIMIT 5;

-- SELECT author, AVG(rating) FROM Books GROUP BY author;
-- SELECT publishing, COUNT(*) FROM Books GROUP BY publishing;
-- SELECT title, AVG(price) FROM Books GROUP BY title;
-- SELECT title, review FROM Books ORDER BY review DESC LIMIT 5;
-- SELECT ranking, AVG(review) FROM Books GROUP BY ranking;

-- SELECT title, rating FROM Books WHERE rating > (SELECT AVG(rating) FROM Books);
-- SELECT title, price FROM Books WHERE price > (SELECT AVG(price) FROM Books);
-- SELECT title, review FROM Books WHERE review > (SELECT MAX(review) FROM Books);
-- SELECT title, sales FROM Books WHERE sales < (SELECT AVG(sales) FROM Books);
-- SELECT title, publishing FROM Books WHERE author = (SELECT author FROM Books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1) ORDER BY publishing DESC LIMIT 1;

-- UPDATE Books SET price = 30000 WHERE title = 'New Book Title';
-- UPDATE Books SET title = 'Updated Title' WHERE author = '홍길동';
-- DELETE FROM Books WHERE sales = (SELECT MIN(sales) FROM Books);
-- UPDATE Books SET rating = rating + 1 WHERE publisher = '민음사';

-- SELECT author, AVG(rating) as avg_rating, AVG(sales) as avg_sales FROM Books GROUP BY author;
-- SELECT publishing, AVG(price) as avg_price FROM Books GROUP BY publishing;
-- SELECT publisher, COUNT(*) as num_books, AVG(review) as avg_review FROM Books GROUP BY publisher;
-- SELECT ranking, AVG(sales) as avg_sales FROM Books GROUP BY ranking;
-- SELECT price, AVG(review) as avg_review, AVG(rating) as avg_rating FROM Books GROUP BY price;

-- SELECT publisher, author, AVG(sales) as avg_sales
-- FROM Books
-- GROUP BY publisher, author
-- ORDER BY publisher, avg_sales DESC

-- SELECT title, review, price
-- FROM Books
-- WHERE review > (SELECT AVG(review) FROM Books) AND price < (SELECT AVG(price) FROM Books);

-- SELECT author, COUNT(DISTINCT title) as num_books
-- FROM Books
-- GROUP BY author
-- ORDER BY num_books DESC
-- LIMIT 1;

-- SELECT author, title, MAX(sales) as max_sales
-- FROM Books
-- GROUP BY author;

-- SELECT YEAR(publishing) as year, COUNT(*) as num_books, AVG(price) as avg_price
-- FROM Books
-- GROUP BY year;

-- SELECT publisher, MAX(rating) - MIN(rating) as rating_difference
-- FROM Books
-- GROUP BY publisher
-- ORDER BY rating_difference DESC
-- LIMIT 1;

-- SELECT title, rating / sales as ratio
-- FROM Books
-- WHERE author = '특정 저자'
-- ORDER BY ratio DESC
-- LIMIT 1;
