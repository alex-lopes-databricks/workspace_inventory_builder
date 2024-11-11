# Databricks notebook source

# COMMAND ----------
dbutils.widgets.text("catalog_schema", "shared.workspace_inventory")

# COMMAND ----------
catalog_schema = dbutils.widgets.get("catalog_schema")
# COMMAND ----------

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.dashboards import LakeviewAPI
from string import Template

w = WorkspaceClient()

# COMMAND ----------

try:
  with open("WorkspaceInventory.lvdash.json.tmpl", "r") as f:
    s = Template(f.read())    
    w.lakeview.create("Workspace Inventory", serialized_dashboard=s.substitute(catalog_schema=catalog_schema))
    print("Dashboard was created")
except:
  print("Dashboard already exists")

# COMMAND ----------


