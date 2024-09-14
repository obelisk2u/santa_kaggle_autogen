import autogen
import tempfile
import shutil
import os
import tempfile
from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor
from autogen import GroupChatManager
from autogen import GroupChat
#===============================================================================
file_path_info = "/projectnb/msspbc/jordanstout/home/santa_kaggle_autogen/puzzle_info.csv"
file_path_puzzles = "/projectnb/msspbc/jordanstout/home/santa_kaggle_autogen/puzzles.csv" 
file_path_subex = "/projectnb/msspbc/jordanstout/home/santa_kaggle_autogen/subex.csv"

custom_prefix = "AIs_folder"
custom_dir = "/projectnb/msspbc/jordanstout/home/santa_kaggle_autogen"
temp_dir=tempfile.mkdtemp(prefix=custom_prefix, dir=custom_dir)
print(f"Temporary Directory Path: {temp_dir}")
try:
    file_name = os.path.basename(file_path_info)
    temp_file_path = os.path.join(temp_dir, file_name)
    shutil.copy(file_path_info, temp_file_path)

    file_name_2 = os.path.basename(file_path_puzzles)
    temp_file_path_2 = os.path.join(temp_dir, file_name_2)
    shutil.copy(file_path_puzzles, temp_file_path_2)

    file_name_3 = os.path.basename(file_path_subex)
    temp_file_path_3 = os.path.join(temp_dir, file_name_3)
    shutil.copy(file_path_subex, temp_file_path_3)

    with open(temp_file_path, 'r') as file:
        train=file.read()
    with open(temp_file_path_2, 'r') as file_2:
        test=file_2.read()
    with open(temp_file_path_3, 'r') as file_3:
        subex=file_3.read()

    print(os.listdir(temp_dir))	

finally:
    print("I got u bro")
#==============================================================================
executor = LocalCommandLineCodeExecutor(
    timeout=100,
    work_dir=temp_dir
)

config_list_writer = [
    {	
        'api_key': '',
	'model':'gpt-3.5-turbo',
    }
]

#===============================================================================

code_executor_agent = ConversableAgent(
    "code_executor_agent",
    llm_config=False,  
    code_execution_config={"executor":executor},  
    human_input_mode="ALWAYS"
)
code_writer_system_message = """You are a helpful AI assistant.
Solve tasks using your coding and language skills.
In the following cases, suggest python code (in a python coding block) or shell script (in a sh coding block) for the user to execute.
1. When you need to collect info, use the code to output the info you need, for example, browse or search the web, download/read a file, print the content of a webpage or a file, get the current date/time, check the operating system. After sufficient info is printed and the task is ready to be solved based on your language skill, you can solve the task by yourself.
2. When you need to perform some task with code, use the code to perform the task and output the result. Finish the task smartly.
Solve the task step by step if you need to. If a plan is not provided, explain your plan first. Be clear which step uses code, and which step uses your language skill.
When using code, you must indicate the script type in the code block. The user cannot provide any other feedback or perform any other action beyond executing the code you suggest. The user can't modify your code. So do not suggest incomplete code which requires users to modify. Don't use a code block if it's not intended to be executed by the user.
If you want the user to save the code in a file before executing it, put # filename: <filename> inside the code block as the first line. Don't include multiple code blocks in one response. Do not ask users to copy and paste the result. Instead, use 'print' function for the output when relevant. Check the execution result returned by the user.
If the result indicates there is an error, fix the error and output the code again. Suggest the full code instead of partial code or code changes. If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, revisit your assumption, collect additional info you need, and think of a different approach to try.
When you find an answer, verify the answer carefully. Include verifiable evidence in your response if possible.
Reply 'TERMINATE' in the end when everything is done.
"""

code_writer_agent = ConversableAgent(
    "code_writer_agent",
    system_message=code_writer_system_message,
    llm_config={"config_list":config_list_writer},
    code_execution_config=False
)

"""
manager_agent = ConversableAgent(
    "manager_agent",
    system_message="Your purpose is to come up with a plan to complete the original task of solving all the puzzles and outputting their solution moves to a csv file in the correct format and keep all the other agents stay on the correct path. All code that is to be executed will be done so by the code_executor_agent",
    llm_config={"config_list":config_list_writer},
    code_execution_config=False
)

group_chat = GroupChat(
    agents=[manager_agent, code_writer_agent, code_executor_agent],
    messages=[],
)

group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config={"config_list":config_list_writer},
)
"""
with open('instructions.txt', 'r') as file:
    instructions = file.read().replace('\n', ' ') 

chat_result=code_executor_agent.initiate_chat(
    code_writer_agent,
    message=instructions
)
