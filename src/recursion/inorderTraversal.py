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

def inorderTraversal(node: dict[str, Any]):
    if len(node['children']) >= 1:
        inorderTraversal(node['children'][0])
            
    print(node['data'], end=' * ')    
    
    if len(node['children']) >= 2:
        inorderTraversal(node['children'][1])
        
    return

inorderTraversal(root)