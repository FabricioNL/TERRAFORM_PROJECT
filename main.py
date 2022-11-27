import os
import json

print("Olá! O que você deseja fazer?")
opcao = input("1 - Criar instancias e grupos de segurança\n2 - Criar usuários\n3 - Associar regras aos usuários\n4 - Deletar instancias/Grupos de Segurança/Usuarios\n5 - Listar instancias/Grupos de Segurança/Usuarios\n6 - Sair\n\n")

if int(opcao) == 1:
    print("\nVocê escolheu criar instancias e grupos de segurança")

    region = input("\nDigite a região:\n1 - us-east-1\n2 - us-east-2\n\n")

    if int(region) == 1:
        region = "east-1"
    elif int(region) == 2:
        region = "east-2"

    n = input("\nQuantas instancias você deseja criar?\n\n")

    dict_instances = {}
    dict_sg_instances = {}
    dict_security_groups = {}

    if int(n) != 0:

        for i in range(int(n)):
            name = input("\nDigite o nome da instancia: ")
            flavor_select = input("\nDigite o tipo da instancia:\n1 - t2.micro\n2 - t3.medium\n\n")

            if int(flavor_select) == 1:
                flavor = "t2.micro"
            else:
                flavor = "t3.medium"

            dict_instances[name] = {"flavor": flavor, 'security_group': []}

    
    n_security_groups = input("\nVocê gostaria de criar grupos de segurança? Se sim, digite a quantidade. Se não, digite 0.\n\n")

    if int(n_security_groups) != 0:

        for i in range(int(n_security_groups)):
            name_sg = input("\nDigite o nome do grupo de segurança: ")


            dict_security_groups[str(i+1)] = name_sg
    
    with open("{0}/security_override.tf.json".format(region), "r") as j:
        data_sg = json.loads(j.read())

    data_sg['variable']['security_config']['default'] = dict_security_groups

    with open("{0}/security_override.tf.json".format(region), "w") as j:
        json.dump(data_sg, j)

    if n_security_groups != 0:

        for k in dict_instances.keys():
            response = input(f"\nVocê gostaria de adicionar um grupo de segurança para a instancia {k}? Se não, digite n.\n\n")

            while response != 'n':

                if response != "n":
                    for i in range(int(n_security_groups)):
                        print(f"{i+1} - {dict_security_groups[str(i+1)]}")

                    response = input("\nDigite o número do grupo de segurança que você deseja adicionar.\n\n")

                    dict_instances[k]['security_group'].append(response)


                response = input(f"\nVocê gostaria de adicionar uma regra de segurança para a instancia {k}? Se não, digite n.\n\n")
    
    with open("{0}/instance_override.tf.json".format(region), "r") as j:
        data_instances = json.loads(j.read())

    data_instances['variable']['flavors_config']['default'] = dict_instances

    with open("{0}/instance_override.tf.json".format(region), "w") as j:
        json.dump(data_instances, j)


    os.chdir("/home/fabricio/learn-terraform-aws-instance/{0}".format(region))
    os.system("terraform init")
    os.system("terraform plan")
    os.system("terraform apply")

if int(opcao) == 2:

    dict_users = {}

    n_users = input("\nVocê gostaria de criar usuários? Se sim, digite a quantidade. Se não, digite 0.\n\n")

    if int(n_users) != 0:

        for i in range(int(n_users)):
            name = input("\nDigite o nome do usuario: ")
            dict_users[str(i+1)] = name
    
    with open("users/user_override.tf.json", "r") as j:
        data_users = json.loads(j.read())

    data_users['variable']['users_config']['default'] = dict_users

    with open("users/user_override.tf.json", "w") as j:
        json.dump(data_users, j)

    os.chdir("/home/fabricio/learn-terraform-aws-instance/users")
    os.system("terraform init")
    os.system("terraform plan")
    os.system("terraform apply")

if int(opcao) == 3:

    describe = """{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Action": [
            "ec2:Describe*"
          ],
          "Effect": "Allow",
          "Resource": "*"
        }
      ]
    }"""

    read =  """{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ec2:GetResourcePolicy",
                "ec2:GetDefaultCreditSpecification",
                "ec2:GetIpamResourceCidrs",
                "ec2:GetIpamPoolCidrs",
                "ec2:GetInstanceUefiData",
                "ec2:GetEbsEncryptionByDefault",
                "ec2:ExportClientVpnClientConfiguration",
                "ec2:GetCapacityReservationUsage",
                "ec2:GetHostReservationPurchasePreview",
                "ec2:GetNetworkInsightsAccessScopeAnalysisFindings",
                "ec2:GetSubnetCidrReservations",
                "ec2:GetConsoleScreenshot",
                "ec2:GetConsoleOutput",
                "ec2:ExportClientVpnClientCertificateRevocationList",
                "ec2:GetLaunchTemplateData",
                "ec2:GetSerialConsoleAccessStatus",
                "ec2:GetFlowLogsIntegrationTemplate",
                "ec2:GetEbsDefaultKmsKeyId",
                "ec2:GetManagedPrefixListEntries",
                "ec2:GetCoipPoolUsage",
                "ec2:GetNetworkInsightsAccessScopeContent",
                "ec2:GetReservedInstancesExchangeQuote",
                "ec2:GetAssociatedEnclaveCertificateIamRoles",
                "ec2:GetIpamAddressHistory",
                "ec2:GetPasswordData",
                "ec2:GetAssociatedIpv6PoolCidrs",
                "ec2:GetSpotPlacementScores",
                "ec2:GetManagedPrefixListAssociations"
            ],
            "Resource": "*"
        }
    ]
}"""

    dict_rules = {}
    dict_final = {}
    template  = {"variable": {"user_policys": {"default": {}}}}

    with open("users/user_override.tf.json", "r") as j:
        data_users = json.loads(j.read())
    
    for k, v in data_users['variable']['users_config']['default'].items():
        dict_rules[v] = ""
    
    for k in dict_rules.keys():
        response = input(f"\nVocê gostaria de adicionar uma regra de segurança para o usuario {k}? Se não, digite n.\n\n")
        
        if (response != 'n'):

            option = input("Selecione uma opção:\n1 - Describe\n2 - Read\n\n")

            if int(option) == 1:
                dict_rules[k] = describe
            
            if int(option) == 2:
                dict_rules[k] = read
    
    for k, v in dict_rules.items():
        if v != "":
            dict_final[k] = v

    template['variable']['user_policys']['default'] = dict_final

    with open("users/policys_override.tf.json", "w") as j:
        json.dump(template, j)

    os.chdir("/home/fabricio/learn-terraform-aws-instance/users")
    os.system("terraform init")
    os.system("terraform plan")
    os.system("terraform apply")
        
