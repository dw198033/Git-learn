# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 18:58:35 2018

@author: 16012
"""
# singer_周杰|周杰伦|刘德华|王力宏;song_冰雨|北京欢迎你|七里香;actor_周杰伦|孙俪
# 请播放周杰伦的七里香给我听

input_string = [i for i in input().split(";")]
usr_string = [j for j in input()]

print('-'*50)

object_name = [] 
object_value = []

print(input_string)
for i in input_string:
    name, value = i.split("_")
    object_name.append(name)
    object_value.append(value)
    
    print(i)

object_dict = {}

object_dict[object_name[0]] = object_value[0].split("|") # singer
object_dict[object_name[1]] = object_value[1].split("|") # song
object_dict[object_name[2]] = object_value[2].split("|")# actor

def string_match(string, sub_str):
    for i in range(len(string) - len(sub_str)+1):
        index = i
        for j in range(len(sub_str)):
            if string[index] == sub_str[j]:
                index += 1
            else:
                break
            if index-i == len(sub_str):
                return i
        return -1

if __name__ == "__main__":
    print(string_match("adbcbdc", "db"))

