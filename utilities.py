def shutdown():
    import os
    os.system("shutdown /s /t 1")
    del os
def User():
    import os
    path=os.path.dirname(os.path.realpath(__file__))
    if not 'Users' in path:
        raise Exception('File should be above "C://Users/<user>"')
    path=path.split('\"')
    path=path[0].split('\\')
    for i in range(len(path)):
        a=path[i]
        if a=='Users':
            user=path[i+1]
            break
    del os
    return user
def Link(programToLink, intrerupt):
    import os
    os.system(programToLink)
    if intrerupt==True:
        os._exit(0)
    else:
        pass
    del os
def ComingSoon():
    print('This AddOn is still in development')
def CopyFile(File1,NextFile):
    f=open(File1, 'r')
    Scripts=f.readlines()
    f.close()
    f=open(NextFile,'w')
    f.write(Scripts)
    f.close()
def ReChaptcha():
    import os
    os.system('cls')
    def verify():
        import random
        L=""
        I=""
        G=""
        L='@@@@@@@@\n@@@@@@@@\n@@@@@@@@\n@@@@@@@@\n@@@@@@@@\n@@@@@@@@\n@@@@@@@@\n@@@@@@@@\n@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@'
        I='@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@\n\n\n@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@'
        G='@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@                    @@@@@@@@@@\n@@@@@@@@@@                    @@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@\n@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@                    @@@@@@@@@@\n@@@@@@@@@@                    @@@@@@@@@@\n@@@@@@@@@@                    @@@@@@@@@@\n@@@@@@@@@@                    @@@@@@@@@@\n@@@@@@@@@@                    @@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
        a=[]
        a.append(L)
        a.append(I)
        a.append(G)
        b=random.choice(a)
        print(b)
        c=input('Leter: ')
        if b==L:
            b='L'
        elif b==I:
            b='I'
        elif b==G:
            b='G'
        else:
            raise Exception('An Error Occured In "Random"')
        del random
        return c==b
    os.system('cls')
    print('Please Verify Human:')
    if verify()!=True or verify()==False:
        raise ImportError('not a human error')
    del os
