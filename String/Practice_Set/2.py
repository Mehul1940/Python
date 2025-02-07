letter='''
    Dear <|name|>,
    
    This is a letter.
    You are Selected!
    <|Date|>
'''
print(letter.replace("<|name|>","Sachin").replace("<|Date|>","01-01-2020"))