# resource "aws_s3_bucket" "example" {
#   bucket = "${var.project_name}-${var.bucket_sufix}"

#   tags = {
#     Name = var.project_name
#   }
# }