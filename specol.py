import json
from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
  username='0d8af576-53ef-4feb-9511-7cb30a2b1728',
  password='UbCAJZSXHbkA')

classes = natural_language_classifier.classify('e82f62x108-nlc-5131', 'As a user I want to ask inputs.?')
print(json.dumps(classes, indent=2))

classes = natural_language_classifier.classify('e82f62x108-nlc-5131', 'As a user I want to add A and B?')
print(json.dumps(classes, indent=2))

classes = natural_language_classifier.classify('e82f62x108-nlc-5131', 'As a user I want to divide A and B?')
print(json.dumps(classes, indent=2))

classes = natural_language_classifier.classify('e82f62x108-nlc-5131', 'print output.')
print(json.dumps(classes, indent=2))



natural_language_classifier = NaturalLanguageClassifierV1(
  username='0d8af576-53ef-4feb-9511-7cb30a2b1728',
  password='UbCAJZSXHbkA')

classes = natural_language_classifier.classify('004a12x110-nlc-3218', 'As a user I want to ask inputs.?')
print(json.dumps(classes, indent=2))

classes = natural_language_classifier.classify('004a12x110-nlc-3218', 'As a user I want to add A and B?')
print(json.dumps(classes, indent=2))

classes = natural_language_classifier.classify('004a12x110-nlc-3218', 'As a user I want to divide A and B?')
print(json.dumps(classes, indent=2))

classes = natural_language_classifier.classify('004a12x110-nlc-3218', 'print output.')
print(json.dumps(classes, indent=2))