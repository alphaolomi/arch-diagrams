from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Microservices Architecture", show=False):
    lb = ELB("lb")
    svc_group = [EC2("web1"), EC2("web2"), EC2("web3")]
    db = RDS("db")

    lb >> svc_group >> db