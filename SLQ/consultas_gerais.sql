SELECT
Tasks.Id,
CASE WHEN 
DATEDIFF(MINUTE, tasks.StartDate, tasks.EndDate) IS NULL
THEN 0
ELSE ABS(DATEDIFF(MINUTE, tasks.StartDate, tasks.EndDate))
END
as 'Intervalo (min)',

CEILING(tasks.EstimatedEffort*60)as 'Estimativa (min)', 
  CASE WHEN 
  Tasks.UserId IS NULL
  THEN 0
  ELSE Tasks.UserId
  END
  AS 'Responsavel',
  CASE WHEN   sub.SubCount IS NULL
    THEN 0
    ELSE sub.SubCount 
	END 
	AS 'TotalSubtarefas',
	CASE 
	WHEN tasks.[Priority] is Null
	THEN 0
	WHEN tasks.[Priority] = 0
	THEN 1
	ELSE 0
	END 
	AS 'Urgente',

		CASE 
	WHEN tasks.[Priority] is Null
	THEN 0
	WHEN tasks.[Priority] = 1
	THEN 1
	ELSE 0
	END 
	AS 'Alta',

	CASE WHEN report.MinutosGastos IS NULL
	THEN 0
	ELSE CEILING(report.MinutosGastos)
	END
	AS 'Tempo Gasto (min)',
CASE WHEN hist.[ultimo status] > DATEADD(DAY,1,Tasks.EndDate)
    THEN 1
    ELSE 0 
	END 
	AS 'Atrasado'
  
  FROM [cash].[fast].[Tasks] tasks
    
  JOIN (

  Select his.ttId, MAX(his.[ultimo status normal]) as 'ultimo status' from (
		SELECT t1.TaskId as ttId, MAX(t1.Timestamp) as 'ultimo status normal' FROM [cash].[fast].[TaskHistories] t1
	
		JOIN (SELECT TemplateId,Id FROM [cash].[fast].[Status]) as statusE
		ON statusE.Id = t1.NewValue
		JOIN (SELECT IsFinal,Id FROM [cash].[fast].StatusTemplates) as statusT
		ON statusE.TemplateId = statusT.Id
		where PropertyName = 'StatusId' and  statusT.IsFinal = 0
			GROUP BY t1.TaskId 
			union ALL
			SELECT t11.TaskId as ttId, MIN(t11.Timestamp) as 'primeiro status final' FROM [cash].[fast].[TaskHistories] t11
	
			JOIN (SELECT TemplateId,Id FROM [cash].[fast].[Status]) as statusE
			ON statusE.Id = t11.NewValue
			JOIN (SELECT IsFinal,Id FROM [cash].[fast].StatusTemplates) as statusT
			ON statusE.TemplateId = statusT.Id

			where PropertyName = 'StatusId' and  statusT.IsFinal = 1
			GROUP BY t11.TaskId

		) as his
		group by ttId
) as hist
	ON Tasks.Id = ttId
	
	LEFT JOIN (SELECT TaskId, COUNT(Subtasks.TaskId) as SubCount FROM [cash].[fast].[Subtasks] GROUP BY TaskId) sub
	ON sub.TaskId = tasks.Id

	LEFT JOIN (SELECT Task_Id, SUM(HorasTrabalhadas)*60 as MinutosGastos FROM cash.[fast].reportagem GROUP BY Task_Id ) report
	ON report.Task_Id = tasks.Id 


  where ABS(DATEDIFF(MINUTE, tasks.StartDate, tasks.EndDate)) <> 0


 
 select tags.Id, tags.Name, COUNT(TagTasks.Tag_Id) as 'Quantidade de Tarefas' from cash.[fast].Tags  as tags
 	LEFT JOIN (select TagTasks.Tag_Id from cash.[fast].TagTasks) as TagTasks
		ON tags.Id = TagTasks.Tag_Id
		group by tags.Id,tags.Name
		HAVING count(TagTasks.Tag_Id) > 30


select * from cash.fast.TagTasks
