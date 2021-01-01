import re

def solution(files):
    num = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    final = sorted(num, key=lambda file : re.split('\d+', file.lower())[0])
    return final

input = [["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
         ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]]

for i in input:
    print(solution(i))