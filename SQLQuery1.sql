-- ================================================
-- Template generated from Template Explorer using:
-- Create Procedure (New Menu).SQL
--
-- Use the Specify Values for Template Parameters 
-- command (Ctrl-Shift-M) to fill in the parameter 
-- values below.
--
-- This block of comments will not be included in
-- the definition of the procedure.
-- ================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Mike Bemiss
-- Create date: 6/23/2024
-- Description:	This procedure is to get a book by its ID.
-- =============================================
CREATE PROCEDURE get_book_by_id 
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
	SELECT * from table_books
	-- The next section is for inserting a new book to the table
	--insert into table_books
	--([book_id],[book_title],[book_summary],[book_content],[author_id])
	--values
	--(@book_id, @book_title, @book_summary, @book_content, @author_id)
	
END
GO
