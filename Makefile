
install_requirements:
	@pip install -r requirements.txt

streamlit:
	@streamlit run Welcome_to_Shipvision.py

# clean:
# 	@rm -fr */__pycache__
# 	@rm -fr __init__.py
# 	@rm -fr build
# 	@rm -fr dist
# 	@rm -fr *.dist-info
# 	@rm -fr *.egg-info
# 	-@rm model.joblib
