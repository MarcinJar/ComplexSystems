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

def postorderTraversal(node: dict[str, Any]):
    if len(node['children']) > 0:
        for child in node['children']:
            postorderTraversal(child)
            
    print(node['data'], end=' * ')    
    return

postorderTraversal(root) #DBGHEFCA