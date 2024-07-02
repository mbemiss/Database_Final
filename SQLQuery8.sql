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
-- Description:	This procedure gets all authors in the database.
-- =============================================
CREATE PROCEDURE get_all_authors 
	-- Add the parameters for the stored procedure here
	@author_id int = 0, 
	@first_name varchar = 50,
	@last_name varchar = 50,
	@birth_date date,
	@nationality varchar = 50,
	@biography varchar = max
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT * from table_authors
END
GO
