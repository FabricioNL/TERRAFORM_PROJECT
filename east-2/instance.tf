#bloco de criação de instancias
resource "aws_instance" "app_server" {
  for_each = var.flavors_config
  
  ami = "ami-0a59f0e26c55590e9" #east-2
  
  instance_type = each.value.flavor

  vpc_security_group_ids = length(each.value.security_group) > 0 ? [for value in each.value.security_group : aws_security_group.sg[value].id] : ["sg-0c3c1c37e088684c8"]

  #adicionando todas as partes de VPC
  subnet_id = "${aws_subnet.prod-subnet-public-1.id}"

  tags = {
    Name = each.key
  }
}
