ALTER TABLE [dbo].[Book]
    ADD CONSTRAINT [FK_Book_Category] FOREIGN KEY ([CategoryID]) REFERENCES [dbo].[Category] ([CategoryID]) ON DELETE NO ACTION ON UPDATE NO ACTION;

