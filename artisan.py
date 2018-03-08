
import sys
import argparse
import os

print(sys.argv)

try:
    if sys.argv[1] == 'makeapp':
        view_name = sys.argv[2].title()
        os.system('python manage.py startapp '+view_name)
        if '-r' in sys.argv or '--resource' in sys.argv:
            #create url.py
            old = open('artisan/urls.py', 'r')
            new = open(view_name+'/urls.py', 'w')
            buff = old.read()
            nbuff = buff.replace('XOXOXO', view_name)
            new.write(nbuff)
            old.close()
            new.close()
            #replace views.py
            old = open('artisan/views.py', 'r')
            new = open(view_name + '/views.py', 'w')
            buff = old.read()
            nbuff = buff.replace('XOXOXO', view_name)
            new.write(nbuff)
            old.close()
            new.close()
            #include urls to main urls.py
            urls = open('ucb_back/urls.py', 'r')
            data = urls.readlines()
            s = "    url(r'', include('" + view_name + ".urls')), \n ]"
            data[len(data) - 1] = s
            with open('ucb_back/urls.py', 'w') as file:
                file.writelines(data)
            #create models.py
            old = open('artisan/models.py', 'r')
            new = open(view_name + '/models.py', 'w')
            buff = old.read()
            nbuff = buff.replace('XOXOXO', view_name)
            new.write(nbuff)
            old.close()
            new.close()
            #create template folder for the new resource
            os.system("mkdir templates/"+view_name)
            #create HTML template files
            os.system("cp artisan/templates/index.html templates/"+view_name+"/index.html")
            os.system("cp artisan/templates/create_form.html templates/"+view_name+"/create_form.html")
            os.system("cp artisan/templates/show.html templates/"+view_name+"/show.html")
            os.system("cp artisan/templates/confirm_delete.html templates/"+view_name+"/confirm_delete.html")
        if '-a' in sys.argv or '--admin' in sys.argv:
            #Register to admin
            old = open('artisan/admin.py', 'r')
            new = open(view_name + '/admin.py', 'w')
            buff = old.read()
            nbuff = buff.replace('XOXOXO', view_name)
            new.write(nbuff)
            old.close()
            new.close()
    else:
        a = ''
        i=0
        for parm in sys.argv:
            if i != 0:
                a += parm + ' '
            i += 1
        os.system('python manage.py ' + a)

except:
    print("error")








#parser = argparse.ArgumentParser("simple_example")

#print(parser)


#f = open('file.txt','w')

#f.write('answer:'+str(a))
#f.close()