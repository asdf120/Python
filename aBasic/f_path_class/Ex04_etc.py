"""
경로 이동은  Path 모듈로 안되어 os 모듈이 필요하다
"""
import os
print(os.environ["HOMEPATH"])
print(os.path.expandvars('%JAVA_HOME%'))
print(os.path.expandvars('%TOMCAT_HOME%'))

'''
    shutil 패키지 
'''
import shutil
# shutil.rmtree('imsi')