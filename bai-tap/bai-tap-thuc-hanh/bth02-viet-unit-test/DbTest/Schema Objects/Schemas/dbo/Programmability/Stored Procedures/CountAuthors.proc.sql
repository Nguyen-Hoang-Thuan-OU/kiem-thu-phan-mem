create proc [dbo].[CountAuthors]
as
	select COUNT(*)
	from Author
