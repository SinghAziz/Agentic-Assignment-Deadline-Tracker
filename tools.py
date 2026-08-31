from datetime import datetime

assignmentList = []
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

def list_assignments(due_date, due_time = "All Day"):
    '''
    This function takes due_date and due_time as inputs and lists all the assignments that are due on the given date and time.
    If due_time is not provided, it lists all assignments due on the given date regardless of the time.
    '''
    results = []
    free = True
    for assignment in assignmentList:
        if assignment["Due Date"] == due_date and ( assignment["Due Time"] == due_time or due_time == "All Day"):
            results.append({
                "Assignment" : assignment["Assignment"], 
                "Due Date" : assignment["Due Date"], 
                "Due Time" : assignment["Due Time"]
            })
            free = False

    if free:
        results.append(f"No assignments due on: {due_date} at {due_time}!")

    return results
    

AVAILABLE_FUNCTIONS={
    "add_assignment" : add_assignment,
    "list_assignments" : list_assignments
}
# add_assignment("Agentic AI", "2024-06-30")
# add_assignment("Agentic AI", "All Day", "17:00")
# add_assignment("Mathematics", "2024-06-30")
# add_assignment("English", "2024-06-30", "1:00")
# print("Assignments due on 2024-06-30 at 17:00:")
# print(list_assignments("2024-06-30", "17:00"), sep ="\n")
# print("Assignments due on 2024-06-30:")
# for i in list_assignments("2024-06-30"):
#     for j in i:
#         print(f"{j}: {i[j]}")