from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Monolith Architecture", show=False):
    ELB("lb") >> EC2("web") >> RDS("db")