import os
import pandas as pd
from azure.identity import DefaultAzureCredential
from azure.monitor.query import LogsQueryClient, MetricsQueryClient
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

credential = DefaultAzureCredential()
logs_client = LogsQueryClient(credential)
metrics_client = MetricsQueryClient(credential)

logs_client = LogsQueryClient(credential)
metrics_client = MetricsQueryClient(credential)

# Get the number of calls that exceed rate or the quota limit  
query = """AzureMetrics | where MetricName == 'BlockedCalls'"""

response = logs_client.query_workspace(workspace_id=os.getenv('LOG_WORKSPACE_ID'), query=query, 
                                       timespan=timedelta(days=30))
print(response)

data = response.tables
for table in data:
    df = pd.DataFrame(data=table.rows, columns=table.columns)
print(df)