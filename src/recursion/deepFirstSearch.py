from typing import Any

root = {
    'name': 'Alicja', 'children': [{
        'name': 'Bartek', 'children':[{
            'name': 'Daria', 'children': []}]}, {
        'name': 'Karolina', 'children':[{
            'name': 'Ewa', 'children': [{
                'name': 'Gabriel', 'children': []}, {
                'name': 'Radosław', 'children': []}]}, {
            'name': 'Franek', 'children': []
        }]
    }]
}

def find8LitterName(node: dict[str, Any], response: list[str]) -> list[str]:
    print('Odwiedzam węzeł ' + node['name'] + '...')
    print('Sprawdzam, czy w węźle ' + node['name'] + ' znajduje się ośmioliterowe słowo')
    if len(node['name']) == 8:
        print('Odwiedzam')
        response.append(node['name'])

    if len(node['name']) > 0:
        for child in node['children']:
            find8LitterName(child, response)
                 
    return response

responses = find8LitterName(root, [])
print('Znalezione ośmioliterowe słowa to: ', responses)