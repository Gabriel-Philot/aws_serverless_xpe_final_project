resource "aws_iam_role" "step_functions_role" {
  name = "StepFunctionsExecutionRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = {
        Service = "states.amazonaws.com"
      },
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "step_functions_policy" {
  role = aws_iam_role.step_functions_role.id

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect   = "Allow",
        Action   = "lambda:InvokeFunction",
        Resource = [
            aws_lambda_function.terraform_lambda_stocks.arn,
            aws_lambda_function.terraform_lambda_crypto.arn,
            aws_lambda_function.terraform_lambda_webscraper_infom.arn
        ]
      },
      {
        Effect   = "Allow",
        Action   = [
          "glue:StartJobRun",
          "glue:GetJobRun",
          "glue:GetJobRuns"
        ],
        Resource = [
            aws_glue_job.stocks.arn,
            aws_glue_job.crypto.arn,
            aws_glue_job.webscraper_infom.arn
        ]
      }
    ]
  })
}

resource "aws_sfn_state_machine" "state_machine_stocks" {
  name     = "stocks-state-machine"
  role_arn = aws_iam_role.step_functions_role.arn

  definition = jsonencode({
    Comment: "A simple AWS Step Functions state machine that executes a Lambda function and a Glue job.",
    StartAt: "Invoke Lambda Function",
    States: {
      "Invoke Lambda Function": {
        Type: "Task",
        Resource: aws_lambda_function.terraform_lambda_stocks.arn,
        Next: "Start Glue Job"
      },
      "Start Glue Job": {
        Type: "Task",
        Resource: "arn:aws:states:::glue:startJobRun.sync",
        Parameters: {
          JobName: aws_glue_job.stocks.name
        },
        End: true
      }
    }
  })
}


resource "aws_sfn_state_machine" "state_machine_crypto" {
  name     = "crypto-state-machine"
  role_arn = aws_iam_role.step_functions_role.arn

  definition = jsonencode({
    Comment: "A simple AWS Step Functions state machine that executes a Lambda function and a Glue job.",
    StartAt: "Invoke Lambda Function",
    States: {
      "Invoke Lambda Function": {
        Type: "Task",
        Resource: aws_lambda_function.terraform_lambda_crypto.arn,
        Next: "Start Glue Job"
      },
      "Start Glue Job": {
        Type: "Task",
        Resource: "arn:aws:states:::glue:startJobRun.sync",
        Parameters: {
          JobName: aws_glue_job.crypto.name
        },
        End: true
      }
    }
  })
}

resource "aws_sfn_state_machine" "state_machine_webscraper_infom" {
  name     = "webscraper_infom-state-machine"
  role_arn = aws_iam_role.step_functions_role.arn

  definition = jsonencode({
    Comment: "A simple AWS Step Functions state machine that executes a Lambda function and a Glue job.",
    StartAt: "Invoke Lambda Function",
    States: {
      "Invoke Lambda Function": {
        Type: "Task",
        Resource: aws_lambda_function.terraform_lambda_webscraper_infom.arn,
        Next: "Start Glue Job"
      },
      "Start Glue Job": {
        Type: "Task",
        Resource: "arn:aws:states:::glue:startJobRun.sync",
        Parameters: {
          JobName: aws_glue_job.webscraper_infom.name
        },
        End: true
      }
    }
  })
}