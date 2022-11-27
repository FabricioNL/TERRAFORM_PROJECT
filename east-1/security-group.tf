resource "aws_security_group" "sg" {
  vpc_id = "${aws_vpc.vpc.id}"

  for_each = var.security_config
  name = each.value

  ingress {
    from_port = var.security_ingress["from_port"]
    to_port = var.security_ingress["to_port"]
    protocol = var.security_ingress["protocol"]
    cidr_blocks = var.security_ingress["cidr_blocks"]
  }

  egress {
    from_port        = var.security_engress["from_port"]
    to_port          = var.security_engress["to_port"]
    protocol         = var.security_engress["protocol"]
    cidr_blocks      = var.security_engress["cidr_blocks"]
    ipv6_cidr_blocks = var.security_engress["ipv6_cidr_blocks"]
  }
  
  tags = {
    Name = each.value
  }

}
