from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import tree, metrics
from joblib import dump

from es.datas.datas import flatten_covid_data as dataset

inputs = dataset.drop(columns=['probable', 'vulnerable', 'fsa', 'week'])

in_recent = LabelEncoder()
in_chills = LabelEncoder()
in_cough = LabelEncoder()
in_breath = LabelEncoder()
in_sixty = LabelEncoder()
in_condit = LabelEncoder()
in_travel = LabelEncoder()
in_contact = LabelEncoder()

inputs['recent_n'] = in_recent.fit_transform(inputs['is_most_recent'])
inputs['chills_n'] = in_recent.fit_transform(inputs['fever_chills_shakes'])
inputs['cough_n'] = in_recent.fit_transform(inputs['cough'])
inputs['breath_n'] = in_recent.fit_transform(inputs['shortness_of_breath'])
inputs['sixty_n'] = in_recent.fit_transform(inputs['over_60'])
inputs['condit_n'] = in_recent.fit_transform(inputs['any_medical_conditions'])
inputs['travel_n'] = in_recent.fit_transform(inputs['travel_outside_canada'])
inputs['contact_n'] = in_recent.fit_transform(inputs['contact_with_illness'])

inputs_n = inputs.drop(columns=['is_most_recent', 'fever_chills_shakes', 'cough', 'shortness_of_breath', 'over_60', 'any_medical_conditions', 'travel_outside_canada', 'contact_with_illness'])

in_probable = LabelEncoder()
in_vulnerable = LabelEncoder()

dataset['probable_n'] = in_probable.fit_transform(dataset['probable'])
dataset['vulnerable_n'] = in_vulnerable.fit_transform(dataset['vulnerable'])

target_prob = dataset['probable_n']
target_vulnerable = dataset['vulnerable_n']

inputs_train, inputs_test, target_train, target_test = train_test_split(inputs_n, target_prob, test_size=0.3, random_state=1)
model = tree.DecisionTreeClassifier()

model = model.fit(inputs_train, target_train)

dump(model, 'covid_v1.joblib')