cmake_minimum_required(VERSION 3.12)
project(MySwaggerToPythonModels)

# Add a custom target to run your Python script
add_custom_target(generate_models
    COMMAND ${CMAKE_COMMAND} -E env PYTHONPATH=${CMAKE_CURRENT_SOURCE_DIR} python src/tunclibs/generate_models.py
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "Generating Python models from Swagger JSON"
)

# Define the 'my_target' target to depend on the custom target
add_custom_target(my_target DEPENDS generate_models)
