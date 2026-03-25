import json

with open('price_analysis.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
    if 'describe' in src:
        cell['source'] = """\
summary = df['price'].describe().rename({
    'count': 'Count', 'mean': 'Mean (\u20ac)', '50%': 'Median (\u20ac)'
}).to_frame().T.round(2)
summary = summary[['Count', 'Mean (\u20ac)', 'Median (\u20ac)']]

summary.style.format('\u20ac{:.2f}', subset=['Mean (\u20ac)', 'Median (\u20ac)']).set_caption('Overall Price Distribution')"""
        cell['outputs'] = []
        cell['execution_count'] = None
        break

with open('price_analysis.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('Done')
