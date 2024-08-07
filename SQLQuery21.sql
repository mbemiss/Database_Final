USE [db_theplotspot]
GO
/****** Object:  StoredProcedure [dbo].[get_book_by_id]    Script Date: 6/23/2024 3:45:38 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[get_book_by_id] 
	-- Add the parameters for the stored procedure here
	@book_id bigint = 0, 
	@book_title varchar = 50,
	@book_summary nvarchar = max,
	@book_content nvarchar = max,
	@author_id int = NULL
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	-- The next line just gets all the books
	SELECT * from table_books where @book_id = [book_id]
	-- The next section is for inserting a new book to the table
	--insert into table_books
	--([book_id],[book_title],[book_summary],[book_content],[author_id])
	--values
	--(@book_id, @book_title, @book_summary, @book_content, @author_id)
	
END
