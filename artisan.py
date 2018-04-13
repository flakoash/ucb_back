
import sys
import os
import platform

print(sys.argv)


def cp(src, dest):
    old = open(src, 'r')
    new = open(dest, 'w')
    buff = old.read()
    nbuff = buff.replace('XOXOXO', view_name)
    new.write(nbuff)
    old.close()
    new.close()


def appendURL(api=False):
    aux = "" if api else view_name+"/"
    urls = open(ParentDir + '/' + ProjectName + '/urls.py', 'r')
    data = urls.readlines()
    s = "    url('" + aux + "', include('" + view_name + ".urls')), \n ]"
    data[len(data) - 1] = s
    with open(ParentDir + '/' + ProjectName + '/urls.py', 'w') as file:
        file.writelines(data)


def getParentDir():
    dir = os.popen('pwd').read()

    return dir, dir.split('/')[-1].replace('\n', '')


try:
    ParentDir, ProjectName = getParentDir()
    #if sys.argv[1] == 'qwerty':
    #    OSslash = '\\\\' if platform.system() != 'Windows' else '/'
    #    print(OSslash)
    if sys.argv[1] == 'makeapp':
        view_name = sys.argv[2].title()
        os.system('python manage.py startapp '+view_name)
        if '-r' in sys.argv or '--resource' in sys.argv:
            print('---Creating resource APP---')
            # create url.py
            cp(ParentDir+'/artisan/urls.py', ParentDir+'/' + view_name + '/urls.py')
            # create views.py
            cp(ParentDir+'/artisan/views.py', ParentDir+'/' + view_name + '/views.py')
            # include urls to main urls.py
            appendURL()
            #create models.py
            cp(ParentDir+'/artisan/models.py', ParentDir+'/' + view_name + '/models.py')
        if '-t' in sys.argv or '--template' in sys.argv:
            # create template folder for the new resource
            os.system("mkdir templates/" + view_name)
            #create HTML template files
            os.system("cp " + ParentDir + "/artisan/templates/index.html " + ParentDir + "/templates/"+view_name+"/index.html")
            os.system("cp " + ParentDir + "/artisan/templates/create_form.html " + ParentDir + "/templates/"+view_name+"/create_form.html")
            os.system("cp " + ParentDir + "/artisan/templates/show.html " + ParentDir + "/templates/"+view_name+"/show.html")
            os.system("cp " + ParentDir + "/artisan/templates/confirm_delete.html " + ParentDir + "/templates/"+view_name+"/confirm_delete.html")

        if '--rest' in sys.argv:
            print('---Creating REST APP---')
            # create url.py
            cp(ParentDir + '/artisan/rest/urls.py', ParentDir + '/' + view_name + '/urls.py')
            # create views.py
            cp(ParentDir + '/artisan/rest/views.py', ParentDir + '/' + view_name + '/views.py')
            # include urls to main urls.py
            appendURL(api=True)
            # create models.py
            cp(ParentDir + '/artisan/models.py', ParentDir + '/' + view_name + '/models.py')
        if '-a' in sys.argv or '--admin' in sys.argv:
            print('---Registering the APP in Admin---')
            #Register to admin
            cp(ParentDir + '/artisan/admin.py', ParentDir + '/' +view_name + '/admin.py')
        print('New App created successfully! \n'
              '###############################################################\n'
              '####Do not Forget to REGISTER the app inside INSTALLED_APPS####\n'
              '####                    on settings.py:                    ####\n'
              '####                      \'' + view_name + '\',                     ####\n'
              '###############################################################\n')
    else:
        a = ''
        i=0
        for parm in sys.argv:
            if i != 0:
                a += parm + ' '
            i += 1
        os.system('python manage.py ' + a)

except:
    print("Ups! Something in the speedforce is not working fine")











#parser = argparse.ArgumentParser("simple_example")

#print(parser)


#f = open('file.txt','w')

#f.write('answer:'+str(a))
#f.close()