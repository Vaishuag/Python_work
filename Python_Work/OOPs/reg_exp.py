import re

txt='You are studying in Besant'
X=re.search('^You.*Besant$',txt)
print(X)

if X:
    print('Match')
else:
    print('No Match')