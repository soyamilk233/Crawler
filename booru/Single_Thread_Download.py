def Download(imglist, page, name, num):
    i = 0;
    while(i < len(imglist)):
        a = imglist[i]
        b = num[i]
        mypath = 'G:\\temp\\' + name + '\\' + b + '.' + a[2]
        if(os.path.exists(mypath)):
            print(name + '-page' + str(page)+ '-' + str(num[i]) + ' already done')
            i+=1
            continue
        print(str(i) + ' - ' + mypath)
        cnt = 5;
        while cnt > 0:
            try:
                mp4data = requests.get(a[1], timeout=30).content
            except: #requests.exceptions.ReadTimeout:
                print ('Timeout, try agian')
                cnt-=1
            else:
                with open(mypath, 'wb') as f:
                    f.write(mp4data)
                break;
        else:
            print (name + '-page' + str(page)+ '-' + b + ' Try 5 times, But all failed')
        print(name + '-page' + str(page)+ '-' + b + ' done')
        i+=1
        time.sleep(5)
