#Gaurav Sablok 
#Senior Postdoctoral Fellow Faculty of Natural and Agricultural Sciences 
#Room 7-35, Agricultural Sciences Building 
#University of Pretoria, Private Bag X20 Hatfield 0028, 
#South Africa 
import os 
import subprocess
def makePBS(path):   
    """a function call to make all the command line application for the
    CHPC cluster. Run with the parameters asked and it will make and 
    submit the job to the cluster
    qsub: Submit a job
    qdel: Delete a batch job
    qsig: Send a signal to batch job
    qhold: Hold a batch job
    qrls: Release held jobs
    qrerun: Rerun a batch job
    qmove: Move a batch job to another queue
    qstat: Show status of batch jobs 
    qselect: Select a specific subset of jobs
    qalter: Alter a batch job
    qmsg: Send a message to a batch job
    """
    if not os.path.exists(path):
        os.mkdir(path)
        os.chdir(os.mkdir(path))
    PBS_JOBNAME = ""
    PBS_O_LOGNAME = ""
    PBS_O_MAIL = ""
    PBS_O_HOST = ""
    PBS_O_QUEUE = ""
    PBS_O_WORKDIR = ""
    PBS_NODES = ""
    PBS_COMMAND = ""
    PBS_MODULE = ""
    PBS_NCPUS = ""
    while True:
        take_jobname = input("Please enter the jobname:")
        take_queue = input("Please enter the queue name:")
        take_logname = input("Please enter the name for the logname:")
        take_mail = input("Please enter the email for the job:")
        take_host = input("Please enter the hostname for the cluster:")
        take_queue = input("Please enter the queue for the job to run:")
        take_workdir = input("Please enter the working directory for the job:")
        take_node = input("please enter the computing node:")
        take_threads = input("Please enter the threads:")
        take_command = input("Please enter the command:")
        PBS_JOBNAME += take_jobname
        PBS_O_QUEUE += take_queue
        PBS_O_LOGNAME += take_logname
        PBS_O_MAIL += take_mail
        PBS_O_HOST += take_host
        PBS_O_QUEUE += take_queue
        PBS_O_WORKDIR += take_workdir
        PBS_NODES += take_node
        PBS_NCPUS += take_threads
        PBS_COMMAND += take_command
        #take_vars = ["take_jobname", "take_queue", "take_logname", "take_mail", "take_host", "take_queue", \
                         #"take_workdir", "take_node", "take_threads", "take_command"] 
        if take_jobname and take_queue and take_logname and take_mail and take_host and take_queue \
            and take_workdir and take_node and take_threads and take_command == "None":
                break
        while True:
            """
            You can pass a space separated list of all the modules you want to load 
            on the cluster. 
            """
            take_module = input("Please enter the module name:")
            PBS_MODULE += take_module
            if take_module == "":
                break
            return print(f"PBS_JOBNAME={''.join(PBS_JOBNAME)} \
                         \nPBS_O_LOGNAME = {''.join(PBS_O_LOGNAME)} \
                         \nPBS_O_MAIL = {''.join(PBS_O_MAIL)} \
                         \nPBS_O_HOST = {''.join(PBS_O_HOST)} \
                         \nPBS_O_QUEUE = {''.join(PBS_O_QUEUE)} \
                         \nPBS_O_WORKDIR = {''.join(PBS_O_WORKDIR)} \
                         \nPBS_NODES = {''.join(PBS_NODES)} \
                         \nPBS_NCPUS = {''.join(PBS_NCPUS)} \
                         \nPBS_COMMAND = {''.join(PBS_COMMAND)} \
                         \nPBS_MODULE = {''.join(PBS_MODULE)}")

# without path version
import os 
import subprocess
def makepbsPATH():   
    """a function call to make all the command line application for the
    CHPC cluster. Run with the parameters asked and it will make and 
    submit the job to the cluster
    qsub: Submit a job
    qdel: Delete a batch job
    qsig: Send a signal to batch job
    qhold: Hold a batch job
    qrls: Release held jobs
    qrerun: Rerun a batch job
    qmove: Move a batch job to another queue
    qstat: Show status of batch jobs 
    qselect: Select a specific subset of jobs
    qalter: Alter a batch job
    qmsg: Send a message to a batch job
    """
    PBS_JOBNAME = ""
    PBS_O_LOGNAME = ""
    PBS_O_MAIL = ""
    PBS_O_HOST = ""
    PBS_O_QUEUE = ""
    PBS_O_WORKDIR = ""
    PBS_NODES = ""
    PBS_COMMAND = ""
    PBS_MODULE = ""
    PBS_NCPUS = ""
    while True:
        take_jobname = input("Please enter the jobname:")
        take_queue = input("Please enter the queue name:")
        take_logname = input("Please enter the name for the logname:")
        take_mail = input("Please enter the email for the job:")
        take_host = input("Please enter the hostname for the cluster:")
        take_queue = input("Please enter the queue for the job to run:")
        take_workdir = input("Please enter the working directory for the job:")
        take_node = input("please enter the computing node:")
        take_threads = input("Please enter the threads:")
        take_command = input("Please enter the command:")
        PBS_JOBNAME += take_jobname
        PBS_O_QUEUE += take_queue
        PBS_O_LOGNAME += take_logname
        PBS_O_MAIL += take_mail
        PBS_O_HOST += take_host
        PBS_O_QUEUE += take_queue
        PBS_O_WORKDIR += take_workdir
        PBS_NODES += take_node
        PBS_NCPUS += take_threads
        PBS_COMMAND += take_command
        #take_vars = ["take_jobname", "take_queue", "take_logname", "take_mail", "take_host", "take_queue", \
                         #"take_workdir", "take_node", "take_threads", "take_command"] 
        if take_jobname and take_queue and take_logname and take_mail and take_host and take_queue \
            and take_workdir and take_node and take_threads and take_command == "None":
                break
        while True:
            """
            You can pass a space separated list of all the modules you want to load 
            on the cluster. 
            """
            take_module = input("Please enter the module name:")
            PBS_MODULE += take_module
            if take_module == "":
                break
            return print(f"PBS_JOBNAME={''.join(PBS_JOBNAME)} \
                         \nPBS_O_LOGNAME = {''.join(PBS_O_LOGNAME)} \
                         \nPBS_O_MAIL = {''.join(PBS_O_MAIL)} \
                         \nPBS_O_HOST = {''.join(PBS_O_HOST)} \
                         \nPBS_O_QUEUE = {''.join(PBS_O_QUEUE)} \
                         \nPBS_O_WORKDIR = {''.join(PBS_O_WORKDIR)} \
                         \nPBS_NODES = {''.join(PBS_NODES)} \
                         \nPBS_NCPUS = {''.join(PBS_NCPUS)} \
                         \nPBS_COMMAND = {''.join(PBS_COMMAND)} \
                         \nPBS_MODULE = {''.join(PBS_MODULE)}")