if int(opcao) == 4:
    region = input("\nDigite a região:\n1 - us-east-1\n2 - us-east-2\n\n")

    if int(region) == 1:
        region = "east-1"
    elif int(region) == 2:
        region = "east-2"

    respose = input("\n1 - Destruir instancias e grupos de seguranca\n2 - Destruir usuarios (Se tiver politicas de segurança, apague-as antes)\n3 - Destruir apenas políticas de usuarios\n\n")
    
    if int(respose) == 1:

        with open("{0}/instance_override.tf.json".format(region), "r") as j:
            data_instances = json.loads(j.read())

        data_instances['variable']['flavors_config']['default'] = {}

        with open("{0}/instance_override.tf.json".format(region), "w") as j:
            json.dump(data_instances, j)
        

        with open("{0}/security_override.tf.json".format(region), "r") as j:
            data_sg = json.loads(j.read())
        
        data_sg['variable']['security_config']['default'] = {}

        with open("{0}/security_override.tf.json".format(region), "w") as j:
            json.dump(data_sg, j)

        os.chdir("/home/fabricio/learn-terraform-aws-instance/{0}".format(region))
        os.system("terraform init")
        os.system("terraform plan")
        os.system("terraform apply")
    
    if int(respose) == 2:

        with open("users/user_override.tf.json".format(region), "r") as j:
            data_users = json.loads(j.read())

        data_users['variable']['users_config']['default'] = {}

        with open("users/user_override.tf.json".format(region), "w") as j:
            json.dump(data_users, j)

        with open("users/policys_override.tf.json".format(region), "r") as j:
            data_policys = json.loads(j.read())

        data_policys['variable']['user_policys']['default'] = {}

        with open("users/policys_override.tf.json".format(region), "w") as j:
            json.dump(data_policys, j)

        os.chdir("/home/fabricio/learn-terraform-aws-instance/users".format(region))
        os.system("terraform init")
        os.system("terraform plan")
        os.system("terraform apply")
    
    if int(respose) == 3:

        with open("users/policys_override.tf.json".format(region), "r") as j:
            data_policys = json.loads(j.read())

        data_policys['variable']['user_policys']['default'] = {}

        with open("users/policys_override.tf.json".format(region), "w") as j:
            json.dump(data_policys, j)

        os.chdir("/home/fabricio/learn-terraform-aws-instance/users".format(region))
        os.system("terraform init")
        os.system("terraform plan")
        os.system("terraform apply")
        
if int(opcao) == 5:

    with open("east-1/terraform.tfstate", "r") as j:
        data_instances_east_1 = json.loads(j.read()) 

    with open("east-2/terraform.tfstate", "r") as j:
        data_instances_east_2 = json.loads(j.read()) 
    
    with open("users/terraform.tfstate", "r") as j:
        data_instances_users = json.loads(j.read()) 

    
    instancias_east_1 = []
    security_groups_east_1 = []

    instancias_east_2 = []
    security_groups_east_2 = []

    users = {}

    for i in data_instances_east_1['resources']:
        if i['type'] == "aws_instance":
            for k in i['instances']:
                instancias_east_1.append(k['attributes']['tags']['Name'])
    
    for i in data_instances_east_1['resources']:
        if i['type'] == "aws_security_group":
            for k in i['instances']:
                if k['attributes'] != None:
                    if k['attributes']['tags'] != None:
                        security_groups_east_1.append(k['attributes']['tags']['Name'])

    for i in data_instances_east_2['resources']:
        if i['type'] == "aws_instance":
            for k in i['instances']:
                if k['attributes'] != None:
                    if k['attributes']['tags'] != None:
                        instancias_east_2.append(k['attributes']['tags']['Name'])
    
    for i in data_instances_east_2['resources']:
        if i['type'] == "aws_security_group":
            for k in i['instances']:
                if k['attributes'] != None:
                    if k['attributes']['tags'] != None:
                        security_groups_east_2.append(k['attributes']['tags']['Name'])

    for i in data_instances_users['resources']:
        if i['type'] == "aws_iam_user":
            for k in i['instances']:
                users[k['attributes']['name']] = ""
    
    for i in data_instances_users['resources']:
        if i['type'] == "aws_iam_user_policy":
            for k in i['instances']:
                if k['index_key'] in users:
                    users[k['index_key']] = k['attributes']['name']
                

                
    print("\nAs instancias criadas em east-1 são: ")
    print(instancias_east_1)

    print("\nOs grupos de segurança criados em east-1 são: ")
    print(security_groups_east_1)

    print("\nAs instancias criadas em east-2 são: ")
    print(instancias_east_2)

    print("\nOs grupos de segurança criados em east-2 são: ")
    print(security_groups_east_2)

    print("\nOs usuários criados e suas politicas: ")
    print(users)

