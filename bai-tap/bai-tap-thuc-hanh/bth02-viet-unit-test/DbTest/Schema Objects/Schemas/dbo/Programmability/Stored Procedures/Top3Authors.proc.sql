create proc [dbo].[Top3Authors]
as
	select top 3 *
	from Author
