SELECT Tasks.Id, Tasks.EndDate as 'Prazo',tasks.EstimatedEffort as 'Estimativa', his.NewValue as 'Ultimo_Status', his.Timestamp as 'Ultima_Mudanca',

	CASE WHEN his.Timestamp > DATEADD(DAY,1,Tasks.EndDate)
    THEN '1' 
    ELSE '0' 
  END 
  AS 'Atrasado',
  Tasks.UserId

  FROM [cash].[fast].[Tasks] tasks
  
  JOIN (

    SELECT t1.TaskId as ttId, t1.NewValue, t1.Timestamp FROM [cash].[fast].[TaskHistories] t1
	JOIN (SELECT TaskId, MAX(timestamp) timestamp FROM [cash].[fast].[TaskHistories] GROUP BY TaskId) t2
    ON t1.TaskId = t2.TaskId AND t1.timestamp = t2.timestamp
	where PropertyName = 'StatusId' ) his
	ON tasks.Id = ttId

  where EndDate is not Null and UserId is not null and Active = 1 





