from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.generic.device import Mobile
from diagrams.generic.device import Tablet

with Diagram("Multi Client-Server Architecture", show=False):
    lb = ELB("lb")
    web = EC2("web")
    db = RDS("db")

    Mobile("mobile") >> lb >> web >> db
    Tablet("tablet") >> lb >> web >> db