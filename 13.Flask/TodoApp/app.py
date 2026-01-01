from flask import Flask,render_template,request,jsonify
app=Flask(__name__)

tasks = [
    {"id": 1, "task": "DSA"},
    {"id": 2, "task": "DEV"}
]

@app.route('/getall',methods=['GET'])
def getAll():
    return jsonify(tasks)

@app.route('/getfromid/<int:id>',methods=['GET'])
def getFromID(id):
    for task in tasks:
        if task['id']==id:
            return jsonify(task)
    return jsonify({"Error":"No Tasks Found"})

@app.route('/addtask',methods=['POST'])
def addTask():
    data=request.json
    newTask={
        'id':len(tasks)+1,
        'task':data.get("task")
    }
    tasks.append(newTask)
    return jsonify(newTask)


@app.route('/deletetask/<int:id>',methods=['DELETE'])
def deleteID(id):
    for i,task in enumerate(tasks):
        if task['id']==id:
            tasks.pop(i)
            return jsonify({"message":"Task Deleted"})
    return jsonify({"Error":"No Tasks Found"})

@app.route('/updateTask/<int:id>',methods=['PUT'])
def update_task(id):
    for task in tasks:
        if task['id']==id:
            task["task"]=request.json.get("task",task['task'])
            return jsonify(task)
    return jsonify({"error":"Not Found"})




if __name__=='__main__':
    app.run(debug=True)