'''
If a node has child nodes, its ID will be stored in the second field. 
Therefore, the condition can be used to determine whether a node is internal or a leaf. 
If its ID is specified in the second field, the node is internal and other nodes extend from it. 
If its number is not in the second field, it is a leaf, and when it is tested, the condition goes to the else clause.
'''

SELECT id,
    CASE WHEN p_id IS NULL THEN 'Root'
         WHEN id IN (SELECT DISTINCT p_id
                     FROM Tree) THEN 'Inner'
         ELSE 'Leaf' END AS type
FROM Tree;
