-- SQL
SELECT * FROM playlist_track AS A
ORDER BY PlaylistId  DESC LIMIT 5;

SELECT * FROM tracks as 'B' 
ORDER by TrackId ASC LIMIT 5;

SELECT PlaylistId, Name FROM playlist_track 
JOIN tracks on playlist_track.TrackId =tracks.TrackId
ORDER BY PlaylistId desc LIMIT 10;

SELECT PlaylistId, name FROM playlist_track
JOIN tracks ON playlist_track.TrackId = tracks.TrackId
WHERE PlaylistId = 10
ORDER BY name desc LIMIT 5;

SELECT count(*) FROM tracks
INNER JOIN artists
ON tracks.Composer = artists. Name;

SELECT count(*) FROM tracks LEFT JOIN artists
on tracks.Composer = artists.Name;

SELECT InvoiceLineId, InvoiceId
FROM invoice_items
ORDER BY InvoiceId
LIMIT 5;

SELECT InvoiceId, CustomerId FROM invoices
ORDER BY InvoiceId asc LIMIT 5;

SELECT it.InvoiceLineId, i.InvoiceId
FROM invoice_items it
JOIN invoices i
ON it.InvoiceId = i.InvoiceId
ORDER BY i.InvoiceId DESC
LIMIT 5;

SELECT InvoiceId, CustomerId FROM invoices
order by InvoiceId desc LIMIT 5;

SELECT InvoiceLineId, InvoiceId, CustomerId FROM invoice_items it
JOIN invoices i on  it.InvoiceId = i.InvoiceId
ORDER by InvoiceId desc LIMIT 5;

SELECT i.CustomerId, COUNT(*)
FROM invoice_items it
JOIN invoices i
ON it.InvoiceId = i.InvoiceId
GROUP BY i.CustomerId
ORDER BY i.CustomerId 
LIMIT 5;