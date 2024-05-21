# ## rds DB using tf


# resource "aws_db_instance" "rds_pa_xpe" {
#   engine              = "postgres"
#   engine_version      = "16.1"
#   instance_class      = "db.t3.micro"
#   allocated_storage   = 20
#   storage_type        = "gp2"
#   identifier          = "${var.project_name}-rds"
#   username            = var.db_username
#   password            = var.db_password
#   publicly_accessible = true
#   skip_final_snapshot = true

#   tags = {
#     Name = var.project_name
#   }
# }