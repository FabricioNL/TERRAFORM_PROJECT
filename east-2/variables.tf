variable "flavors_config" {
  description = "Flavors of the EC2 instances to be created"
  type        = map(object({
    flavor    = string
    security_group = list(string)
  }))

  default     = {

  }
}

variable "users_config" {
  description = "Users to be created"
  type        = map(string)
  default     = {

  }
}

variable "security_config" {
  description = "Security groups to be created"
  type        = map(string)
  default     = {

  }
}

variable "user_policys" {
  description = "User policy to be created"
  type        = map(string)
  default     = {

  }
  
}

variable "security_ingress" {
  type        = object({
    description      = string 
    from_port        = number
    to_port          = number
    protocol         = string
    cidr_blocks      = list(string)
  })

  default     = {
    description      = "TLS from VPC"
    from_port        = 443
    to_port          = 443
    protocol         = "tcp"
    cidr_blocks      = ["10.0.0.0/16"]
  }
}
  
variable "security_engress" {
  type        = object({
    from_port        = number
    to_port          = number
    protocol         = string
    cidr_blocks      = list(string)
    ipv6_cidr_blocks = list(string)
  })

  default     = {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}