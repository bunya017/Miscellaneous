import json
import os



filename = str(input('Write the name or path of snippets file: \n$ '))
with open(filename, encoding='utf-8') as f_obj:
	vs_code_snippets = json.load(f_obj)

vs_code_snippets_keys = list(vs_code_snippets.keys())
snippet_name = 'snippets/%s.sublime-snippet' % (
	vs_code_snippets[vs_code_snippets_keys[0]]['prefix']
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
	vs_code_snippets[vs_code_snippets_keys[0]]['body'][0],
	vs_code_snippets[vs_code_snippets_keys[0]]['prefix'],
	vs_code_snippets[vs_code_snippets_keys[0]]['description']
)
if not os.path.exists('snippets'):
	os.makedirs('quasar_snippets')
with open(snippet_name, 'w') as w_obj:
	w_obj.write(snippet_content.strip())

print('Completed successfully')