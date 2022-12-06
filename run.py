import utils.clone_repo as clone_utils
import utils.repo_link_generator
from utils.scan import scan_repo_report
from utils.compare import main as compare_and_generate_report
from utils.delete import delete_temp
import sys
import os

def workflow():
    valid_repositories = []
    cwd = os.getcwd()
    clone_utils.install_privado()
    for repo_link in utils.repo_link_generator.generate_repo_link(sys.argv[1]):
        try:
            repo_name = repo_link.split('/')[-1].split('.')[0]
        except:
            print("Not a valid git repository")
            continue
        valid_repositories.append(repo_name)
        clone_utils.clone_repo(repo_link)
    scan_repo_report()
    for repo_name in valid_repositories:
        stable_file = f'{cwd}/temp/result/stable/{repo_name}.json'
        dev_file = f'{cwd}/temp/result/dev/{repo_name}.json'
        cpu_usage = f'{cwd}/temp/cpu_mem/{repo_name}_cpu_mem.txt'
        stable_time = f'{cwd}/temp/result/stable/{repo_name}_time.txt'
        dev_time = f'{cwd}/temp/result/dev/{repo_name}_time.txt'
        compare_and_generate_report(stable_file, dev_file, cpu_usage, stable_time, dev_time)

    delete_temp()



        
    
    

workflow()

