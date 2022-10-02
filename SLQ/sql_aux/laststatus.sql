Select MAX(t6.[ultimo status normal]) as 'ultimo status' from (
    SELECT t1.TaskId as ttId, MAX(t1.Timestamp) as 'ultimo status normal' FROM [cash].[fast].[TaskHistories] t1
	
		JOIN (SELECT TemplateId,Id FROM [cash].[fast].[Status]) as statusE
		ON statusE.Id = t1.NewValue
		JOIN (SELECT IsFinal,Id FROM [cash].[fast].StatusTemplates) as statusT
		ON statusE.TemplateId = statusT.Id
	where PropertyName = 'StatusId' and t1.TaskId = 26497 and statusT.IsFinal = 0
	GROUP BY t1.TaskId 
	union ALL
		SELECT t11.TaskId as ttId, MIN(t11.Timestamp) as 'primeiro status final' FROM [cash].[fast].[TaskHistories] t11
	
		JOIN (SELECT TemplateId,Id FROM [cash].[fast].[Status]) as statusE
		ON statusE.Id = t11.NewValue
		JOIN (SELECT IsFinal,Id FROM [cash].[fast].StatusTemplates) as statusT
		ON statusE.TemplateId = statusT.Id

		where PropertyName = 'StatusId' and t11.TaskId = 26497 and statusT.IsFinal = 1
		GROUP BY t11.TaskId

		) t6
