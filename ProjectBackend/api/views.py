from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import connection
import django.db as db


################## function to get or post a task ##################

@api_view(['GET', 'POST'])
def GetTasks(request):
    if(request.method == 'GET'):
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM tasks''')
        result = cursor.fetchall()
        return Response(result)
    elif(request.method == 'POST'):
        try:
            cursor = connection.cursor()
            cursor.execute('''INSERT into tasks (task) values("''' + request.data['task'] + '")')
            return Response({"Message": "Task added sucessfully."})
        except db.OperationalError as e:
            return Response(list({'Error': e}), status = 400)
        except db.Error as e:
            return Response(list({'Error': e}), status = 400)
        except:
            return Response({'Error': 'Invalid Parameter'}, status = 400)


################## function to get, put and detele a task by id ##################

@api_view(['GET', 'PUT', 'DELETE'])
def GetTask(request):
    if(request.method == 'GET'):
        try:
            cursor = connection.cursor()
            cursor.execute('''SELECT * FROM tasks where id = "''' + request.query_params['id'] + '"')
            result = cursor.fetchone()
            if(result):
                return Response(result)
            else:
                return Response({'Error': 'Task not found with id :: ' + request.query_params['id']}, status = 404)
        except:    
            return Response({'Error': 'Invalid Parameter'}, status = 400)
        
    elif(request.method == 'DELETE'):
        try:
            cursor = connection.cursor()
            cursor.execute('''delete from tasks where id = "''' + request.query_params['id'] + '"')
            if(cursor.rowcount == 0):
                return Response({"Message": "Task does not exists."}) 
            else:
                return Response({"Message": "Task deleted sucessfully."})
        except db.OperationalError as e:
            return Response(list({'Error': e}), status = 400)
        except db.Error as e:
            return Response(list({'Error': e}), status = 400)
        except:    
            return Response({'Error': 'Invalid Parameter'}, status = 400)   
        
    elif(request.method == 'PUT'):
        try:
            cursor = connection.cursor()
            cursor.execute('''update tasks set task = "''' + request.data['task'] + '" where id = "' + request.query_params['id'] + '"')
            if(cursor.rowcount == 0):
                return Response({"Message": "Task does not exists."}) 
            else:
                return Response({"Message": "Task edited sucessfully."})
        except:    
            return Response({'Error': 'Invalid Parameter'}, status = 400)
            
    

