import trace
import sys
tracer = trace.Trace(count = False, trace = True)

def trace_calls(frame, event, arg):
    if event == 'call':
        print(f'calling function: {frame.f_code.co_name}')
    elif event == 'line': #when a new line of code happens
        print(f'Executing line {frame.f_lineno} in {frame.f_code.co_name}')
    elif event == 'line': #when a new line of code happens
        print(f'Executing line {frame.f_lineno} in {frame.f_code.co_name}')
    elif event == 'return':
        print(f"{frame.f_code.co_name} returned {arg}")
    elif event == 'exception': #triggered when there is an exception
        print(f"Exception in {frame.f_code.co_name}: {arg}")
    
    return trace_calls


sys.settrace(trace_calls)
def sub(numone, numtwo):
    return numone - numtwo

def add(numone, numtwo):
    print(sub(numone, numtwo))
    return numone + numtwo


print(add(5,2))
#baisc tracing command

#tracer.run('add(8,9)')
"""
    --trace (displays lines as executed)
    --count (displays number of time executed)
    --listfuncs (displays function used in the program)
    --trackcalls (displays relationships between functions)
"""
x = 14j