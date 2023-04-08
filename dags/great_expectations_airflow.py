import os
from pathlib import Path
from great_expectations_provider.operators.great_expectations import (
    GreatExpectationsOperator,
)
from great_expectations.core.batch import BatchRequest
from great_expectations.data_context.types.base import (
    DataContextConfig,
    CheckpointConfig,
)

base_path = Path(__file__).parents[2]
data_dir = os.path.join(base_path, "data")
ge_root_dir = os.path.join(base_path, "great_expectations")

ge_data_context_root_dir_with_checkpoint_name_pass = GreatExpectationsOperator(
    task_id="ge_data_context_root_dir_with_checkpoint_name_pass",
    data_context_root_dir=ge_root_dir,
    checkpoint_name="taxi.pass.chk",
)

ge_data_context_config_with_checkpoint_config_pass = GreatExpectationsOperator(
    task_id="ge_data_context_config_with_checkpoint_config_pass",
    data_context_config=example_data_context_config,
    checkpoint_config=example_checkpoint_config,
)

(
    ge_data_context_root_dir_with_checkpoint_name_pass
    >> ge_data_context_config_with_checkpoint_config_pass
)
