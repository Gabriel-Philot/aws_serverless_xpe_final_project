# Definindo o papel (role) para Step Functions com a política de confiança adequada
resource "aws_iam_role" "step_functions_role_new" {
  name = "StepFunctionsExecutionRoleNew"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = [
            "states.amazonaws.com",
            "scheduler.amazonaws.com"
          ]
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
}

# Atualizando a política IAM para incluir permissão de start execution nas máquinas de estado e permissões do scheduler
resource "aws_iam_role_policy" "event_bridge_policy" {
  role = aws_iam_role.step_functions_role_new.id

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect   = "Allow",
        Action   = "lambda:InvokeFunction",
        Resource = [
          aws_lambda_function.terraform_lambda_crypto.arn,
          aws_lambda_function.terraform_lambda_webscraper_infom.arn,
          aws_lambda_function.terraform_lambda_stocks.arn
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
      },
      {
        Effect   = "Allow",
        Action   = [
          "states:StartExecution"
        ],
        Resource = [
          aws_sfn_state_machine.state_machine_webscraper_infom.arn,
          aws_sfn_state_machine.state_machine_crypto.arn,
          aws_sfn_state_machine.state_machine_stocks.arn
        ]
      },
      {
        Effect   = "Allow",
        Action   = [
          "scheduler:CreateSchedule",
          "scheduler:UpdateSchedule",
          "scheduler:DeleteSchedule"
        ],
        Resource = "*"
      }
    ]
  })
}

# Definindo um agendamento no EventBridge Scheduler para acionar as máquinas de estado diariamente às 7h
resource "aws_scheduler_schedule" "daily_schedule_webscraper_infom" {
  name               = "daily-schedule-webscraper-infom"
  schedule_expression = "cron(0 7 * * ? *)"
  flexible_time_window {
    mode = "OFF"
  }
  target {
    arn       = aws_sfn_state_machine.state_machine_webscraper_infom.arn
    role_arn  = aws_iam_role.step_functions_role_new.arn
  }
}

resource "aws_scheduler_schedule" "daily_schedule_crypto" {
  name               = "daily-schedule-crypto"
  schedule_expression = "cron(0 7 * * ? *)"
  flexible_time_window {
    mode = "OFF"
  }
  target {
    arn       = aws_sfn_state_machine.state_machine_crypto.arn
    role_arn  = aws_iam_role.step_functions_role_new.arn
  }
}

resource "aws_scheduler_schedule" "daily_schedule_stocks" {
  name               = "daily-schedule-stocks"
  schedule_expression = "cron(0 7 * * ? *)"
  flexible_time_window {
    mode = "OFF"
  }
  target {
    arn       = aws_sfn_state_machine.state_machine_stocks.arn
    role_arn  = aws_iam_role.step_functions_role_new.arn
  }
}
