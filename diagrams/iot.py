from diagrams import Diagram
from diagrams.aws.iot import IotCore
from diagrams.aws.compute import Lambda
from diagrams.aws.database import DynamoDB

with Diagram("IoT Architecture", show=False):
    IotCore("iot") >> Lambda("lambda") >> DynamoDB("db")