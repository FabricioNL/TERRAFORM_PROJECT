# TERRAFORM_PROJECT

Para testar o projeto, primeiro é necessário ter o terraform instalado. Caso ainda não tenha, leia a documentação da [hashicorp](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli).

## Sobre o projeto

O projeto consiste em um software de automação capaz de criar uma cloud privada personalizada na AWS. Basta clonar o repositório, adicionar suas chaves como variáveis de ambiente e 
rodar o script em python. 

O scrip possui uma interface baseada em perguntas. Basta responder as perguntas conforma a descrição para realizar a personalização da sua VPC.

[teste do software](https://www.youtube.com/playlist?list=PLsVpiC1hnxCo3vSf9kxCaUWIA0sNj8Djd)
[teste do H.A](https://www.youtube.com/playlist?list=PLsVpiC1hnxCpovxvp4CHmBNRxXt6iIHf5)

## Roteiro do projeto

Se você quer criar um projeto semelhante, siga o passo a passo abaixo:

1. Instale o terraform através do tutorial da hashicorp.

2. Leia a documentação da hashicorp e seus tutoriais, eles fornecerão uma base importante sobre o funcionamento de infraestrutura em código. [link](https://developer.hashicorp.com/terraform/tutorials?product_intent=terraform)

3. Crie um sistema de arquivos baseados em: main.tf, instances.tf, vcp.tf, security-groups.tf e etc. Isso permitirá que as funcionalidades estejam separadas e
o código fique mais simples para a compreensão.

4. No main.tf você precisará definir seu provider, e a região de funcionamento da sua VPC.

5. No vpc.tf, configure todas as necessidades básicas que deseja que o cliente utilize. Os valores não precisam ser hardcodes, eles serão lidos através de um arquivo de variáveis no futuro.
A VPC será importante porque todos os demais componentes estarão presentes dentro dela. Obs: para criar um componente, utilize o "resource ..."

6. Tanto no instances.tf quanto no security-groups.tf você precisa seguir o modelo da VPC. Leia a documentação de cada um dos componentes e quais os argumentos obrigatórios, 
eles precisam ser instanciados mas não necessáriamente preenchidos ali, o usuário que dará os valores.

7. Agora que já possui a insfraestrutura básica, VPC, instances e security groups, pesquise sobre o tf.vars e como utilizar loops (dica: pesquise sobre o for_each) no terraform.

8. Com o for_each conectando as variáveis com os componentes, ao iniciar `terraform init`, `terraform plan` e em seguida um `terraform apply`, sua infraestrutura será criada na AWS.

9. Crie um script em python capaz de pedir input para o usuário e escrever esses inputs no arquivo tfvars. Isso automatizará a personalização. dica: use a biblioteca `os` para aplicar as mudanças
de maneira automática.

10. Com a automação das variáveis prontas, pesquise sobre como criar usuários e regras para eles. O processo é o mesmo!

Após ter feito todo o roteiro, deve ter percebido que a cada novidade, basta adicionar mais componentes e regras de personalização.


