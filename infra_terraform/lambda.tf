resource "aws_iam_role" "lambda_role" {
 name   = "terraform_aws_lambda_role"
 assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# IAM policy for logging from a lambda

resource "aws_iam_policy" "iam_policy_for_lambda" {

  name         = "aws_iam_policy_for_terraform_aws_lambda_role"
  path         = "/"
  description  = "AWS IAM Policy for managing aws lambda role"
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*",
      "Effect": "Allow"
    }
  ]
}
EOF
}

# Policy Attachment on the role.

resource "aws_iam_role_policy_attachment" "attach_iam_policy_to_iam_role" {
  role        = aws_iam_role.lambda_role.name
  policy_arn  = aws_iam_policy.iam_policy_for_lambda.arn
}

# Ads the policy to the role of s3 to.
data "aws_iam_policy" "s3_policy" {
  arn = var.iam_bucket_arn
}

resource "aws_iam_role_policy_attachment" "attach_s3_policy" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = data.aws_iam_policy.s3_policy.arn
}

# Create a lambda function
# In terraform ${path.module} is the current directory.
resource "aws_lambda_function" "terraform_lambda_crypto" {
 filename                       = var.zip_path_1
 function_name                  = "terraform-lambdafun-cripto"
 role                           = aws_iam_role.lambda_role.arn
 handler                        = "lambda_function.lambda_handler"
 runtime                        = "python3.12"
 memory_size                    = 512 
 timeout                        = 60
 depends_on                     = [aws_iam_role_policy_attachment.attach_iam_policy_to_iam_role]
 layers = [
    var.layer_1_arn, 
    var.layer_2_arn
  ]
}

# # Create a lambda function event invoke config
# resource "aws_lambda_function_event_invoke_config" "teste_evento" {
#   function_name = aws_lambda_function.terraform_lambda_func1.function_name
# }


resource "aws_lambda_function" "terraform_lambda_webscraper_infom" {
 filename                       = var.zip_path_2
 function_name                  = "terraform-lambdafun-webscraper-fiis"
 role                           = aws_iam_role.lambda_role.arn
 handler                        = "lambda_function.lambda_handler"
 runtime                        = "python3.12"
 memory_size                    = 512 
 timeout                        = 60
 depends_on                     = [aws_iam_role_policy_attachment.attach_iam_policy_to_iam_role]
 layers = [
    var.layer_1_arn, 
    var.layer_2_arn
  ]
}


resource "aws_lambda_function" "terraform_lambda_stocks" {
 filename                       = var.zip_path_3
 function_name                  = "terraform-lambdafun-brapi_stocks"
 role                           = aws_iam_role.lambda_role.arn
 handler                        = "lambda_function.lambda_handler"
 runtime                        = "python3.12"
 memory_size                    = 512 
 timeout                        = 60
 depends_on                     = [aws_iam_role_policy_attachment.attach_iam_policy_to_iam_role]
 layers = [
    var.layer_1_arn, 
    var.layer_2_arn
  ]
}


output "teraform_aws_role_output" {
 value = aws_iam_role.lambda_role.name
}

output "teraform_aws_role_arn_output" {
 value = aws_iam_role.lambda_role.arn
}

output "teraform_logging_arn_output" {
 value = aws_iam_policy.iam_policy_for_lambda.arn
}