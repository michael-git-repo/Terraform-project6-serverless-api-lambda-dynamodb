resource "aws_dynamodb_table" "students" {
  name         = var.table_name
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "student_id"

  attribute {
    name = "student_id"
    type = "S"
  }
}