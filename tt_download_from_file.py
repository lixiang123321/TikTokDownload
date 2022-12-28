import TikTokDownload as ttd
import os

file_name = './workspace/movie_1104.txt'
movie_start = 96 # 下一个就是a，用chr(start)
num_start = 0

download_dir = '/Users/rerelovehermione/Workspace/tt/movie_workspace/batch/'

with open(file_name) as f:
    for line in f:
        # print(line)
        if (line.strip()==''):
            # print('空行')
            continue
        elif (line.strip()=='---'):
            print('换电影了')
            movie_start+=1
            print(chr(movie_start))
            num_start = 0
        else :
            num_start+=1
            # 下载， line就是url，名字就是 chr(movie_start) + str(num_start)
            # 目标文件夹， download_dir+"movie_"+chr(movie_start)
            # # print("url:"+line)
            # print("name:"+chr(movie_start) + str(num_start))
            # print("dir"+download_dir+"movie_"+chr(movie_start))
            url = line
            name = chr(movie_start) + str(num_start) 
            dir_name = download_dir+"movie_"+chr(movie_start) + '/'

            print("url:"+url)
            print("name:"+name)
            print("dir:"+dir_name)
            
            try:
                os.makedirs(dir_name)
            except FileExistsError:
                None

            if num_start == 1:
                # 写电影信息
                with open(f'{dir_name}info.txt', 'w') as f:
                    f.write(line)

            # ttd.video_download(urlarg=url, 
                # musicarg=dir_name+name)


