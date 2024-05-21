# Regra do EventBridge para agendar a execução diária
resource "aws_cloudwatch_event_rule" "daily_schedule" {
  name                = "daily-schedule"
  description         = "Daily schedule to trigger state machines"
  schedule_expression = "cron(0 7 * * ? *)"
}

# Alvo do EventBridge para a primeira máquina de estado (webscraper_infom)
resource "aws_cloudwatch_event_target" "state_machine_target_webscraper_infom" {
  rule      = aws_cloudwatch_event_rule.daily_schedule.name
  target_id = "StepFunctionsStateMachineTargetWebscraperInfom"
  arn       = aws_sfn_state_machine.state_machine_webscraper_infom.arn
  role_arn  = aws_iam_role.step_functions_role.arn
}

# Alvo do EventBridge para a segunda máquina de estado (crypto)
resource "aws_cloudwatch_event_target" "state_machine_target_crypto" {
  rule      = aws_cloudwatch_event_rule.daily_schedule.name
  target_id = "StepFunctionsStateMachineTargetCrypto"
  arn       = aws_sfn_state_machine.state_machine_crypto.arn
  role_arn  = aws_iam_role.step_functions_role.arn
}

# Alvo do EventBridge para a terceira máquina de estado (stocks)
resource "aws_cloudwatch_event_target" "state_machine_target_stocks" {
  rule      = aws_cloudwatch_event_rule.daily_schedule.name
  target_id = "StepFunctionsStateMachineTargetStocks"
  arn       = aws_sfn_state_machine.state_machine_stocks.arn
  role_arn  = aws_iam_role.step_functions_role.arn
}