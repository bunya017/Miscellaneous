import json
import os



filename = str(input('Write the name or path of snippets file: \n$ '))
with open(filename, encoding='utf-8') as f_obj:
	vs_code_snippets = json.load(f_obj)

vs_code_snippets_keys = list(vs_code_snippets.keys())

for i in range(len(vs_code_snippets_keys)):
	snippet_name = 'snippets/%s.sublime-snippet' % (
		vs_code_snippets[vs_code_snippets_keys[i]]['prefix']
	)
	snippet_content = '''
	<snippet>
		<content><![CDATA[
	%s
	]]></content>
		<tabTrigger>%s</tabTrigger>
		<description>%s</description>
	</snippet>
	''' % (
		vs_code_snippets[vs_code_snippets_keys[i]]['body'][0],
		vs_code_snippets[vs_code_snippets_keys[i]]['prefix'],
		vs_code_snippets[vs_code_snippets_keys[i]]['description']
	)
	if not os.path.exists('snippets'):
		os.makedirs('snippets')
	with open(snippet_name, 'w') as w_obj:
		w_obj.write(snippet_content.strip())

print('Completed successfully')