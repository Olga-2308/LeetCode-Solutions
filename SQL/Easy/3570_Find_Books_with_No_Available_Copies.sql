SELECT l.book_id, l.title, l.author, l.genre, l.publication_year, 
    SUM(CASE WHEN b.return_date IS NULL THEN 1 ELSE 0 END) AS current_borrowers
FROM library_books l
RIGHT JOIN borrowing_records b ON l.book_id = b.book_id
GROUP BY l.book_id
HAVING current_borrowers = MAX(l.total_copies)
ORDER BY current_borrowers DESC, l.title ASC;