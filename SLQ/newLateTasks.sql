SELECT Tasks.Id, Tasks.EndDate as 'Prazo',tasks.StartDate,tasks.EstimatedEffort as 'Estimativa', his.NewValue as 'Ultimo_Status', his.Timestamp as 'Ultima_Mudanca',
	CASE WHEN his.Timestamp > DATEADD(DAY,1,Tasks.EndDate)
    THEN '1' 
    ELSE '0' 
	END 
	AS 'Atrasado',
  Tasks.UserId,
  TemplateId,
  IsFinal,
  CASE WHEN   sub.SubCount IS NULL
    THEN '0' 
    ELSE sub.SubCount 
	END 
	AS 'TotalSubtarefas'

  FROM [cash].[fast].[Tasks] tasks
    
  JOIN (

    SELECT t1.TaskId as ttId, t1.NewValue, t1.Timestamp FROM [cash].[fast].[TaskHistories] t1
	JOIN (SELECT TaskId, MAX(timestamp) timestamp FROM [cash].[fast].[TaskHistories] GROUP BY TaskId) t2
    ON t1.TaskId = t2.TaskId AND t1.timestamp = t2.timestamp
	where PropertyName = 'StatusId' ) his
	ON tasks.Id = ttId
	
	JOIN (SELECT TemplateId,Id FROM [cash].[fast].[Status]) as statusE
	ON statusE.Id = his.NewValue
	JOIN (SELECT IsFinal,Id FROM [cash].[fast].StatusTemplates) as statusT
	ON statusE.TemplateId = statusT.Id
	
	LEFT JOIN (SELECT TaskId, COUNT(Subtasks.TaskId) as SubCount FROM [cash].[fast].[Subtasks] GROUP BY TaskId) sub
	ON sub.TaskId = tasks.Id
  where EndDate is not Null and Active = 1 



  
  select * from cash.[fast].Status
    select * from cash.[fast].StatusTemplates