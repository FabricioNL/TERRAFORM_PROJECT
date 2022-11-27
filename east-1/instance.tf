#bloco de criação de instancias
resource "aws_instance" "app_server" {
  for_each = var.flavors_config
  
  ami = "ami-072d6c9fae3253f26" #east 
  
  instance_type = each.value.flavor

  vpc_security_group_ids = length(each.value.security_group) > 0 ? [for value in each.value.security_group : aws_security_group.sg[value].id] : ["sg-06bf9842f0f974835"]

  #adicionando todas as partes de VPC
  subnet_id = "${aws_subnet.prod-subnet-public-1.id}"

  tags = {
    Name = each.key
  }
}
