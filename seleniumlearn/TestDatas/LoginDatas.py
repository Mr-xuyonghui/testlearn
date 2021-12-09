class Login_account:
    suc_name_psw =["xuyonghui","xuyonghui0224"]
    false_name_psw_notnull =[
        ["xuyoni","xuyonghui0224","请输入正确的账号密码"],
        ["xuyoni","xuyonghu","请输入正确的账号密码"]
    ]
    false_name_psw_null = [
        ["", "xuyonghui0224", "请输入账号"],
        ["xuyoni", "", "请输入密码"],
        ["xuyoni", "", ["请输入密码","请输入账号"]]
    ]
