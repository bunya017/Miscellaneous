import json
import os



filename = input('Write the name or path of snippets file: \n$ ')
with open(filename, encoding='utf-8') as f_obj:
	vs_code_snippets = json.load(f_obj)

vs_code_snippets_keys = list(vs_code_snippets.keys())

for i in range(len(vs_code_snippets_keys)):
	snippet_name = 'snippets/%s.sublime-snippet' % (
		vs_code_snippets[vs_code_snippets_keys[i]]['prefix']
	)
	prefix = vs_code_snippets[vs_code_snippets_keys[i]]['prefix']
	body = '''{}'''.format('\n'.join(vs_code_snippets[vs_code_snippets_keys[i]]['body']))
	description = vs_code_snippets[vs_code_snippets_keys[i]]['description']
	short_description = description[:32] + '...'
	snippet_content =(
		'<snippet>\n\t<content><![CDATA[\n%s\n]]></content>\n\t<tabTrigger>%s</tabTrigger>\n\t<scope>text.html.vue</scope>\n\t<description>%s</description>\n\t<!-- Long description: %s --></snippet>'
	) % (body, prefix, short_description, description)
	if not os.path.exists('snippets'):
		os.makedirs('snippets')
	with open(snippet_name, 'w') as w_obj:
		w_obj.write(snippet_content.strip())

print('Completed successfully')