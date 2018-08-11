Chapter 7 -- Exercises 
7.1 please execute the program: mainwithoutreturn, and print the return value
 of it with the command "echo $?", and then compare the return of the printf 
function, they are the same. 
7.2 it will depend on the exection mode, interactive or redirection to a file, 
if interactive, the "output" action will accur after the \n char with the line
 buffer mode, else, it will be really "printed" after all of the strings have 
been stayed in the buffer. 
7.3 there is no another effective method in most OS. because argc and argv are 
not global variables like environ.