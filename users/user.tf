resource "aws_iam_user" "user" {

  for_each = var.users_config
  name = each.value

  tags = {
    Name = each.value
  }
}

resource "aws_iam_access_key" "user" {
  for_each = aws_iam_user.user
  user    = each.value.name
}
