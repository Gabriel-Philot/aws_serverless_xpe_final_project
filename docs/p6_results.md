# Results

## Scalable Solution

The solution is scalable, capable of ingesting new data sources without impacting performance—a key premise from the start of the project. In the financial world, there's a continuous need for new data to add new assets for analysis and client portfolios. The solution ensures this through a developed ingestion framework, providing a simple and agile method to add new assets and endpoints.

## Flexible Architecture

The architecture is malleable, allowing for the scaling up or dismantling of resources without impacting existing setups, fitting new pipelines, or adapting Lambdas for existing pipelines. It has been demonstrated during the project that our architecture can smoothly ingest data in various formats—APIs, web scraping, and databases—through AWS's serverless resources. Additionally, adjusting the update frequency is easily managed in the orchestration stage by merely changing the cron configuration in AWS Step Functions.

## Data Persistence Across Layers

Data is stored across various layers, offering several advantages such as maintaining a real historical data record for legal reasons and more analytical layers focused on performance and cost-efficiency. Understanding business demands, measures can be taken to transfer less frequently used data to even cheaper storage layers (like AWS Glacier), thereby ensuring performance and cost efficiency in the same scenario.

## Centralized Data Availability via Metabase

Data is centralized and made accessible through Metabase, which interfaces with Athena, a high-performance tool capable of accessing Delta-format data, thus enhancing performance and reducing costs. Within Metabase, dashboards can be published and accessed on the web (both PC and mobile) by clients. Data and Business Analysts can also access the refined tables to conduct studies and create dashboards and reports.

## Data Quality and Observability

Observability and understanding of data ingestion are emphasized in the pipelines to enable preventive actions against failures and facilitate effective communication with other departments.

## FinOps and Cost-Efficient Architecture

The architecture is highly cost-effective, capable of handling production scenarios with minimal adjustments.

*  **POC Development Cost**: Less than $50
*  **Projected Production Cost**: $255 per month | $3060 per year 💸

## Potential Business Impact 💰

### Analysts' Time Efficiency

It's well known that analysts spend considerable hours collecting and preparing data before they can even begin their actual analysis. After a brief web search, a conservative estimate suggests that each analyst spends around 10 hours per week on these tasks (studies indicate it could be more than 30 hours). For a company with 10 analysts, this equates to about 100 hours per week, or 400 hours per month. Given the average cost of R$40 per hour for a mid-level analyst, the company spends approximately R$16,000 monthly on these preparatory tasks.

### Cost Savings with the New Solution

Our solution, projected to cost about R$1,400 per month, can significantly reduce these expenses, saving the business around R$14,000 per month or R$168,000 annually. This allows funds to be reallocated to marketing or other impactful business activities.

### Enhanced Analytical Output

Moreover, the time saved for analysts can lead to more analytical outcomes, potentially creating additional value for clients and, consequently, the business. This increase in productivity and effectiveness could translate into a competitive advantage in the marketplace.

