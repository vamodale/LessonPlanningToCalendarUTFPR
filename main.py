import os
import pandas as pd	

SCHEDULER_NAME = 'scheduler.csv'
CSV_PATH = './csvs/{}'

schedule = pd.read_csv(CSV_PATH.format(SCHEDULER_NAME), sep=',')
	
class_schedule = dict()

for _, row in schedule.iterrows():
	a = row.iloc[3:-1]
	for i, dia in enumerate(a.index):
		dia = dia.split(' ')[0]
		if not pd.isna(row.iloc[i+3]):
			class_name = row.iloc[i+3].split('-')[0]
			if not class_schedule.get(dia, None):
				class_schedule[dia] = dict()
			class_schedule[dia][class_name] = class_schedule.get(dia, dict()).get(
				class_name, list()
			) + [
				(row.iloc[1], row.iloc[2]),
			]

for file in os.scandir('./csvs'):
	file = file.name
	if file == SCHEDULER_NAME: 
		continue

	class_plan = pd.read_csv(CSV_PATH.format(file), sep='" ; "', engine='python')
	class_name = file.split('.')[0]
	print(class_name)
	for _, row in class_plan.iterrows():
		print(class_schedule[row.iloc[1]][class_name])
	