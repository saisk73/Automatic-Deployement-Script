import os
def  menu():
    print("AUTOMATIC DEPLOYMENT SCRIPT")
    print("1.update packages")
    print("2.deploy project")
    menu_key = input("Enter Choice:")
    if(menu_key == "1"):
        package_update()
    elif(menu_key == "2"):
        install_project()
    else():
        any_key()
        menu()
    def any_key():
        any_input = input("press any key to continue.....")
    def install_project():
        print("Choose one of the options to download code")
        print("1.github")
        print("2.s2 bucket")
        os.system("pip install boot3")
        os.system("pip install bootcore")
        install_choice = input("ENTER CHOICE:")
        if(install_choice == "1"):
            github_is_private = input("Is your repo private? (Y/N)")
            if(github_is_private == "Y" || ):
                github_private_url = input("ENTER GITHUB REPO SSH COMMAND:")
                github_private_username = input("Enter Username:")
                github_private_password = input("Enter password")
                os.system("git clone https://" + github_private_username+":" + github_private_username + "@" + github_private_url)
            elif(github_is_private == "N"):
                git_public_url = input("ENTER GITHUB URL:")
                os.system("git clone " + github_public_url " .")
        elif(install_choice == "2"):
            s3_choice = input("Is the s3 bucket public? (Y/N)")

            if(s3_choice == "Y"):
                s3_name = input("Enter bucket name")
                key = input("enter object name")

                s3 = boot3.resource('s3')
                try:
                    s3.Bucket(s3_name).download_file(KEY, KEY)
                except botocore.exceptions.ClientError as e:
                    if e.response['Error']['Code'] == "404":
                        print("The object does not exist.")
                        any_key()
                    else:
                        continue
            elif(s3_choice == "N"):
                s3_name = input("Enter bucket name")
                key = input("enter object name")
                s3_access_key = input("Enter access key")s
                s3 = boot3.resource('s3')
                try:
                    s3 = boto3.client('s3', s3_access_key , aws_secret_access_key=...)
                    s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
                except botocore.exceptions.ClientError as e:
                    if e.response['Error']['Code'] == "404":
                        print("The object does not exist.")
                        any_key()
                    else:
                        continue
    #end project
        

        github_url = input("Enter github url")
        print()
    