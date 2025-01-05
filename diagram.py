from diagrams import Cluster, Diagram, Edge, Group, Node, Path
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.analytics import Spark
from diagrams.openstack.user import OpenStackClient
from diagrams.azure.ml import MachineLearningStudioWebServicePlans
from diagrams.programming.framework import Svelte, Flask, FastAPI, Starlette
from diagrams.onprem.queue import Kafka
from diagrams.onprem.monitoring import Splunk, Dynatrace
from diagrams.onprem.database import MongoDB

apphosts = [
    ("app host 1"),
    ("app host 2")
]

apihosts = {

}



redishosts = {

}



mongohosts = {

}



with Diagram(name="Summarize Infrastructure", show=False):
    gradio = Svelte("Gradio")

    splunk = Splunk("Splunk Index and Dashboards")
    dynatrace = Dynatrace("Dynatrace Dashboards and Alerts")

    user_group = Group("Users")
    with user_group:
        OpenStackClient("User")
    
    mongo_cluster = Cluster("Mongo Document and Activity Cluster")
    
    with mongo_cluster:
        MongoDB("Primary")
        MongoDB("Secondary1")
        MongoDB("Secondary2")
    
    redis_cluster = Cluster("Redis Chunking Embedding Cluster")
    with redis_cluster:
        Redis("Primary")
        Redis("Secondary1")
        Redis("Secondary2")


    autosys_server = Server("ETCLab Ingestion")

    with Cluster("Summarize Cluster"):
        Server("Summ1")
        Server("Summ2")
        Server("Summ3")


        
    with Cluster("API Cluster"):
        Node("API1")
        Node("API2")


    # with Cluster("Redis Cluster"):
    #     primary = Redis("chunks")
    #     primary - Edge(color="brown", style="dashed") - Redis("replica") << Edge(label="collect") << metrics
    #     grpcsvc >> Edge(color="brown") >> primary
    #     ingsvc >> Edge(color="brown") >> primary

    # with Cluster("MongoDB Cluster"):
    #     primary = MongoDB("conversations")
    #     primary - Edge(color="brown", style="dotted") - MongoDB("replica") << Edge(label="collect") << metrics
    #     grpcsvc >> Edge(color="black") >> primary
    #     ingsvc >> Edge(color="brown") >> primary

    # aggregator = Splunk("logging")
    # aggregator >> Edge(label="forwarder") >> Edge(color="black", style="bold") >> Splunk("Splunk Query and Dashboards")

    # gradio >> Edge(color="darkgreen") << grpcsvc >> Edge(color="darkorange") >> aggregator