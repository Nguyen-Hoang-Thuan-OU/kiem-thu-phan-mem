﻿ALTER TABLE [dbo].[BookAuthor]
    ADD CONSTRAINT [FK_BookAuthor_Author] FOREIGN KEY ([AuthorID]) REFERENCES [dbo].[Author] ([Id]) ON DELETE NO ACTION ON UPDATE NO ACTION;

