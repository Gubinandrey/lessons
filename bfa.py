import tqdm
import utils
n1='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()<>,./?'
for asd1 in tqdm.tqdm(n1):
    for asd2 in n1:
        for asd3 in n1:
            for asd4 in n1:
                password=asd1+asd2+asd3+asd4
                n5=utils.check_password(password)
                if n5==True:
                    print(password)
                    exit(0)