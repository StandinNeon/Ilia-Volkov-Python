def parse_log(pth_file="./nginx_logs.txt"):

    if pth_file:
        with open(pth_file, "r", encoding="utf-8") as file:
            for line in file:
                ip = line.split(" - - ")[0]
                rsp_and_pth = line.split('"')[1]
                rsp = rsp_and_pth.split()[0]
                pth = rsp_and_pth.split()[1]
                yield(ip, rsp, pth)