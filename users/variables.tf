variable "user_policys" {
  description = "User policy to be created"
  type        = map(string)
  default     = {

  }
  
}

variable "users_config" {
  description = "Users to be created"
  type        = map(string)
  default     = {

  }
}