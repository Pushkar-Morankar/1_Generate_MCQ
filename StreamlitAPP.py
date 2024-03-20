import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcq_generator.utils import read_file,get_table_data
import streamlit as st
from langchain_community.callbacks import get_openai_callback
from src.mcq_generator.MCQ_generator import generate_evaluate_chain
from src.mcq_generator.logger import logging