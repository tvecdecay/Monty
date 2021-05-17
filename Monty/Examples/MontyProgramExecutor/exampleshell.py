import monty

print("MONTY SHELL | (not) Copyright (not in) 2021")
objs = []
while True:
    try:
        print('\n', end='')
        cmd = input(">>>")
        for i in objs:
            if cmd in i.givename():
                i.execute()
        cmdobj = monty.command(cmd, execinstant=False)
        objs.append(cmdobj)
    except Exception as excp:
        print(f"Error: {excp}")