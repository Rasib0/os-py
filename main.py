from asyncio.windows_events import NULL


from functionDic import function_list
with open('p1.txt') as f:
    contents = f.read().split()
    
currByte = NULL


for i in len(contents):
    if (contents[i] in functionList):
        function_list[contents[i]]





    