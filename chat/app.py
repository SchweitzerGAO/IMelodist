import os

os.system("pip install modelscope")

# run demo
os.system("streamlit run chat/IMelodist_deploy.py --server.address=0.0.0.0 --server.port 7860")
