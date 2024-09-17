from typing import Any

root = {
    'data': 'A', 'children': [{
        'data': 'B', 'children':[{
            'data': 'D', 'children': []}]}, {
        'data': 'C', 'children':[{
            'data': 'E', 'children': [{
                'data': 'G', 'children': []}, {
                'data': 'H', 'children': []}]}, {
            'data': 'F', 'children': []
        }]
    }]
}

def preorderTraverse(node: dict[str, Any]):
    print(node['data'], end=' * ')
    
    if len(node['children']) > 0:
        for child in node['children']:
            preorderTraverse(child)
            
    return

preorderTraverse(root)  # Output: ABDCEGHF