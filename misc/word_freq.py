
'''
Setting the default_factory to int makes the defaultdict useful for counting (like a bag or multiset in other languages):
https://docs.python.org/2/library/collections.html#collections.defaultdict
'''

from collections import defaultdict

str = '''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

#print(str)

words = str.split()
#print (words)
d = defaultdict(int)

for w in words:
    d[w] += 1
     
print (d)

o/p
defaultdict(<class 'int'>, {'The': 1, 'Zen': 1, 'of': 3, 'Python,': 1, 'by': 1, 'Tim': 1, 'Peters': 1, 'Beautiful': 1, 'is': 10, 
'better': 8, 'than': 8, 'ugly.': 1, 'Explicit': 1, 'implicit.': 1, 'Simple': 1, 'complex.': 1, 'Complex': 1, 'complicated.': 1, 
'Flat': 1, 'nested.': 1, 'Sparse': 1, 'dense.': 1, 'Readability': 1, 'counts.': 1, 'Special': 1, 'cases': 1, "aren't": 1, 
'special': 1, 'enough': 1, 'to': 5, 'break': 1, 'the': 5, 'rules.': 1, 'Although': 3, 'practicality': 1, 'beats': 1, 'purity.': 1, 
Errors': 1, 'should': 2, 'never': 2, 'pass': 1, 'silently.': 1, 'Unless': 1, 'explicitly': 1, 'silenced.': 1, 'In': 1, 'face': 1, 
'ambiguity,': 1, 'refuse': 1, 'temptation': 1, 'guess.': 1, 'There': 1, 'be': 3, 'one--': 1, 'and': 1, 'preferably': 1, 'only': 1, 
'one': 2, '--obvious': 1, 'way': 2, 'do': 2, 'it.': 1, 'that': 1, 'may': 2, 'not': 1, 'obvious': 1, 'at': 1, 'first': 1, 'unless': 1, 
"you're": 1, 'Dutch.': 1, 'Now': 1, 'never.': 1, 'often': 1, '*right*': 1, 'now.': 1, 'If': 2, 'implementation': 2, 'hard': 1, 
'explain,': 2, "it's": 1, 'a': 2, 'bad': 1, 'idea.': 2, 'easy': 1, 'it': 1, 'good': 1, 'Namespaces': 1, 'are': 1, 'honking': 1, 
'great': 1, 'idea': 1, '--': 1, "let's": 1, 'more': 1, 'those!': 1})
