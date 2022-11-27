resource "aws_iam_user_policy" "user_policy" {
  name = "ec2-describe"

  for_each = var.user_policys
  user = each.key 

  policy = each.value

}