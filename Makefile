
install_requirements:
	@pip install -r requirements.txt

streamlit:
	@streamlit run pages/1_product_demo.py --server.enableXsrfProtection false

# clean:
# 	@rm -fr */__pycache__
# 	@rm -fr __init__.py
# 	@rm -fr build
# 	@rm -fr dist
# 	@rm -fr *.dist-info
# 	@rm -fr *.egg-info
# 	-@rm model.joblib
