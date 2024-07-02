USE [db_theplotspot]
GO
/****** Object:  StoredProcedure [dbo].[get_all_authors]    Script Date: 6/23/2024 2:44:53 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Mike Bemiss
-- Create date: 6/23/2024
-- Description:	This procedure gets all authors in the database.
-- =============================================
ALTER PROCEDURE [dbo].[get_all_authors] 
	-- Add the parameters for the stored procedure here
	-- These parameters are not needed for this procedure but will be needed for others.
	--@author_id int = 0, 
	--@first_name varchar = 50,
	--@last_name varchar = 50,
	--@birth_date date,
	--@nationality varchar = 50,
	--@biography varchar = max
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT * from table_authors
END
