from datetime import datetime

assignmentList = []
results = []
def add_assignment(assignment, due_date, due_time = "All Day"):
    '''
    The function takes assignment, due_date, due_time as inputs.
    This tool adds assignment to the assignmentList dictionary with the assignment name as the key and a tuple of due_date and due_time as the value. 
    The due_time is an optional parameter and defaults to "All Day" if not mentioned. 
    '''
    assignmentList.append({
            "Assignment" : assignment, 
            "Due Date" : due_date, 
            "Due Time" : due_time
        })
    return f"Assignment: {assignment} has been added with due date: {due_date}and due time: {due_time}."

def list_assignments(due_date, due_time = None):
    '''
    This function takes due_date and due_time as inputs and lists all the assignments that are due on the given date and time.
    If due_time is not provided, it lists all assignments due on the given date regardless of the time.
    '''
    free = True
    for assignment in assignmentList:
        if (due_time is None and assignmentList[assignment]["Due Date"] == due_date):
            if (assignmentList[assignment][1] is None):
                results.append({
                    "Assignment" : assignment, 
                    "Due Date" : due_date, 
                    "Due Time" : "All Day"
                })
            else:
                results.append({
                    "Assignment" : assignment, 
                    "Due Date" : due_date, 
                    "Due Time" : assignmentList[assignment][1]
                })
            free = False
        elif assignmentList[assignment][0] == due_date and assignmentList[assignment][1] == due_time:
            results.append({
                "Assignment" : assignment, 
                "Due Date" : due_date, 
                "Due Time" : due_time
            })
            free = False

    if free:
        results.append(f"No assignments due on: {due_date} at {due_time}!")

    return results
    


# add_assignment("Agentic AI", "2024-06-30")
# add_assignment("Agentic AI", "2024-06-30", "17:00")
# add_assignment("Mathematics", "2024-06-30")
# add_assignment("English", "2024-06-30", "1:00")
# print("Assignments due on 2024-06-30 at 17:00:")
# list_assignments("2024-06-30", "17:00")
# print("Assignments due on 2024-06-30:")
# list_assignments("2024-06-30")